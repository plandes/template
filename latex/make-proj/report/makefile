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
#FINAL_PDF_NAME=	$(HOME)/Desktop/${pdf-file-name}_Report.pdf

# uncomment to skip a second compilation (for references)
#SECOND_RUN=1

# uncomment to quiet the compilation
QUIET=

#PREV_POS ?=	{1100, 0}
#PREV_SIZE ?=	{1100, 1600}
#PREV_POS ?=	{650, 0}
#PREV_SIZE ?=	{900, 900}

# make build dependencies
_ :=	$(shell cd .. && [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )

include ../zenbuild/main.mk
