from fabric import *
from fabric.connection import *
from fabric import task
from invoke import Exit
# import fabric.contrib.project as project
import os
import shutil
import sys
import socketserver

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
DEPLOY_PATH = "output"

# Github Pages configuration
GITHUB_PAGES_BRANCH = "gh-pages"

# Port for `serve`
PORT = 8000

@task
def clean(c):
  """Remove generated files"""
  if os.path.isdir(DEPLOY_PATH):
    shutil.rmtree(DEPLOY_PATH)
    os.makedirs(DEPLOY_PATH)

@task
def build(c):
  """Build local version of site"""
  c.run('pelican -s pelicanconf.py')

@task
def rebuild(c):
  """`clean` then `build`"""
  clean(c)
  build(c)

@task
def regenerate(c):
  """Automatically regenerate site upon file modification"""
  c.run('pelican -r -s pelicanconf.py')

@task
def serve(c):
  """Serve site at http://localhost:8000/"""
  os.chdir(DEPLOY_PATH)

  class AddressReuseTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

  server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

  sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
  server.serve_forever()

@task
def reserve(c):
  """`build`, then `serve`"""
  build(c)
  serve(c)

@task
def preview(c):
  """Build production version of site"""
  c.run('pelican -s publishconf.py')

@task
def gh_pages(c):
  """Publish to GitHub Pages"""
  clean(c)
  c.run('pelican -s publishconf.py')
  c.run("ghp-import -b {} {}".format(GITHUB_PAGES_BRANCH, DEPLOY_PATH))
  c.run("git push origin {}".format(GITHUB_PAGES_BRANCH))
