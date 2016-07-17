    #!/usr/bin/python

import os

virtenv = os.environ['APPDIR'] + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    exec(compile(open(virtualenv).read(), virtualenv, 'exec'), dict(__file__=virtualenv))
except IOError:
    pass

from api import application as application