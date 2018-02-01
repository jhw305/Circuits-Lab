LATEX=pdflatex
BUILD=$(LATEX) nmos_wrap.tex

build: nmos.tex nmos_wrap.tex
	$(BUILD)
	$(BUILD)

clean:
	rm nmos_wrap.aux nmos_wrap.log
