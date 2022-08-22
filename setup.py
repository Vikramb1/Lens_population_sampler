#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Vikram Bhamre",
    author_email='bhamrev@stpaulsschool.org.uk',
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
    description="Python package to sample from a velocity dispersion function of ellictical galaxies in the local universe",
    entry_points={
        'console_scripts': [
            'vdf_sampler=vdf_sampler.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='vdf_sampler',
    name='vdf_sampler',
    packages=find_packages(include=['vdf_sampler', 'vdf_sampler.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/vikramb1/lens_population_sampler',
    version='0.1.0',
    zip_safe=False,
)
