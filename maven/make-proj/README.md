#set($dateYear= $dateTool.get('yyyy'))
# ${project-name}

${project-description}


#[[## Obtaining]]#

In your `pom.xml` file add
the
[dependency XML element](https://${user}.github.io/${project}/dependency-info.html) below:
```xml
<dependency>
    <groupId>${group}</groupId>
    <artifactId>${artifact}</artifactId>
    <version>${initial-version}</version>
</dependency>
```


#[[## Documentation]]#

More [documentation](https://${user}.github.io/${project}/):
* [Javadoc](https://${user}.github.io/${project}/apidocs/index.html)
* [Dependencies](https://${user}.github.io/${project}/dependencies.html)


#[[## Building]]#

To build from source, do the following:

- Install [Maven](https://maven.apache.org)
- Install [GNU make](https://www.gnu.org/software/make/) (optional)
- Build the software: `make`
- Build the distribution binaries: `make dist`

Note that you can also build a single jar file with all the dependencies with: `make package`


#[[## Changelog]]#

An extensive changelog is available [here](CHANGELOG.md).



#[[## License]]#

Copyright © ${dateYear} Paul Landes

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
