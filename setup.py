import subprocess
from setuptools import setup

setup(version=subprocess.check_output(['git', 'describe']).decode('utf8').strip().lstrip('v'))
