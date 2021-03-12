#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    with open('README.md', encoding='utf-8') as readme_file:
        readme = readme_file.read()
except IOError:
    readme = ''

try:
    with open('HISTORY.md', encoding='utf-8') as history_file:
        history = history_file.read()
except IOError:
    history = ''


install_requires = [
    'baytune>=0.2.3,<0.3',
    'mlblocks>=0.4.0,<0.5',
    'mlprimitives>=0.3.0,<0.4',
    'mongoengine>=0.16.3,<0.17',
    'pymongo>=3.7.2,<4',
    'tabulate>=0.8.3,<0.9',
    'numba>=0.48,<0.52',
    'pyts>=0.9,<0.11',
    'azure-cognitiveservices-anomalydetector>=0.3,<0.4',
    # tensorflow installation
    # 'tensorflow>=2.3,<2.4',
    # 'tensorflow-gpu>=2.3,<2.4'
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

tests_require = [
    'pytest>=3.4.2',
    'pytest-cov>=2.6.0',
    'rundoc>=0.4.3,<0.5',
]

development_requires = [
    # general
    'pip>=9.0.1',
    'bumpversion>=0.5.3,<0.6',
    'watchdog>=0.8.3,<0.11',

    # docs
    'm2r2>=0.2.5,<0.3',
    'nbsphinx>=0.5.0,<0.7',
    'Sphinx>=3,<3.3',
    'pydata-sphinx-theme',
    'autodocsumm>=0.1.10,<1',
    'ipython>=6.5,<7.5',

    # style check
    'flake8>=3.7.7,<4',
    'isort>=4.3.4,<5',

    # fix style issues
    'autoflake>=1.2,<2',
    'autopep8>=1.4.3,<2',

    # distribute on PyPI
    'twine>=1.10.0,<4',
    'wheel>=0.30.0',

    # Advanced testing
    'coverage>=4.5.1,<6',
    'tox>=2.9.1,<4',

    # Documentation style
    'pydocstyle==3.0.0,<4',
]

setup(
    author="MIT Data To AI Lab",
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Orion is a machine learning library built for data generated by satellites.",
    entry_points={
        'console_scripts': [
            'orion=orion.cli:main'
        ],
        'mlblocks': [
            'primitives=orion:MLBLOCKS_PRIMITIVES',
            'pipelines=orion:MLBLOCKS_PIPELINES'
        ],
    },
    extras_require={
        'test': tests_require,
        'dev': development_requires + tests_require,
    },
    include_package_data=True,
    install_requires=install_requires,
    keywords='orion',
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='orion-ml',
    packages=find_packages(include=['orion', 'orion.*']),
    python_requires='>=3.6,<3.8',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/D3-AI/Orion',
    version='0.1.7.dev0',
    zip_safe=False,
)
