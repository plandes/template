#set($pdf-file-name = $description.replace(" ", "_"))
#[[## latex document creation make file]]#
#
#[[## targets (see zenbuild/src/proj/tex.mk):]]#
#   debug: shows all errors and warning for when compilation fails
#   compile: quickly compiles, but doesn't run a second time for references
#   package: creates a complete viewable PDF
#   install: like package but creates a distribution set to the desktop

#[[## project defined (expert use)]]#
# type of project
PROJ_TYPE=		tex
# make modules to add functionality to a build; add tex-index for indexes
PROJ_MODULES=		tex-biber
#PROJ_LOCAL_MODULES=	tex-table tex-graffle tex-bibstract
PROJ_LOCAL_MODULES=	tex-graffle

# per make file vars
TEX=			report
TIPATH +=		$(abspath ../sty)
BIB_FILE =		$(abspath ../sty/${project}.bib)

#[[## user defined]]#
# distribution file name
FINAL_NAME=		${pdf-file-name}_Report
# Preview.app top x, y, width, height
PREV_LOC ?=		0 0 1100 1500

# run three times when running from scratch, otherwise reference links are
# question marks and a manual forced run would otherwise be necessary
SECOND_RUN_INIT=	1

# make build dependencies
_ :=	$(shell cd .. && [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add git@github.com:plandes/zenbuild.git && make gitinit )

include ../zenbuild/main.mk
