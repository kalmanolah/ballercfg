#!/usr/bin/env python3

"""Setup module."""
from setuptools import setup, find_packages
import os


def read(fname):
    """Read and return the contents of a file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='BallerCFG',
    version='1.0.2',
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
    entry_points={
        'ballercfg.extension_loaders': [
            'yaml = ballercfg.yaml_configuration_file:YamlConfigurationFile',
            'yml = ballercfg.yaml_configuration_file:YamlConfigurationFile',
            'json = ballercfg.json_configuration_file:JsonConfigurationFile',
            'ini = ballercfg.ini_configuration_file:IniConfigurationFile',
            'cfg = ballercfg.yaml_configuration_file:IniConfigurationFile',
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyYAML',
    ],
)
