#!/usr/bin/env python3

"""Setup module."""
from setuptools import setup, find_packages
import os


def read(fname):
    """Read and return the contents of a file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='BallerCFG',
    version='1.0.1',
    description='BallerCFG - a totally baller configuration loader',
    long_description=read('README.md'),
    author='Kalman Olah',
    author_email='hello@kalmanolah.net',
    url='https://github.com/kalmanolah/ballercfg',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyYAML',
    ],
)
