all: gitsave srd-epub srd-html srd-pdf

gitsave:
	rm -rf *~ */*~ */*/*~ */*/*/*~
	git add src
	git add -u
	git commit -a -m"Incremental save" --allow-empty

srd-html: out/srd/index.html

out/srd/index.html: out/srd.xml src/mychunk.xsl
	xmlto -o out/srd xhtml out/srd.xml -m src/mychunk.xsl

srd-pdf: out/srd.pdf

out/srd.pdf: out/srd.xml
	dblatex -o out/srd.pdf -t pdf out/srd.xml

srd-epub: out/srd.epub

out/srd.epub: out/srd.xml
	dbtoepub -o out/srd.epub out/srd.xml

out/srd.xml: src/*.txt src/tables/*.txt src/classes/*.txt
	asciidoc -d book -a unearthed-arcana -b docbook -o out/srd.xml src/srd.txt


clean:
	rm -rf out/*


