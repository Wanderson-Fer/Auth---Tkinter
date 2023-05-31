from getpass import getuser as user
from datetime import datetime as dt
import venv
import os

print('\n--------------------------')
print('>>>', user())
print('>>>', dt.now())
curdir = os.path.abspath(os.getcwd())
print('>>>', curdir)
print('\t-', type(curdir))

venv_dir = curdir + r'\.venv'

venv.create(venv_dir, system_site_packages=False)

print('>>> Created successfully!')
