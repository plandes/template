#[[## makefile automates the build and deployment for docker projects]]#

# type of project, currently one of: clojure, python
PROJ_TYPE=		docker
# make modules to add functionality to a build
#PROJ_MODULES=		

DOCKER_IMG_NAME=	${image-name}
DOCKER_USER=		${user}
#DOCKER_UP_DEPS=		

# make build dependencies (remove after initial build)
_ :=	$(shell [ ! -d .git -a ! -d zenbuild ] && \
	  git init . && \
          git submodule add git@github.com:plandes/zenbuild.git && \
	  git add -A :/ && \
	  git commit -am 'initial add' && \
	  git tag -am initial v0.0.1 && \
          echo "initialized repo" )

include ./zenbuild/main.mk
