# Latex document creation make file
# Created: 01/27/2011

## stuff to include in a makefile.in
GRAFFLEBIN=	$(TEXLIBDIR)/bin/exportgraffle.scpt
SDEDITBIN=	$(HOME)/opt/lib/javabin/sdedit-3.1/bin/sdedit
PDFTOPSBIN=	$(HOME)/opt/lib/osx/xpdf-3.02/bin/pdftops

## everything else shouldn't need modifying
# paths
nullstr=
space=		$(nullstr) $(nullstring)
TIPATH +=	. $(TEXLIBDIR)/image $(TEXLIBDIR)/lib
TIPATHSTR=	$(subst $(space),:,$(TIPATH))
# trailing colon needed
TPATH=		TEXINPUTS=$(TIPATHSTR):
LAT ?=		$(TPATH) latex
HTMLDIR=	$(TEX)
GRAFFLEPATH=	$(realpath ../graffle)
DBPATH=		$(realpath ../db)
SEQPATH=	$(realpath ../seq)
VECPATH=	$(realpath ../vec)

# file deps
DBPDFS=		$(notdir $(wildcard $(DBPATH)/*.pdf))
VECEPS=		$(notdir $(wildcard $(VECPATH)/*.eps))
GRAFFLES=	$(wildcard $(GRAFFLEPATH)/*.graffle)
SEQUENCES=	$(notdir $(wildcard $(SEQPATH)/*.sdx))
DIAGRAMS=	$(SEQUENCES:.sdx=.eps) $(DBPDFS:.pdf=.eps) $(VECEPS)

# record keeping
BASEDIR=	$(realpath .)
GRAFFINDF=	grafflecreated
LATDEPS+=	
DISTDIR=	$(TEX)-$(shell date +'%y-%m-%d')
DISTZIP=	$(DISTDIR).zip

OBJS_TO_DEL+=	$(TEX).aux $(TEX).log *~ $(TEX).dvi $(TEX).ps \
			$(TEX).pdf $(TEX).toc $(TEX).equ $(DIAGRAMS) $(HTMLDIR) \
			$(TEX).lot $(TEX).lof $(TEX).lol $(TEX).pdb $(TEX).rtf \
			$(TEX).loa *.eps *.ps $(TEX).out *.bak \
			$(GRAFFINDF) $(DISTDIR) $(DISTZIP)

# compiles faster in Emacs avoiding fontification of verbose output
QUIET ?=	> /dev/null

# default position of Preview.app
PREV_POS ?=	{1500, 0}
PREV_SIZE ?=	{1400, 1600}


%.eps:		$(SEQPATH)/%.sdx
		$(SDEDITBIN) -t eps -o $(CURDIR)/$*.eps $(SEQPATH)/$*.sdx

%.eps:		$(DBPATH)/%.pdf
		$(PDFTOPSBIN) -eps $(DBPATH)/$*.pdf $(CURDIR)/$*.eps

%.eps:		$(VECPATH)/%.eps
		cp $(VECPATH)/$*.eps $(CURDIR)/$*.eps

$(GRAFFINDF):	$(GRAFFLES) $(DIAGRAMS)
		echo $(GRAFFLES)
		touch $(GRAFFINDF)
		for i in $(GRAFFLES) ; do \
			osascript $(GRAFFLEBIN) $$i $(BASEDIR) $(CANVASES) ; \
		done

$(TEX).dvi:	$(TEX).tex $(GRAFFINDF) $(LATDEPS)
		$(LAT) $(TEX).tex $(QUIET)
		@ [ -z "$(NO_SECOND_RUN)" ] && $(LAT) $(TEX).tex $(QUIET)

.PHONY:
force:
		$(LAT) $(TEX).tex $(QUIET)

.PHONY:
ps:		$(TEX).ps

$(TEX).ps:	$(TEX).dvi
		$(TPATH) dvips -o $(TEX).ps $(TEX).dvi

.PHONY:
pdf:		$(TEX).pdf

$(TEX).pdf:	$(TEX).dvi
		$(TPATH) dvipdfm -q -p letter $(TEX).dvi
		@ if [ ! -z "$(FINAL_PDF_NAME)" ] ; then \
			cp $(TEX).pdf "$(FINAL_PDF_NAME)" ; \
		fi

.PHONY:
rtf:		$(TEX).rtf

$(TEX).rtf:	$(TEX).dvi
		$(TPATH) latex2rtf $(TEX).tex

$(HTMLDIR):
		latex2html -local_icons $(TEX).tex

.PHONY:
dist:		$(DISTZIP)

$(DISTDIR):	$(TEX).pdf $(TEX).rtf
		mkdir -p $(DISTDIR)
		cp $(TEX).pdf $(TEX).rtf $(DISTDIR)

$(DISTZIP):	$(DISTDIR) $(TEX).pdf $(TEX).rtf
		zip -r $(DISTZIP) $(DISTDIR)

.PHONY:
html:		$(HTMLDIR)

.PHONY:
show:		$(TEX).dvi
		xdvi -s 6 -gamma 1.5 $(TEX).dvi &

.PHONY:
showpdf:	$(TEX).pdf
		open $(TEX).pdf
		osascript -e 'tell application "System Events" to set position of first window of application process "Preview" to $(PREV_POS)'
		osascript -e 'tell application "System Events" to set size of first window of application process "Preview" to $(PREV_SIZE)'
		osascript -e 'tell application "Emacs" to activate'

.PHONY:
showrtf:	$(TEX).rtf
		open -a Microsoft\ Word $(TEX).rtf
		osascript -e 'tell application "Emacs" to activate'

.PHONY:
install:	$(TEX).pdf
		cp $(TEX).pdf $(HOME)/Desktop

.PHONY:
clean:
		rm -fr $(OBJS_TO_DEL)
