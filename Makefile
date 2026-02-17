# Change 'cv' to match your filename (e.g., resume.tex -> resume)
FILENAME = cv
LATEX    = latexmk
FLAGS    = -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all clean distclean

all: $(FILENAME).pdf

$(FILENAME).pdf: $(FILENAME).tex
	$(LATEX) $(FLAGS) $(FILENAME).tex

clean:
	$(LATEX) -c
	rm -f *.nav *.snm *.vrb *.bbl *.run.xml *.fls *.log *.*SAVE-ERROR *.gz *.out *.fdb* *.bcf *.aux *.pdf

distclean: clean
	$(LATEX) -C
