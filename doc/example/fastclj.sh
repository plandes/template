#!/bin/sh

PNAME=$1

echo "usage: $0 [<project name>]"

# Clone the template (this repo):
mkdir template && \
  wget -O - https://api.github.com/repos/plandes/template/tarball | \
  tar zxfv - -C template --strip-components 1

# Download the mkproj boilerplate project starter:
mkdir mkproj && \
  wget -O - https://github.com/plandes/clj-mkproj/releases/download/v0.0.7/mkproj.tar.bz2 | \
  tar jxfv - -C mkproj --strip-components 1

# Get zenbuild system by cloning or:
mkdir zenbuild && \
  wget -O - https://api.github.com/repos/plandes/zenbuild/tarball | \
  tar zxfv - -C zenbuild --strip-components 1

# Create (for example) a Clojure boilerplate project or choose from a directory
# in ./template (note that not all are mkproj projects):
bash ./mkproj/bin/mkproj config -s template/lein

# Optionally make changes to the project parameters mkproj.yml file (for any
# serious work you'll have to edit this file):
#vi mkproj.yml
if [ ! -z "$PNAME" ] ; then
    sed -i "s/someproj/${PNAME}/g" mkproj.yml
fi

# Build out the project from the template:
bash ./mkproj/bin/mkproj

# Create an initial commit baseline for the project and create an uberjar:
make -C clj-someproj init uber

# Run the executable jar from the command line:
java -jar clj-someproj/target/someproj-0.0.1-standalone.jar 
