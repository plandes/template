#set($dateYear= $dateTool.get('yyyy/dd/MM'))
#set($pdf-file-name = $description.replace(" ", ""))
#set($double-hash = '##')
${double-hash} @meta: {desc: 'Slides LaTeX makefile', date: '${dateYear}'}


#[[## Build configuration]]#
#
# make modules to add functionality to a build
PROJ_MODULES =		tex-biber

# make modules to include before the build is configured
PROJ_LOCAL_MODULES =	tex-graffle

# the latex source file stem
TEX =			slides

# the build process will create a presentation version
TEX_SLIDES =		1

# override/add to default paths
#TEX_PATH +=
#BIB_FILE =


#[[## User defined]]#
#
# distribution file name
#FINAL_NAME =		${pdf-file-name}Slides


#[[## Includes]]#
#
include ../config/${project}.mk
include ../zenbuild/main.mk
