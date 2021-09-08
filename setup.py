import setuptools
import os

from __version__ import __version__

NAME = 'tournesol-twitter-bot'
EXCLUDE_DIRS = []
VERSION = __version__
AUTHOR = 'Aidan Jungo'
EMAIL = 'tournesol.app@gmail.com'
DESCRIPTION = 'TournesolBot scripts'
URL = 'https://github.com/tournesol-app/tournesol-twitter-bot'
REQUIRES_PYTHON = '>=3.6.0'
REQUIRED = ['pandas','tweepy']
README = 'README.md'
PACKAGE_DIR = '.'
LICENSE = 'LICENSE'


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, README), "r") as fp:
    long_description = fp.read()

# with open(LICENSE) as f:
#     license = f.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    url=URL,
    include_package_data=True,
    package_dir={'': PACKAGE_DIR},
    license=license,
    packages=setuptools.find_packages(exclude=EXCLUDE_DIRS),
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    # See: https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Research",
        "Topic :: Scientific/Data",
    ],
    entry_points={
        "console_scripts": [
            "tournesolbot = tournesolbot.__main__:main"
        ]
    }
)
