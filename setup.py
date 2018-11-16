from __future__ import print_function
import sys, codecs
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]

with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()

setup(name='seglearn',
      version='1.0.2p0',
      description='Machine Learning Time Series',
      author='David Burns',
      packages=find_packages(),
      include_package_data=True,
      install_requires=INSTALL_REQUIRES,
      author_email='david.mo.burns@gmail.com',
      url = 'https://github.com/dmbee/seglearn',
      download_url = 'https://github.com/dmbee/seglearn',
      long_description=LONG_DESCRIPTION,
      classifiers = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.5']
      )
