#set($date= $dateTool.get('yyyy-MM-dd'))
#[[##@meta {desc: 'build and deployment for docker projects']]#, date: '${date}'}


#[[## Build system]]#
#
#
# type of project
PROJ_TYPE=		docker
# make modules to add functionality to a build
#PROJ_MODULES=		


#[[## Project]]#
#
DOCKER_IMG_NAME=	${image-name}
DOCKER_USER=		${user}
#DOCKER_UP_DEPS=		


# make build dependencies (remove after initial build)
_ :=	$(shell [ ! -d .git -a ! -d zenbuild ] && \
	  git init . && \
          git submodule add https://github.com/plandes/zenbuild && \
	  git add -A :/ && \
	  git commit -am 'initial add' && \
	  git tag -am initial v0.0.1 && \
          echo "initialized repo" )


#[[## Includes]]#
#
include ./zenbuild/main.mk
