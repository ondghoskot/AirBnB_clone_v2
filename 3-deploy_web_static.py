#!/usr/bin/python3
"""Fabric script to deploy web_static"""
from fabric.api import local, run, env, put
from os.path import *
import datetime
env.user = "ubuntu"
env.hosts = ['54.197.21.225', '52.87.255.100']
archive_path = None


def do_pack():
    """generates a .tgz archive"""
    try:
        if not isdir("versions"):
            local("mkdir versions")
        clock = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        archive = "versions/web_static_{}.tgz".format(clock)
        local("tar -cvzf {} web_static".format(archive))
        archive_path = archive
        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    filename = splitext(basename(archive_path))[0]
    path0 = '/data/web_static/releases/'
    path1 = '/data/web_static/current'
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p {}{}/".format(path0, filename))
        run("sudo tar -xzf /tmp/{}.tgz -C {}{}/"
            .format(filename, path0, filename))
        run("sudo rm /tmp/{}.tgz".format(filename))
        run("sudo mv {}{}/web_static/* {}{}/"
            .format(path0, filename, path0, filename))
        run("sudo rm -rf {}{}/web_static".format(path0, filename))
        run("sudo rm -rf {}".format(path1))
        run("sudo ln -s {}{}/ {}".format(path0, filename, path1))
        return True
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    global archive_path
    if archive_path is None:
        path_arch = do_pack()
        if path_arch is None:
            return False
        archive_path = path_arch
    return do_deploy(archive_path)
