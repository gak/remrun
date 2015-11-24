import os
import re
from textwrap import dedent

import yaml
from fabric.decorators import task
from fabric.operations import local


@task
def update_django_dockerfile():
    '''
    Updates the web/Dockerfile with specific python packages so it can be
    cached during build
    '''
    packages = open('requirements.txt').readlines()

    p = []
    for package in packages:
        if package.startswith('-e '):
            p.append(package[3:])
        else:
            p.append(package)
    packages = p

    # Strip the comment after the package generated by pip-compile
    packages = [re.sub(' +# via .*$', '', a) for a in packages]

    # Whitespace is the devil
    packages = [a.strip() for a in packages]

    # Don't include comments
    packages = [a for a in packages if not a.startswith('#')]

    # Don't include local wheels
    packages = [a for a in packages if not a.startswith('.')]

    packages = ' '.join(packages)

    dockerfile_content = dedent('''
    FROM remrun_django_base

    RUN pip3 install {packages}
    '''.format(**locals()))

    open('docker/django/Dockerfile', 'w').write(dockerfile_content)

    print(dockerfile_content)


def _push(registry, name):
    name = 'remrun_{}'.format(name)
    local('docker tag -f {name} {registry}/{name}'.format(**locals()))
    local('docker push {registry}/{name}'.format(**locals()))


@task
def push(registry, name=None):
    if not name:
        for name in yaml.load(open('docker-compose.yml')).keys():
            if name == 'django_base':
                continue
            _push(registry, name)
    else:
        _push(registry, name)
