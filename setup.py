from setuptools import setup, find_packages

setup(name='mnistenv',
  version='0.1.0',
  install_requires = [
    'numpy',
    'gym',
    'keras'
  ],
  packages=find_packages())
