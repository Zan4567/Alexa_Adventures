"""This file contains setup information for multiple data-structures."""

from setuptools import setup

setup(
    name='Alexa Adventures',
    description='Contains setup for Alexa Adventures app.',
    author='Chelsea and Carson',
    author_email='carson.newton@outlook.com, brendanmd@gmail.com, allan.liebold@gmail.com',
    package_dir={'': 'src'},
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox']}
)
