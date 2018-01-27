ALL_CSVS = $(wildcard *.csv)
GEN_PLT = ../../../common/scripts/gen_plt.py

# Make all plots from csvs
$(ALL_CSVS): %.png : %.csv
	$(GEN_PLT) $< $@
