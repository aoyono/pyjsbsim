from setuptools import find_packages
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

version = '0.0.1'

setup(name='PyJSBSim',
      version=version,
      description="A python interface for JSBSim using Cython.",
      long_description="""\
      Interfaces to JSBSim using Cython.
      """,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering',
          'Topic :: Text Processing :: General',
      ],
      # Get strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='James Goppert',
      author_email='james.goppert@gmail.com',
      url='https://github.com/arktools/pyjsbsim',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      install_requires=['cython'],
      ext_modules= cythonize('cython/*.pyx'),
      #cmdclass = {'build_ext': build_ext},
      test_suite="test",
      #package_dir={'pyjsbsim': 'pyjsbsim'},
      #package_data={'pyjsbsim': ['templates/*']},
      #entry_points={
      #  'console_scripts': [
      #      'pydatcom-export = pydatcom:DatcomExporter.command_line',
      #      'pydatcom-plot = pydatcom:DatcomPlotter.command_line'
      #  ]},
      )
