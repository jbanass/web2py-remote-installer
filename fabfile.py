from __future__ import with_statement
from fabric.api import local, env, run, cd, get, settings, abort
from fabric.operations import put
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
import os

env.hosts = [''] #Remote machine address
env.user = '' #Remote machine username
env.password = '' #Remote machine pw
web2py.link = 'http://www.web2py.com/examples/static/web2py_src.zip'
web2py.port = '0001'
web2py.ip = '0.0.0.0'
web2py.pw = 'pw'

def deploy_and_unzip(zipfile, folder):
    with settings(warn_only=True):
        if not os.path.exists(zipfile) and not confirm("File not there. Continue?"):
            abort("Aborting at user request")
        put(zipfile, folder)
        run('unzip ' + zipfile)

def install_web2py():
    if not os.path.exists('web2py_src.zip') and confirm("web2py does not exist. Download?:"):
        local('wget {}'.format(web2py.link))
    deploy_and_unzip('web2py_src.zip','')
    with cd('web2py'):
        run('python web2py.py -i {} -p {} -a {}'.format(web2py.ip, web2py.port, web2py.pw))
