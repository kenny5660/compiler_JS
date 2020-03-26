from setuptools import setup, find_packages
from os.path import join, dirname
import compiler_js

import rebuild_g4

setup(
    name='compiler_js',
    version=compiler_js.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
            'antlr4-python3-runtime==4.8'
        ],
    entry_points={
        'console_scripts':
            ['compiler_js = compiler_js.console_utility:main']
        }
)