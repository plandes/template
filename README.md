# Boilerplate Template Projects

This repo contains many of my own project boilerplate code.  Some of it is
documentation specific and others coding projects.

Most of these are [mkproj] templates that macro compile out to a project.


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
## Table of Contents

- [Templates](#templates)
- [Usage](#usage)
- [License](#license)

<!-- markdown-toc end -->


## Templates

* **[Lein project](https://github.com/plandes/template/tree/master/lein)**:
  boilerplate for [Leiningen](http://leiningen.org).
* **[Scala project](https://github.com/plandes/template/tree/master/sbt)**:
  Boilerplate [simple built tool (SBT)](http://www.scala-sbt.org) project to
  build Scala projects with Ensime ane Emacs.
* **[LaTeX environment](https://github.com/plandes/template/tree/master/tex)**:
  boilerplate setup
  for [Latex](https://github.com/plandes/template/tree/master/tex) documents,
  which include:
  * Design/architecture documentation--includes handy bib setup
  * Academic papers
  * Academic slides
* **[Emacs Lisp Package](https://github.com/plandes/template/tree/master/elisp)**:
  boilerplate for [Emacs](https://www.gnu.org/software/emacs/) Lisp and
  includes support for:
  * [Travis Continuous Integration](https://travis-ci.org)
  * [Cask Builds](https://cask.github.io)


## Usage

I'll provide an example via a use case with a Clojure project.  First you'll
need to install the [dependencies].

The recommended process is (see [script version]):

1. Clone the template (this repo):
```bash
mkdir template && \
  wget -O - https://api.github.com/repos/plandes/template/tarball | \
  tar zxfv - -C template --strip-components 1
```
2. Download the [mkproj] boilerplate project starter:
```bash
mkdir mkproj && \
  wget -O - https://github.com/plandes/clj-mkproj/releases/download/v0.0.7/mkproj.tar.bz2 | \
  tar jxfv - -C mkproj --strip-components 1
```
3. Get [zenbuild] system by cloning or:
```bash
mkdir zenbuild && \
  wget -O - https://api.github.com/repos/plandes/zenbuild/tarball | \
  tar zxfv - -C zenbuild --strip-components 1
```
4. Create (for example) a Clojure boilerplate project or choose from a directory
   in `./template` (note that not all are [mkproj] projects):
```bash
/bin/bash ./mkproj/bin/mkproj config -s template/lein
```
5. Optionally make changes to the project parameters `mkproj.yml` file (for
   any serious work you'll have to edit this file):
```bash
vi mkproj.yml
```
6. Build out the project from the template:
```bash
/bin/bash ./mkproj/bin/mkproj
```
7. Create an initial commit baseline for the project and create an uberjar:
```bash
make -C clj-someproj init uber
```

8. Run the executable jar from the command line:
```bash
java -jar clj-someproj/target/someproj-0.0.1-standalone.jar 
```

 

## License
Copyright © 2016 - 2017 Paul Landes

GNU Lesser General Public License, Version 2.0


<!-- links -->
[zenbuild]: https://github.com/plandes/zenbuild
[mkproj]: https://github.com/plandes/clj-mkproj
[dependencies]: https://github.com/plandes/zenbuild#building-and-dependencies
[script version]: doc/example/fastclj.sh
