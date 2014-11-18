#!/usr/bin/env python3
import imp
from distutils.core import setup

# http://stackoverflow.com/q/2601047/2187091
linkodeit = imp.load_source(name='linkodeit', pathname='linkodeit/linkodeit')

version = linkodeit.__VERSION__

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (ImportError, RuntimeError):
    long_description = ''

setup(
    name='linkodeit',
    version=version,
    description='Command-line utility to publish pastes at http://linkode.org',
    long_description=long_description,
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    url='https://github.com/humitos/linkodeit',
    download_url='https://github.com/humitos/linkodeit/tarball/{}'.format(version),
    keywords=['linkode', 'pastebin', 'paste', 'share', 'code', 'programming', 'utils'],
    scripts=['linkodeit/linkodeit'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
)
