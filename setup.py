import os, sys, codecs

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = codecs.open(os.path.join(here, 'README.txt'), encoding='utf8').read()
CHANGES = codecs.open(os.path.join(here, 'CHANGES.txt'), encoding='utf8').read()

setup(name='pep425tags',
      version='0.0.0',
      description='Reference implementation of PEP 425 compatibility tags.',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        ],
      author='Daniel Holth',
      author_email='dholth@fastmail.fm',
      url='http://bitbucket.org/dholth/pep425/',
      keywords='packaging',
      license='MIT',
      py_modules=['pep425tags'],
      include_package_data=True,
      zip_safe=False,
      )

