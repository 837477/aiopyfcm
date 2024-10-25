"""
aiopyfcm
"""
from setuptools import setup
from aiopyfcm import (
    __TITLE__, __SUMMARY__, __URL__, __VERSION__, __AUTHOR__, __EMAIL__, __LICENSE__
)

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=__TITLE__,
    version=__VERSION__,
    description=__SUMMARY__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=__URL__,
    author=__AUTHOR__,
    author_email=__EMAIL__,
    license=__LICENSE__,
    packages=['aiopyfcm'],
    keywords=__SUMMARY__,
    install_requires=['requests', 'aiohttp', 'google-auth'],
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
