#[[## makefile for the ${project-name} app]]#

MTARG=		target

.PHONY:		run
run:
		./${project}

.PHONY:		deps
deps:
		pip install -r src/requirements.txt

.PHONY:		clean
clean:
		rm -fr $(MTARG)
		find . -type d -name __pycache__ -prune -exec rm -r {} \;
