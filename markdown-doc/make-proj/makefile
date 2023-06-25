#[[## makefile creates html and pdf files from a markdown file]]#
#

## Build config
#
# type of project
PROJ_TYPE =		markdown
# add targets
PROJ_MODULES=		git
# name of the source file without the (assumed) `.md` extension
MD_SRC_NAME =		${project}


#[[## Build submodule]]#
#
_ :=	$(shell [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )


include ./zenbuild/main.mk
