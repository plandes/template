#set($pdf-file-name = $description.replace(" ", "_"))
# latex document creation make file

## project defined (expert use)
# type of project
PROJ_TYPE=	tex
# make modules to add functionality to a build
PROJ_MODULES=	tex-bib

# per make file vars
TEX=		paper
TIPATH +=	$(abspath ../sty) $(abspath ./sty)
BIB_FILE =	$(abspath ../sty/${project}.bib)

## user defined
# distribution file name (no extension, post pended by `slides', `report' etc)
FINAL_NAME=	${pdf-file-name}_Paper
# Preview.app top x, y, width, height
PREV_LOC ?=	0 0 1100 1500
# control verbosity
# TEX_QUIET=0

# make build dependencies
_ :=	$(shell cd .. && [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )

include ../zenbuild/main.mk
