from app import create_app
from gunicorn.app.wsgiapp import WSGIApplication

application = WSGIApplication()
application.app_uri = 'create_app:app'  # Replace 'yourapp' with the name of your main application and 'app' with the name of your Flask or Django application instance