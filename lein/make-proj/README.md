#set($dateYear= $dateTool.get('yyyy'))
# ${project-name}

${project-description}


#[[## Obtaining]]#

In your `project.clj` file, add:

[![Clojars Project](https://clojars.org/${group}/${artifact}/latest-version.svg)](https://clojars.org/${group}/${artifact}/)


#[[### Binaries]]#

The latest release binaries are
available [here](https://github.com/${user}/${project}/releases/latest).


#[[## Documentation]]#

API [documentation](https://${user}.github.io/${project}/codox/index.html).


#[[## Building]]#

To build from source, do the folling:

- Install [Leiningen](http://leiningen.org) (this is just a script)
- Install [GNU make](https://www.gnu.org/software/make/)
- Install [Git](https://git-scm.com)
- Download the source: `git clone --recurse-submodules https://github.com/${user}/${project} && cd ${project}`
- Build the software: `make jar`
- Build the distribution binaries: `make dist`

Note that you can also build a single jar file with all the dependencies with: `make uber`


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
