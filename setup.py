#!/usr/bin/env python

import codecs
import glob
import os
import re

from setuptools import setup, find_packages


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'rb', 'utf-8') as f:
        return f.read()


def find_version(*file_paths):
    """
    Build a path from *file_paths* and search for a ``__version__``
    string inside.
    """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

print('==================================')
print(find_packages(exclude=['tests*']))
print('==================================')

setup(
    name='cameralogger',
    version=find_version('cameralogger/__init__.py'),
    description='Tools to record and decorate camera images for timelapses etc.',
    long_description=(read('README.rst') + '\n\n' +
                      read('AUTHORS.rst')),
    url='https://github.com/stevemarple/python-cameralogger',
    license='GPLv3+',
    author='Steve Marple',
    author_email='s.marple@lancaster.ac.uk',
    packages=find_packages(exclude=['tests*']),
    install_requires=['astral', 'atomiccreate', 'aurorawatchuk',
                      'numpy>=1.7', 'Pillow'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    scripts=glob.glob('cameralogger/bin/*.py'),
)

