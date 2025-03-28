# filepath: untitled:/var/www/martingubala_pythonanywhere_com_wsgi.py
# import os
# import sys

# Correct the path to your project directory
# sys.path.append('/home/martingubala/WAD2-8C/WAD2_Project')

# Set the Django settings module
# os.environ['DJANGO_SETTINGS_MODULE'] = 'WAD2_Project.settings'

# Activate the virtual environment
# activate_this = '/home/martingubala/.virtualenvs/yourenvname/bin/activate_this.py'
# with open(activate_this) as file_:
#     exec(file_.read(), dict(__file__=activate_this))

# Import and set up the WSGI application
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()


import os
import sys

# Set the path to the project root
path = '/home/Jasoom/WAD2-8C/WAD2-8C/WAD2_Project'
if path not in sys.path:
    sys.path.append(path)

# Set the environment variable for Django's settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'WAD2_Project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()