"""raumd installer."""

from pathlib import Path
from setuptools import setup, find_packages
from main.__init__ import __version__

with open(Path('main') / 'requirements.txt', encoding="utf-8") as f:
    requirements = f.readlines()

LONG_DESCRIPTION = 'Raumdeuter runs your sequence of bash commands defined custom json files. \
    This files can be created on the online platform https://airlocks.xyz.'

setup(
        name ='raumd',
        version =__version__,
        author ='Roman Botnari',
        author_email ='romanbotnari@me.com',
        url ='',
        description ='.',
        long_description = LONG_DESCRIPTION,
        long_description_content_type ="text/markdown",
        license ='Apache License, Version 2.0',
        packages = find_packages(),
        entry_points = {
            'console_scripts': [
                'raumd = main.raumd:main'
            ]
        },
        classifiers =[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        keywords ='',
        install_requires = requirements,
        zip_safe = False,
        package_data={
            "main": ["raumd.conf", "requirements.txt"],
        }
)
