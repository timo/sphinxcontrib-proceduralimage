# -*- coding: utf-8 -*-
'''
This package adds the proceduralimage directive to Sphinx.

.. _Sphinx: http://sphinx.pocoo.org/

It allows a python code snippet to be supplied, that generates an image, that
will be included in the documentation.

It adds a single directive, `proceduralimage`. It takes a block of python
code, executes the code and extracts the local variables `image_data` and
`alt`. image_data will be saved to a .png in _images and embedded and
the alt variable will be used as the images alt tag.
'''

from setuptools import setup


requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-proceduralimage',
    version='0.1',
    license='BSD',
    author='Timo Paulssen',
    author_email='timonator@perpetuum-immobile.de',
    description='proceduralimage Sphinx extension',
    long_description=__doc__,
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
