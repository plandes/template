#set($pdf-file-name = $description.replace(" ", "_"))
# latex document creation make file

# type of project
PROJ_TYPE=	tex
# make modules to add functionality to a build
PROJ_MODULES=	tex-bib

# per make file vars
TEX=		paper
TIPATH +=	$(abspath ../sty) $(abspath ./sty)
BIB_FILE =	$(abspath ../sty/${project}.bib)
FINAL_PDF_NAME=	$(HOME)/Desktop/${pdf-file-name}.pdf

# Preview.app top x, y, width, height
PREV_LOC ?=	0 0 1100 1500

# uncomment to quiet the compilation
QUIET=

# make build dependencies
_ :=	$(shell cd .. && [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )

include ../zenbuild/main.mk
