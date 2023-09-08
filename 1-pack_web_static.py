#!/usr/bin/python3
"""
Deploy a new version of our static files
"""

import os
from fabric.api import local


def do_pack():
    """Pack the static files to a tgz archive"""
    # Get the current date and time for naming the archive
    timestamp = local("date +'%Y%m%d%H%M%S'", capture=True)

    # Define the archive filename
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Define the local paths
    local_web_static_path = "./web_static"
    local_archive_path = "./versions/{}".format(archive_name)

    # Create the versions directory if it doesn't exist
    local("mkdir -p ./versions")

    # Use tar to create the archive from the web_static folder
    local("tar -czvf {} {}".format(local_archive_path, local_web_static_path))

     # Check if the archive was created successfully
    if os.path.exists(local_archive_path):
        return local_archive_path
    return None
