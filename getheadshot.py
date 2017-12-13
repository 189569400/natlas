#!/usr/bin/python3

import subprocess
import os

# apt-get install wkhtmltopdf vncsnapshot
# wkhtmltoimage --width 50 --quality 80 -f jpg <target> out.jpg
# vncsnapshot -quality 50 <target> out.jpg

def getheadshot(ip,rand):

  # display hack, wkhtmltoimage doesn't like to run headless
  # this requires you to run a vncserver or something
  os.environ["DISPLAY"]=':1'

  process = subprocess.Popen(["vncsnapshot","-quality","50",ip,"data/nweb."+rand+".headshot.jpg"],stdout=subprocess.PIPE)
  try:
    out, err = process.communicate(timeout=60)
    if process.returncode is 0:
      return True
  except:
    try:
      print("killing slacker process")
      process.kill()
    except:
      print("okay, seems like it was already dead")

  process = subprocess.Popen(["wkhtmltoimage","--javascript-delay","3000","--width","800","--height","600","--quality","80","-f","jpg","http://"+ip,"data/nweb."+rand+".headshot.jpg"],stdout=subprocess.PIPE)

  try:
    out, err = process.communicate(timeout=60)
    if process.returncode is 0:
      return True
  except:
    try:
      print("killing slacker process")
      process.kill()
    except:
      print("okay, seems like it was already dead")

  process = subprocess.Popen(["wkhtmltoimage","--javascript-delay","3000","--width","800","--height","600","--quality","80","-f","jpg","https://"+ip,"data/nweb."+rand+".headshot.jpg"],stdout=subprocess.PIPE)
  try:
    out, err = process.communicate(timeout=60)
    if process.returncode is 0:
      return True
  except:
    try:
      print("killing slacker process")
      process.kill()
    except:
      print("okay, seems like it was already dead")

  print("seems like nothing worked")
  return False