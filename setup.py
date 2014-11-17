import sys

from distutils.core import setup


setup(
    name='linkodeit',
    version='0.3',
    description='Command-line utility to publish pastes at http://linkode.org',
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    url='https://github.com/humitos/linkodeit',
    download_url='https://github.com/humitos/linkodeit/tarball/0.3',
    keywords=['linkode', 'pastebin', 'paste'],
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
