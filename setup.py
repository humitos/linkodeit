import sys

from distutils.core import setup


setup(
    name='linkodeit',
    version='0.2',
    description='Command-line utility to publish pastes at http://linkode.org',
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    url='https://github.com/humitos/linkodeit',
    download_url='https://github.com/humitos/linkodeit/tarball/0.2',
    keywords=['linkode', 'pastebin', 'paste'],
    scripts=['linkodeit/linkodeit'],
    install_requires=['six'],
    classifiers=[],
)
