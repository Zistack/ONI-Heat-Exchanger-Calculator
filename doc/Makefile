all : HeatExchanger.pdf

HeatExchanger.pdf : HeatExchanger.tex
	xelatex -shell-escape HeatExchanger.tex
	xelatex -shell-escape HeatExchanger.tex

.PHONY : clean

clean :
	rm *.log
	rm *.aux
	rm -r _minted-*
	rm *.pdf
