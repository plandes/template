## todo: need to iterate over dots to expand `packages`--only two levels supported
#set($packages = $namespace.substring(0, $namespace.indexOf(".")))
from setuptools import setup, find_packages

setup(
    name = "${namespace}",
    packages = ['${packages}', '${namespace}'],
    version = '0.1',
    description = '${project-description}',
    author = '${user-name}',
    author_email = '${user-email}',
    url = 'https://github.com/${user}/${project}',
    download_url = 'https://github.com/${user}/${project}/releases/download/v0.0.1/${namespace}-0.1-py3-none-any.whl',
    keywords = ['tooling'],
    classifiers = [],
    entry_points={
        'console_scripts': [
            '${project}=${namespace}.cli:main'
        ]
    }
)
