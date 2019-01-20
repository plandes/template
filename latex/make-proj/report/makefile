#set($pdf-file-name = $description.replace(" ", "_"))
# latex document creation make file

# type of project
PROJ_TYPE=	tex
# make modules to add functionality to a build; add tex-index for indexes
PROJ_MODULES=	tex-biber

# per make file vars
TEX=		report
TIPATH +=	$(abspath ../sty)
BIB_FILE =	$(abspath ../sty/${project}.bib)
FINAL_PDF_NAME=	$(HOME)/Desktop/${pdf-file-name}_Report.pdf

# Preview.app top x, y, width, height
PREV_LOC ?=	0 0 1100 1500

# uncomment to quiet the compilation
QUIET=

# make build dependencies
_ :=	$(shell cd .. && [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )

include ../zenbuild/main.mk
