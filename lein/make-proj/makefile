#[[## makefile automates the build and deployment for lein projects]]#

# type of project
PROJ_TYPE=		clojure
# make modules to add functionality to a build
#PROJ_MODULES=		appassem release model docker python

# edit these if you want
#GITUSER=		johndoe
#APP_NAME=		${artifact}
#APP_SCR_NAME=		${package}.core
#PROJ=		
#REMOTE=		origin
#DIST_PREFIX=		$(HOME)/Desktop

# where the stanford model files are located
#ZMODEL=		$(HOME)/opt/nlp/model

# additional resources generated by the build that should be cleaned up
# (example: clean the generated app assembly file)
#ADD_CLEAN+=		$(ASBIN_DIR)

# make build dependencies
_ :=	$(shell [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )

include ./zenbuild/main.mk

.PHONY: test
test:
	$(LEIN) test
