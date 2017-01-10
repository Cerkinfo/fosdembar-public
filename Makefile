all: index.html

%.html: %.haml
	haml $< > $@
