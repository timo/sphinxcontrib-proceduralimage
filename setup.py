# -*- coding: utf-8 -*-

from setuptools import setup

with open("README") as readme:
    long_description = readme

requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-proceduralimage',
    version='0.1',
    license='BSD',
    author='Timo Paulssen',
    author_email='timonator@perpetuum-immobile.de',
    description='proceduralimage Sphinx extension',
    long_description=long_description,
    url="https://github.com/timo/sphinxcontrib-proceduralimage",
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=["sphinxcontrib"],
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
