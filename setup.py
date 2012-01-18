from setuptools import setup, find_packages
import os, sys, re


# Load the version by reading prep.py, so we don't run into
# dependency loops by importing it into setup.py
version = None
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "gmtasks", "__init__.py")) as file:
    for line in file:
        m = re.search(r'__version__\s*=\s*(.+?\n)', line)
        if m:
            version = eval(m.group(1))
            break

setup_args = dict(
    name             = 'gmtasks',
    version          = version,
    author           = 'Chris Petersen',
    author_email     = 'geek@ex-nerd.com',
    url              = 'https://github.com/ex-nerd/gmtasks',
    license          = 'Modified BSD',
    description      = 'Gearman Task Server',
    long_description = open('README.rst').read(),
    install_requires = ['gearman'],
    packages         = find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)

if __name__ == '__main__':
    setup(**setup_args)
