#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents
   of the web_static folder of the AirBnB Clone repo,
   using the function do_pack."""
from fabric.api import local
from os.path import isdir
import datetime

def do_pack():
    """generates a .tgz archive"""
    try:
        if not isdir("versions"):
            local("mkdir versions")
        clock = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        archive = "versions/web_static_{}.tgz".format(clock)
        local("tar -czf {} web_static".format(archive))
        return archive
    except:
        return None
