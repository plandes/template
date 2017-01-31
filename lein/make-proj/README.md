# ${project-name}

${project-description}


#[[## Obtaining]]#

In your `project.clj` file, add:

[![Clojars Project](https://clojars.org/${group}/${artifact}/latest-version.svg)](https://clojars.org/${group}/${artifact}/)

#[[### Binaries]]#

The latest release binaries are
available [here](https://github.com/plandes/${project}/releases/latest).


#[[## Documentation]]#

API [documentation](https://${user}.github.io/${project}/codox/index.html).


#[[## Building]]#

To build from source, do the folling:

- Install [Leiningen](http://leiningen.org) (this is just a script)
- Install [GNU make](https://www.gnu.org/software/make/)
- Install [Git](https://git-scm.com)
- Download the source: `git clone https://github.com/${project} && cd ${project}`
- Download the make include files:
```bash
mkdir ../clj-zenbuild && wget -O - https://api.github.com/repos/plandes/clj-zenbuild/tarball | tar zxfv - -C ../clj-zenbuild --strip-components 1
```
- Build the distribution binaries: `make dist`

Note that you can also build a single jar file with all the dependencies with: `make uber`


#[[## License]]#

Copyright © 2017 Paul Landes

Apache License version 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
