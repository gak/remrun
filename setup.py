from setuptools import setup

from web.version import version

setup(
    name='remrun',
    version=version,
    author='Gerald Kaszuba',
    author_email='gak@gak0.com',
    license='Apache 2.0',
    install_requires=[
        a for a in open('requirements.txt')
        if not a.startswith('#') and not a.startswith('-')
    ],
    entry_points={
        'console_scripts': [
            'remrun-runner = web.entry_points:runner',
            'remrun-api = web.entry_points:api',
        ],
    },
)
