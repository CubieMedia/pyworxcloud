# -*- coding: utf-8 -*-

from pyworxcloud import __version__
import setuptools

requirements = ['paho-mqtt==1.3.1',
                'pyOpenSSL==17.5.0',
                'async_timeout=3.0.1']

setuptools.setup(
    name = 'pyworxcloud',
    version = __version__,
    description = 'Worx Landroid API library',
    author = 'Morten Trab',
    author_email = 'morten@trab.dk',
    license= 'MIT',
    url = 'https://github.com/mtrab/pyworxcloud',
    packages=setuptools.find_packages(),
    install_requires=requirements,
)