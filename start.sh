export SECRET_KEY=435313ea80b5a872114356a1
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL='postgresql+psycopg2://esther:p@localhost/newblog'

python3 manage.py test
# python3 manage.py db migrate -m "redo migrations"
# python manage.py db migrate -m "Deployment"
# python manage.py db upgrade



