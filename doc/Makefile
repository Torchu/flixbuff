DOC := proyecto.tex

all: clean doc

doc: $(DOC:.tex=.pdf)

all: proyecto.pdf

%.pdf: %.tex
	pdflatex $< && bibtex $* && pdflatex $< && pdflatex $<

clean:
	rm -f *.aux *.bbl *.blg *.lof *.log *.lot *.out *.toc *.pdf

