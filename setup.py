from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'python_loc_counter',
  packages = ['python_loc_counter'],
  version = '0.1',
  license='MIT', 
  description = 'Get LOC metrics for python scripts',
  long_description=long_description,
  author = 'Bryce Vonilten',
  author_email = 'ki6bpd@gmail.com',
  url = 'https://github.com/BryceV/python_loc_counter', 
  download_url = 'https://github.com/BryceV/python_loc_counter/archive/v0.1.tar.gz',
  keywords = ['python', 'lines of code', 'loc'],
  install_requires=[ ],
  classifiers=[
    'Development Status :: 3 - Alpha', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
