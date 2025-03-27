# filepath: untitled:/var/www/martingubala_pythonanywhere_com_wsgi.py
import os
import sys
from django.core.wsgi import get_wsgi_application

# # Correct the path to your project directory
sys.path.append('/home/martingubala/WAD2-8C/WAD2_Project')

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'WAD2_Project.settings'
application = get_wsgi_application()

# # Activate the virtual environment
# activate_this = '/home/martingubala/.virtualenvs/yourenvname/bin/activate_this.py'
# with open(activate_this) as file_:
#     exec(file_.read(), dict(__file__=activate_this))

# Import and set up the WSGI application

