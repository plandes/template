# GNU make file to automate build of all latex documents

SUBS=paper report slides

# generate all PDFs
all:
	@for i in $(SUBS) ; do \
		[ -d $$i ] && make -C $$i pdf ; \
	done

# generate and show all PDFs
.PHONY:	showpdf
showpdf:
	@for i in $(SUBS) ; do \
		[ -d $$i ] && make -C $$i showpdf ; \
	done

# clean up all generated objects
.PHONY:	clean
clean:
	@for i in $(SUBS) ; do \
		[ -d $$i ] && make -C $$i clean ; \
	done
