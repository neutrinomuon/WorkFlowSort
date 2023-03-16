from numpy.distutils.core import Extension
from numpy.distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup( name='WorkFlowSort',
       version='0.0.1',
       description='Show Work Flows of repos sorted by name, by starting date or final date',
       long_description=long_description,      # Long description read from the the readme file
       long_description_content_type="text/markdown",
       author='Jean Gomes',
       author_email='antineutrinomuon@gmail.com',
       url='https://github.com/neutrinomuon/IntegralALL',
       install_requires=[ 'numpy','matplotlib' ],
       classifiers=[
           "Programming Language :: Python :: 3",
                   ],
       data_files=[('', ['version.txt'])],
      )
    
