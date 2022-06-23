#set($dateYear= $dateTool.get('yyyy'))
# ${project-name}

[![PyPI][pypi-badge]][pypi-link]
[![Python 3.9][python39-badge]][python39-link]
[![Build Status][build-badge]][build-link]

${project-description}


#[[## Documentation]]#

See the [full documentation](https://${user}.github.io/${project}/index.html).
The [API reference](https://${user}.github.io/${project}/api.html) is also
available.


#[[## Obtaining]]#

The easiest way to install the command line program is via the `pip` installer:
```bash
pip3 install ${namespace}
```

Binaries are also available on [pypi].


#[[## Changelog]]#

An extensive changelog is available [here](CHANGELOG.md).


#[[## License]]#

[MIT License](LICENSE.md)

Copyright (c) ${dateYear} ${user-name}


<!-- links -->
[pypi]: https://pypi.org/project/${namespace}/
[pypi-link]: https://pypi.python.org/pypi/${namespace}
[pypi-badge]: https://img.shields.io/pypi/v/${namespace}.svg
[python39-badge]: https://img.shields.io/badge/python-3.9-blue.svg
[python39-link]: https://www.python.org/downloads/release/python-390
[build-badge]: https://github.com/${user}/${project}/workflows/CI/badge.svg
[build-link]: https://github.com/${user}/${project}/actions
