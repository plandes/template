# makefile for the ${project-name} app

MTARG =		target

.PHONY:		run
run:
		./${project}.py

.PHONY:		clean
clean:
		rm -fr $(MTARG)
		find . -type d -name __pycache__ -prune -exec rm -r {} \;
