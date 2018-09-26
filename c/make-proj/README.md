#set($dateYear= $dateTool.get('yyyy'))
# ${project-name}

[![Travis CI Build Status][travis-badge]][travis-link]

${project-description}


#[[## Obtaining]]#

The latest release binaries are
available [here](https://github.com/${user}/${project}/releases/latest).


#[[## Building]]#

To build from source, do the folling:

- Install [GNU make](https://www.gnu.org/software/make/)
- Build the software and run: `make run`


#[[## Changelog]]#

An extensive changelog is available [here](CHANGELOG.md).


#[[## License]]#

Copyright (c) ${dateYear} ${user-name}

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<!-- links -->
[travis-link]: https://travis-ci.org/${user}/${project}
[travis-badge]: https://travis-ci.org/${user}/${project}.svg?branch=master
