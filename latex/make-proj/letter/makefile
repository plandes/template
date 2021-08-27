#set($pdf-file-name = $description.replace(" ", "_"))
# latex document creation make file

# type of project
PROJ_TYPE=	tex

# per make file vars
TEX=		letter
FINAL_PDF_NAME=	$(HOME)/Desktop/${pdf-file-name}_Letter.pdf

# Preview.app top x, y, width, height
PREV_LOC ?=	0 0 1100 1500

# uncomment to quiet the compilation
# TEX_QUIET=0

# make build dependencies
_ :=	$(shell cd .. && [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add git@github.com:plandes/zenbuild.git && make gitinit )

include ../zenbuild/main.mk
