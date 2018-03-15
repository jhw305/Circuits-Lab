LATEX=pdflatex
BUILD=$(LATEX) conclusion_wrap.tex

build: conclusion.tex conclusion_wrap.tex
	$(BUILD)
	$(BUILD)

clean:
	@rm *.log *.pdf *aux
