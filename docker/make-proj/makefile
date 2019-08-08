#[[## makefile automates the build and deployment for docker projects]]#

# type of project, currently one of: clojure, python
PROJ_TYPE=		docker
# make modules to add functionality to a build
#PROJ_MODULES=		

DOCKER_IMG_NAME=	${image-name}
DOCKER_USER=		${user}
#DOCKER_UP_DEPS=		

# make build dependencies
_ :=	$(shell [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )

include ./zenbuild/main.mk
