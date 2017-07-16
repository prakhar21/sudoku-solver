from distutils.core import setup

setup(
  name = 'sudokubot',
  packages = ['sudokubot'],
  version = '0.1',
  description = 'A simple library that solves any sudoku in the world. It is written in pure Python and holds no dependencies.',
  author = 'Prakhar Mishra',
  author_email = 'pmprakhargenius@gmail.com',
  url = 'https://github.com/prakhar21/sudoku-solver',
  download_url = 'https://github.com/prakhar21/sudoku-solver/archive/0.1.tar.gz',
  keywords = ['sudoku', 'artificial intelligence', 'game playing agent'], 
  classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
  entry_points={
        'console_scripts': [
            'sudoku = sudokubot.solver:solve'
     ]},
)
