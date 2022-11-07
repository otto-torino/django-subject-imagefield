import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-subject-imagefield',
    version='0.2.7',
    packages=['subject_imagefield'],
    include_package_data=True,
    license='MIT License',
    description='A model ImageField with subject position support',
    long_description=README,
    long_description_content_type='text/markdown',
    url='http://github.com/otto-torino/django-subject-imagefield',
    author='abidibo',
    author_email='abidibo@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ]
)
