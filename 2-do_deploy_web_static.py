#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy.
"""


from fabric.api import *



env.hosts = ['54.83.131.175', '54.144.21.80']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):

    """Distributes an archive to your web servers."""
    try:
        if path.exists(archive_path):
            return False

        # Upload archive to web server
        put(archive_path, '/tmp/')

        # Creating target directory.
        time_stamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'.format(time_stamp))

        # Uncompressing and deleting the archive to the newly created folder.
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/releases/web_static_{}/'.format(time_stamp, time_stamp))
        run('rm /tmp/web_static_{}.tgz'.format(time_stamp))

        # Deleting symbolic link from the web server
        run('sudo rm -rf /data/web_static/current/')

        # Creating new symbolic link
        run("sudo ln -s /data/web_static/releases/web_static_{} /data/web_static/current".format(time_stamp))
    except:
        return False

    return True
