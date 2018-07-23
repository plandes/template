## todo: need to iterate over dots to expand `packages`--only two levels supported
#set($packages = $namespace.substring(0, $namespace.indexOf(".")))
from setuptools import setup
from os import path

nname, dname = None, path.abspath(path.join(path.dirname(__file__)))
while nname != dname:
    nname, dname = dname, path.abspath(path.join(dname, path.pardir))
    if path.exists(path.join(dname, 'README.md')):
        break
with open(path.join(dname, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "${namespace}",
    packages = ['${packages}', '${namespace}'],
    version = '0.0.1',
    description = '${project-description}',
    author = '${user-name}',
    author_email = '${user-email}',
    url = 'https://github.com/${user}/${project}',
    download_url = 'https://github.com/${user}/${project}/releases/download/v0.0.1/${namespace}-0.0.1-py3-none-any.whl',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires=[
        'zensols.actioncli>=0.6',
    ],
    keywords = ['tooling'],
    classifiers = [],
    entry_points={
        'console_scripts': [
            '${project}=${namespace}.cli:main'
        ]
    }
)
