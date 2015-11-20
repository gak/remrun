from setuptools import setup

from web.version import version

setup(
    name='runrem',
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
            'runrem-runner = web.entry_points:runner',
            'runrem-api = web.entry_points:api',
        ],
    },
)
