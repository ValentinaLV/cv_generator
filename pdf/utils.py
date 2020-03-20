from io import BytesIO

import xhtml2pdf.pisa as pisa
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template

from cv_generator.settings import CV_PER_PAGES
from .models import Profile


class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)


def posts_search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        resumes = Profile.objects.filter(
            Q(name__icontains=search_query)
        ).distinct()
    else:
        resumes = Profile.objects.all()
    return resumes


def posts_pagination(request):
    paginator = Paginator(posts_search(request), CV_PER_PAGES)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    return {
        'page_obj': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
