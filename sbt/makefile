ENSIME_CONF=	.ensime

all:		init

.PHONY:	init
init:		$(ENSIME_CONF)

$(ENSIME_CONF):
	sbt ensimeConfig

.PHONY: run
run:
	sbt run

.PHONY: compile
compile:
	sbt compile

clean:
	rm -rf .ensime* project target
