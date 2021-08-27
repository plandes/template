#[[## makefile generates documents (HTML only for now) from org mode files]]#

# type of project
PROJ_TYPE =		org
# make modules to add functionality to a build
#PROJ_MODULES=		docker release model

# use Bootstrap compatible HTML Back-End for Org instead of default emacs
#OM_EXPORT_FUNC_HTML =	org-twbs-export-to-html
#OM_EXPORT_EVAL =	"(load (car (file-expand-wildcards \"~/opt/var/emacs/elpa/ox-twbs*/ox-twbs.el\")))"

# derived files from Emacs exports
ADD_CLEAN +=		*.html *.pdf *.tex *.doc *.odt

# make build dependencies
_ :=	$(shell [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add git@github.com:plandes/zenbuild.git && make gitinit )

# uncomment to refresh for every default make
#all:			clean show

include ./zenbuild/main.mk
