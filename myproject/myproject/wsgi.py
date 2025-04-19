import os
from django.core.wsgi import get_wsgi_application

# Modified for nested project structure
<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.myproject.settings')
application = get_wsgi_application()
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()
>>>>>>> 13a28653f9a0efef4af998ecd9891eb247804bbd
