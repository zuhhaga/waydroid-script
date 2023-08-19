#!/usr/bin/python3
import os
from setuptools import setup, find_packages
from os import environ as env
import subprocess

text=open('waydroid_script/requirements.txt', 'r').readlines()

requirements=[]
for i in text:
    i = i.strip()
    if not (len(i) == 0 or i[0] == '#'):
        requirements.append(i)

try:
    VERSION = open('VERSION').read()
except Exception:
    VERSION = '0.dev'

setup(
    name='waydroid_script',
    version=VERSION,
    description="""Script to add gapps and other stuff to waydroid!""",
    long_description="""Python Script to add OpenGapps,
Magisk, libhoudini translation library
and libndk translation library to waydroid !""",
    author="huakim",
    author_email='zuhhaga@gmail.com',
    url='http://github.com/casualsnek/waydroid-script',
    license='MIT',
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'waydroid-script = main:main',
        ],
    },
    zip_safe=False
) 
