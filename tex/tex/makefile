# Latex document creation make file
# Created: 01/27/2011

## location of the the tex setup (i.e. make file libs, sty files etc) library directory
TEXLIBDIR=	../res

## per make file vars
TEX=		Design

## uncomment to produce a copy of the PDF at path
#FINAL_PDF_NAME=	../$(TEX).pdf

## default position of Preview.app after PDF creation
#PREV_POS ?=	{1100, 0}
#PREV_SIZE ?=	{1100, 1600}

## uncomment to get latex feedback, otherwise compiles faster (Emacs
## fontification latency)
#QUIET=


#all:		$(TEX).dvi
all:		showpdf

#include $(TEXLIBDIR)/lib/make-slides.mk
#include $(TEXLIBDIR)/lib/make-bib.mk
#include $(TEXLIBDIR)/lib/make-idx.mk
include $(TEXLIBDIR)/lib/make-cmd.mk
