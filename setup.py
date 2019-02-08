#!/usr/bin/env python
from setuptools import setup

entry_points = {
    'console_scripts': ['nato=nato:main'],
}

setup(name='nato',
      version='1.0.0',
      description="""Are completely arbitrary words better than 1 letter variables?  Let's find out together!""",
      long_description=open("README.rst", "r").read(),
      author='Mike Steder',
      author_email='steder@gmail.com',
      url='http://github.com/steder/nato',
      packages=['nato'],
      install_requires=["astor"],
      entry_points=entry_points,
      license="MIT",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          ]
)
