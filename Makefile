all: index.html menu.pdf

%.html: %.haml pricelist.json
	haml $< > $@

pricelist.tex: makemenu.py pricelist.json
	python $^ > $@

menu.pdf: menu.tex pricelist.tex
	pdflatex $<

clean:
	rm -f pricelist.tex index.html
