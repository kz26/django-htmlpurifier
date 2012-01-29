import subprocess
import os
from django.conf import settings

HTMLPURIFIER_SCRIPT_PATH = getattr(settings, 'HTMLPURIFIER_SCRIPT_PATH', 'htmlpurifier-cli.php')

def purify(data):
    cl = ['php', '-f', HTMLPURIFIER_SCRIPT_PATH]
    cwd = os.path.dirname(__file__) 
    p = subprocess.Popen(cl, cwd=cwd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    out = p.communicate(data)
    return out[0]

