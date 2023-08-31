#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Tahar Allouche",
    author_email='tahartaharallouche@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Scraps sports betting sites to look for arbitrage opportunities across different platforms",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bet_arbitrage',
    name='bet_arbitrage',
    packages=find_packages(include=['bet_arbitrage', 'bet_arbitrage.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/taharallouche/bet_arbitrage',
    version='0.1.0',
    zip_safe=False,
)
