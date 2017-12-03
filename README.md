# Boilerplate Template Projects

This repo contains many of my own project boilerplate code.  Some of it is
documentation specific and others coding projects.

Most of these are [make project](https://github.com/plandes/clj-mkproj)
templates that macro compile out to a project.


## Usage

The recommended process is:

1. Clone the template (this repo):
   `mkdir template && wget -O - https://api.github.com/repos/plandes/template/tarball | tar zxfv - -C template --strip-components 1`
2. Download the boilerplate project starter:
   `mkdir mkproj && wget -O - https://github.com/plandes/clj-mkproj/releases/download/v0.0.7/mkproj.tar.bz2 | tar jxfv - -C mkproj --strip-components 1`
3. Get build system by cloning or:
   `mkdir zenbuild && wget -O - https://api.github.com/repos/plandes/zenbuild/tarball | tar zxfv - -C zenbuild --strip-components 1`
4. Create (for example) a Clojure boilerplate project (choose from a directory
   in `./template`):
   `/bin/bash ./mkproj/bin/mkproj config -s template/lein`
5. Make changes to the project parameters: `vi mkproj.yml`
6. Build out the project from the template: `/bin/bash ./mkproj/bin/mkproj`
7. Optionally create an initial commit baseline for the project:
   `make -C <project created from mkproj> init`
8. Compile and test the project `make -C <project created from mkproj> test`


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
  

## License
Copyright © 2016 - 2017 Paul Landes

GNU Lesser General Public License, Version 2.0
