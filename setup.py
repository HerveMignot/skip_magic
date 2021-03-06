from setuptools import setup

LICENSE = 'MIT'
AUTHOR = "HerveMignot"
EMAIL = "HerveMignot@github.com"
URL = "http://github.com/HerveMignot/skip_magic"
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable'
    'Environment :: Console'
    'Framework :: IPython'
    'Framework :: Jupyter'
    'Intended Audience :: Developers'
    'Intended Audience :: Science/Research'
    'License :: OSI Approved :: MIT License'
    'Operating System :: OS Independent'
    'Programming Language :: Python'
    'Programming Language :: Python :: 2'
    'Programming Language :: Python :: 2.7'
    'Programming Language :: Python :: 3.5'
    'Programming Language :: Python :: 3.6'
    'Programming Language :: Python :: 3.7'
    'Topic :: Scientific/Engineering'
]

setup(name='skip_magic',
      version='0.1.0',
      description='Magic command to skip cell execution',
      keywords='cell execution magic command IPython Jupyter Jupyterlab',
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,
      license=LICENSE,
      packages=['skip_magic'],
      classifiers=CLASSIFIERS,
      # install_requires=[
      #     'requests',
      #     ],
      include_package_date=False,
      zip_safe=False
      )
