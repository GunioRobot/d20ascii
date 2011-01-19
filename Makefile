all: clearmess srd-all handbooks
	python src/couch.py

srd-all: srd-epub srd-html srd-pdf srd-html-nochunks

clearmess:
	rm -rf *~ */*~ */*/*~ */*/*/*~

gitsave: clearmess
	git add src
	git add -u
	git commit -a

srd-html: out/srd/index.html

srd-html-nochunks: out/srd.html

out/srd.html: out/srd.xml
	mkdir -p out
	xmlto -o out html-nochunks out/srd.xml

out/srd/index.html: out/srd.xml src/mychunk.xsl src/stylesheet.css
	mkdir -p out
	xmlto -o out/srd xhtml out/srd.xml -m src/mychunk.xsl
	cp src/stylesheet.css out/srd

srd-pdf: out/srd.pdf

out/srd.pdf: out/srd.xml
	mkdir -p out
	dblatex -o out/srd.pdf -t pdf out/srd.xml

srd-epub: out/srd.epub

out/srd.epub: out/srd.xml
	mkdir -p out
	dbtoepub -o out/srd.epub out/srd.xml

out/srd.xml: src/srd/*.asciidoc gen/srd/base-classes.asciidoc Makefile src/handbooks/*asciidoc
	mkdir -p out
	asciidoc -a idprefix= -d book -b docbook -o out/srd.xml src/srd/srd.asciidoc

clean:
	rm -rf out
	rm -rf gen

gen/srd/base-classes.asciidoc: src/srd/base-classes/*.yaml
	mkdir -p gen/srd
	python src/classes.py>gen/srd/base-classes.asciidoc

handbooks:	out/beingbatman.html out/beingbatman.pdf

out/index.html: out/srd.xml
	xmlto -o out/index.html html-nochunks out/srd.xml

out/beingbatman.html:	out/beingbatman.xml
	mkdir -p out
	xmlto -o out html-nochunks out/beingbatman.xml

out/beingbatman.pdf:	out/beingbatman.xml
	mkdir -p out
	dblatex -o out/beingbatman.pdf -t pdf out/beingbatman.xml

out/beingbatman.xml:	src/handbooks/beingbatman.asciidoc
	mkdir -p out
	asciidoc -d book -b docbook -o out/beingbatman.xml src/handbooks/beingbatman.asciidoc
