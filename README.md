MASTER
# CV Generator Master
Build by using Django3 and Python3

# Deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Insert your own db configuration settings (see example secret.env):
and change file name to .env:

`DB_PASSWORD`,
`DB_NAME`,
`DB_USER`

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

4 - Run app:

`python3 manage.py runserver`

Project was deployed to Heroku:

`heroku run python manage.py createsuperuser -a cvs-generator`

https://cvs-generator.herokuapp.com/