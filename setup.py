
# Thanks: http://pythonhosted.org/an_example_pypi_project/setuptools.html

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nb_examine",
    version = "0.1.0",
    author = "Ian Stokes-Rees",
    author_email = "ijstokes@continuum.io",
    description = ("Python data structure browser for Jupyter"),
    license = "BSD",
    keywords = "data jupyter widget",
    url = "https://github.com/ijstokes/nb_examine",
    packages=['nb_examine'],
    package_data={'nb_examine': ['*.js']},
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
)
