#[[## makefile automates the build and deployment for lein projects]]#

# edit these if you want
#GUSER=		johndoe
#APP_NAME=	${artifact}
#APP_SCR_NAME=	${package}.core
#PROJ=		
#REMOTE=	origin
#DIST_PREFIX=	$(HOME)/Desktop

# location of the http://github.com/plandes/clj-zenbuild cloned directory
ZBHOME ?=	../clj-zenbuild
# type of project, currently one of: clojure, python
PROJ_TYPE=	clojure

# where the stanford model files are located
#ZMODEL=	$(HOME)/opt/nlp/model

# clean the generated app assembly file
#ADD_CLEAN+=	$(ASBIN_DIR)

all:		info

include $(ZBHOME)/src/mk/env.mk
#[[#include $(ZBHOME)/src/mk/model.mk]]#
#[[#include $(ZBHOME)/src/mk/dist.mk]]#
#[[#include $(ZBHOME)/src/mk/release.mk]]#
#[[#include $(ZBHOME)/src/mk/docker.mk]]#

.PHONY: test
test:
	$(LEIN) test
