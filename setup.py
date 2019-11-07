from distutils.core import setup
setup(
  name = 'python_loc_counter',
  packages = ['python_loc_counter'],
  version = '0.1',
  license='MIT', 
  description = 'Get LOC metrics for python scripts',
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