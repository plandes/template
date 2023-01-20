#[[## makefile generates documents and deploys to github]]#
#
# files in this directory can be moved to a subdirectory

## project make setup
#
PROJ_TYPE=		default
PROJ_MODULES=		git git-doc

## project
#
# directory that has the documentation
DOC_DIR =		doc

## git variables
#
# the name of this repo and user name of the repo owner
GIT_PROJ =		${project}
GIT_USER =		${user}


# make build dependencies (remove after initial build)
_ :=	$(shell [ ! -d .git -a ! -d zenbuild ] && \
	  git init . && \
          git submodule add https://github.com/plandes/zenbuild && \
	  git add -A :/ && \
	  git commit -am 'initial add' && \
	  git tag -am initial v0.0.1 && \
          echo "initialized repo" )


include ./zenbuild/main.mk


$(GIT_DOC_SRC_DIR):
			mkdir -p $(GIT_DOC_SRC_DIR)
			cp -r doc/* $(GIT_DOC_SRC_DIR)
			touch $(GIT_DOC_SRC_DIR)/.nojekyll


.PHONY:			deploy
deploy:			gitdocdeploy
			@echo "url: https://$(GIT_USER).github.io/$(GIT_PROJ)"
