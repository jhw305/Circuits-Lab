CSV_FNAMES = $(wildcard *.csv)
PNG_FNAMES = $(CSV_FNAMES:%.csv=%.png)
GEN_PLT = ../../../common/scripts/gen_plt.py

all: $(PNG_FNAMES)

# Make all plots from csvs
%.png: %.csv
	$(GEN_PLT) $< $@

clean:
	rm -rf $(PNG_FNAMES)

.PHONY: clean
