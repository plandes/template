#set($dateYear= $dateTool.get('yyyy/dd/MM'))
#set($pdf-file-name = $description.replace(" ", ""))
#set($double-hash = '##')
${double-hash} @meta: {desc: 'LaTeX compilation make include', date: '${dateYear}'}


#[[## Build configuration]]#
#
# type of project
PROJ_TYPE ?=		tex
# LaTeX include path
TEX_PATH +=		$(abspath ../sty):
# bibliography file path
BIB_FILE ?=		$(abspath ../sty/${project}.bib)


#[[## Project]]#
#
# distribution file name
FINAL_NAME ?=		${pdf-file-name}
# uncomment to add all tex paths to bibstract
#BIBSTRACT_EXPORT_ALL =	1
# uncomment to add a custom bibstract configuration
#BIBSTRACT_ARGS =	export --config ../config/bibstract.conf
# the QR URL
TEX_QR_URL = 		"https://github.com/${author-user}/${project}"
# add non-anonymous urls and authors
#TEX_LATEX_INIT_ADD +=	\newif\ifisfinal\isfinaltrue


#[[## Build submodules]]#
#
# make build dependencies
_ :=	$(shell cd .. && [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )
