# build file for ${project-name}

all:	compile

.PHONY:	compile
compile:
	mvn compile

.PHONY:	test
test:
	mvn -Plogging-deps test

.PHONY:	package
package:
	mvn -Plogging-deps package

.PHONY:	fatjar
fatjar:
	mvn -Pfat-jar compile assembly:single

.PHONY:	install
install:
	mvn -Plogging-deps install

.PHONY:	site
site:
	mvn -Plogging-deps site

.PHONY:	run
run:
	mvn -Plogging-deps compile exec:exec

.PHONY:	docs
docs:
	mvn javadoc:javadoc

.PHONY:	dist
dist:
	mvn -Plogging-deps package appassembler:assemble

.PHONY:	clean
clean:
	mvn clean

.PHONY:	deploy
deploy:
	mvn clean package deploy
