export SECRET_KEY=435313ea80b5a872114356a1
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL='postgresql+psycopg2://esther:p@localhost/blog'
# python3 manage.py server
# python manage.py db migrate -m "REmove unique constraint from class Comments"
python manage.py db upgrade