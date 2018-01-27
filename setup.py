import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pygments-yang-lexer',
    version='0.2',
    description=('A Pygments lexer for YANG modules'),
    long_description=read('README.md'),
    packages=['yanglexer'],
    author='Carl Moberg',
    author_email='camoberg@cisco.com',
    license='New-style BSD',
    url='https://github.com/cmoberg/pygments-yang-lexer',
    install_requires=['Pygments'],
    include_package_data=True,
    keywords=['yang', 'pygments', 'lexer'],
    classifiers=[],
    entry_points={'pygments.lexers': 'yanglexer=yanglexer.yanglexer:YangLexer'}
)