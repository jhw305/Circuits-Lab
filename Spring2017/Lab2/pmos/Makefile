LATEX=pdflatex
BUILD=$(LATEX) pmos_wrap.tex

build: pmos.tex pmos_wrap.tex
	$(BUILD)
	$(BUILD)

clean:
	@rm pmos_wrap.aux pmos_wrap.log
