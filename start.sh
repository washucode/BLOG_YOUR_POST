export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL='postgresql+psycopg2://esther:p@localhost/blog'
# python3 manage.py server
# python manage.py db migrate -m "Add column profile image to table users"
python manage.py db upgrade