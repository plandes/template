## todo: need to iterate over dots to expand `packages`--only two levels supported
#set($packages = $namespace.substring(0, $namespace.indexOf(".")))
import os
from os import path
from setuptools import setup

README_FILE = 'README.md'
REQUIREMENTS_FILE = 'requirements.txt'


def get_packages(dnames):
    dirs = []
    for dname in dnames:
        for root, subdirs, files in os.walk(dname):
            root = path.relpath(root, dname)
            if root != '.':
                dirs.append(path.join(dname, root.replace(os.sep, '.')))
    return dirs


def get_curpath():
    return path.abspath(path.join(path.dirname(__file__)))


def get_root_dir():
    nname, dname = None, get_curpath()
    while nname != dname:
        nname, dname = dname, path.abspath(path.join(dname, path.pardir))
        if path.exists(path.join(dname, README_FILE)):
            break
    return dname


def get_long_description():
    dname = get_root_dir()
    with open(path.join(dname, README_FILE), encoding='utf-8') as f:
        return f.read()


def get_requires():
    req_file = path.join(path.dirname(__file__), REQUIREMENTS_FILE)
    with open(req_file, encoding='utf-8') as f:
        return [x.strip() for x in f.readlines()]


setup(
    name="${namespace}",
    packages=get_packages(['${packages}', '${namespace}']),
    # package_data={'': ['*.html', '*.js', '*.css', '*.map', '*.svg']},
    version='0.0.1',
    description='${project-description}',
    author='${user-name}',
    author_email='${user-email}',
    url='https://github.com/${user}/${project}',
    download_url='https://github.com/${user}/${project}/releases/download/v0.0.1/${namespace}-0.0.1-py3-none-any.whl',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    install_requires=get_requires(),
    keywords=['tooling'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            '${project}=${namespace}.cli:main'
        ]
    }
)
