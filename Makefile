all: index.html

%.html: %.haml pricelist.json
	haml $< > $@
