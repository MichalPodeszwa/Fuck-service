from setuptools import setup

setup(name='FuckAsService',
    version='1.0',
    description='Never trouble about flipping someone off!',
    author='Michal Podeszwa',
    author_email='michal.podeszwa@gmail.com',
    install_requires=['Flask',
        'Flask-PyMongo',
        'Jinja2',
        'MarkupSafe',
        'Werkzeug',
        'itsdangerous',
        'pymongo',
        'mimerender',
        'python-mimeparse',
        'wsgiref']
    )
