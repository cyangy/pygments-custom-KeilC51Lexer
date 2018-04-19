# pygments-custom-KeilC51Lexer
A custom C51-lexer for [Pygments](http://pygments.org/), for extra keyword highlighting when using the package [minted](https://github.com/gpoore/minted) in LaTeX. Adds some extra keywords like *\_at\_*,  And Some types  *sbit*, *idata*, *xdata*,*code*,*bit*,*sfr*

##  Based on  https://github.com/FSund/pygments-custom-cpplexer


## Install

    $ git clone https://github.com/cyang/pygments-custom-KeilC51Lexer.git
    $ cd pygments-custom-KeilC51Lexer
    $ (sudo) python setup.py install

### Verify

Verify that the package installed correctly by looking for the lexer "C51" in the output of

    $ pygmentize -L lexers

## Using the lexer in latex

Just use the **C51** or  **c51**  "language". In LaTeX this means something like this

    \begin{minted}{c51}
    sbit AD9837_SDATA = P0^5;	///<AD9837_SDATA
	sbit AD9837_SCLK  = P0^6;	///<AD9837_SCLK
	sbit AD9837_FSYNC = P0^7;	///<AD9837_FSYNC
	sfr ISP_CONTR = 0xE7;
    \end{minted}
or use it like this

	 \definecolor{bg}{rgb}{0.95,0.95,0.95}
	 \inputminted[linenos,firstnumber=last,mathescape,bgcolor=bg,breaklines,obeytabs=true,tabsize=1,fontsize=\normalfont,baselinestretch=1.0,gobble=0,numbers =left,numberfirstline,numbersep=4pt,stepnumber=1,stripall,stepnumberfromfirst]{c51}{SourceCode/AD9837Write.c}

See the minted package at https://github.com/gpoore/minted for more information.
