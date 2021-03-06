#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def calculate_version():
    initpy = open('few/_version.py').read().split('\n')
    version = list(filter(lambda x: '__version__' in x, initpy))[0].split('\'')[1]
    return version

package_version = calculate_version()

setup(
    name='FEW',
    version=package_version,
    author='William La Cava',
    author_email='lacava@upenn.edu',
    packages=find_packages(),
    url='https://github.com/lacava/few',
    download_url='https://github.com/lacava/few/releases/tag/'+package_version,
    license='GNU/GPLv3',
    entry_points={'console_scripts': ['few=few:main', ]},
    test_suite='nose.collector',
    tests_require=['nose'],
    description=('Feature Engineering Wrapper'),
    long_description='''
A feature engineering wrapper for scikitlearn based on genetic programming.

Contact:
===
e-mail: lacava@upenn.edu

This project is hosted at https://github.com/lacava/few
''',
    zip_safe=True,
    install_requires=['numpy', 'scipy', 'pandas', 'scikit-learn', 'update_checker', 'tqdm', 'joblib','DistanceClassifier'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    keywords=['data science', 'machine learning', 'classification'],
)
