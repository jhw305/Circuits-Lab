LATEX=pdflatex
BUILD=$(LATEX) main.tex

build: main.tex
	$(BUILD)
	bibtex main.aux
	$(BUILD)
	$(BUILD)
