from __future__ import absolute_import

import os
import pwd
import subprocess

from celery import shared_task


@shared_task
def run(user, directory, command):
    uid = pwd.getpwnam(user)[2]
    status = subprocess.call(
        command,
        shell=True,
        cwd=directory,
        preexec_fn=lambda: os.setuid(uid),
    )
