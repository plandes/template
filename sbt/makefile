ENSIME_CONF=	.ensime

all:		init

.PHONY:
init:		$(ENSIME_CONF)

$(ENSIME_CONF):
	sbt ensimeConfig

.PHONEY:
run:
	sbt run

clean:
	rm -rf .ensime* project target
