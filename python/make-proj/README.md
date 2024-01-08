#set($dateYear= $dateTool.get('yyyy'))
# ${project-name}

[![PyPI][pypi-badge]][pypi-link]
[![Python 3.10][python3100-badge]][python3100-link]
[![Python 3.11][python311-badge]][python311-link]
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


#[[## Community]]#

Please star this repository and let me know how and where you use this API.
Contributions as pull requests, feedback and any input is welcome.


#[[## License]]#

[MIT License](LICENSE.md)

Copyright (c) ${dateYear} ${user-name}


<!-- links -->
[pypi]: https://pypi.org/project/${namespace}/
[pypi-link]: https://pypi.python.org/pypi/${namespace}
[pypi-badge]: https://img.shields.io/pypi/v/${namespace}.svg
[python3100-badge]: https://img.shields.io/badge/python-3.10-blue.svg
[python3100-link]: https://www.python.org/downloads/release/python-3100
[python311-badge]: https://img.shields.io/badge/python-3.11-blue.svg
[python311-link]: https://www.python.org/downloads/release/python-3110
[build-badge]: https://github.com/${user}/${project}/workflows/CI/badge.svg
[build-link]: https://github.com/${user}/${project}/actions
