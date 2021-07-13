from flask import Flask
from urllib3 import request
import subprocess

app = Flask(__name__)


@app.route('/')
def execute2(cmd):
  try:
    retcode = subprocess.call(cmd, shell=True)
  except OSError as e:
    pass

@app.route("/dns")
def page():
  hostname = request.values.get(hostname)
  cmd = 'nslookup ' + hostname

  return subprocess.check_output(cmd, shell=True)