import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'thaistock',
  packages = ['thaistock'], 
  version = '0.0.2',
  license='MIT', 
  description = 'Thai stock data in The Stock Exchange of Thailand (SET) by Uncle Engineer',
  long_description=DESCRIPTION,
  author = 'Uncle Engineer',                 
  author_email = 'loong.wissawakorn@gmail.com',     
  url = 'https://github.com/UncleEngineer/ThaiStock',  
  download_url = 'https://github.com/UncleEngineer/ThaiStock/archive/refs/heads/main.zip',  
  keywords = ['Thai Stock', 'SET', 'Stock Exchange of Thailand' ,'Uncle Engineer'],
  install_requires=[
          'beautifulsoup4',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Office/Business :: Financial',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)