#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-C51',
    description='Pygments lexer for KeilC51',
    long_description=open('README.md').read(),
    keywords='pygments molecular-dynamics C51  lexer',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.lexers]
                    C51=pygments_C51:C51Lexer''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
