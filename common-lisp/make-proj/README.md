#set($dateYear= $dateTool.get('yyyy'))
# ${project-name}

[![Build Status][build-badge]][build-link]

${project-description}


#[[## Obtaining]]#

The easiest way to install is using [quicklisp]:
```lisp
(ql:quickload :${project})
```

#[[## Changelog]]#

An extensive changelog is available [here](CHANGELOG.md).


#[[## License]]#

[MIT License](LICENSE.md)

Copyright (c) ${dateYear} ${user-name}


<!-- links -->

[quicklisp]: https://www.quicklisp.org/beta/
[MIT License]: https://opensource.org/licenses/MIT
[build-badge]: https://github.com/${user}/${project}/workflows/CI/badge.svg
[build-link]: https://github.com/${user}/${project}/actions
