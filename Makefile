all: clearmess srd-all srd-ua-all

srd-all: srd-epub srd-html srd-pdf srd-html-nochunks

srd-ua-all: srd-ua-epub srd-ua-html srd-ua-pdf srd-ua-html-nochunks

clearmess:
	rm -rf *~ */*~ */*/*~ */*/*/*~

gitsave: clearmess
	git add src
	git add -u
	git commit -a

srd-html: out/srd/index.html

srd-html-nochunks: out/srd.html

out/srd.html: out/srd.xml
	xmlto -o out html-nochunks out/srd.xml

srd-ua-html-nochunks: out/srd-ua.html

out/srd-ua.html: out/srd-ua.xml
	xmlto -o out html-nochunks out/srd-ua.xml

out/srd/index.html: out/srd.xml src/mychunk.xsl
	xmlto -o out/srd xhtml out/srd.xml -m src/mychunk.xsl

srd-pdf: out/srd.pdf

out/srd.pdf: out/srd.xml
	dblatex -o out/srd.pdf -t pdf out/srd.xml

srd-epub: out/srd.epub

out/srd.epub: out/srd.xml
	dbtoepub -o out/srd.epub out/srd.xml

out/srd.xml: src/*.asciidoc src/tables/*.asciidoc src/classes/*.asciidoc Makefile
	asciidoc -a idprefix= -d book -b docbook -o out/srd.xml src/srd.asciidoc

srd-ua-html: out/srd-ua/index.html

out/srd-ua/index.html: out/srd-ua.xml src/mychunk.xsl
	xmlto -o out/srd-ua xhtml out/srd-ua.xml -m src/mychunk.xsl

srd-ua-pdf: out/srd-ua.pdf

out/srd-ua.pdf: out/srd-ua.xml
	dblatex -o out/srd-ua.pdf -t pdf out/srd-ua.xml

srd-ua-epub: out/srd-ua.epub

out/srd-ua.epub: out/srd-ua.xml
	dbtoepub -o out/srd-ua.epub out/srd-ua.xml

out/srd-ua.xml: src/*.asciidoc src/tables/*.asciidoc src/classes/*.asciidoc Makefile
	asciidoc -d book -a idprefix= -a unearthed-arcana -b docbook -o out/srd-ua.xml src/srd.asciidoc


clean:
	rm -rf out/*


