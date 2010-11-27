<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:exsl="http://exslt.org/common"   
                version="1.0"
                exclude-result-prefixes="exsl">


<xsl:param name="background-color" select="green"/>
<xsl:param name="html.stylesheet" select="'stylesheet.css'"/>
<xsl:param name="use.id.as.filename" select="1"/>
<xsl:param name="chunk.section.depth" select="1"></xsl:param>
<xsl:template name="user.footer.content">
  <HR/>
  <small><a href="https://dl.dropbox.com/u/1086388/d20ascii/out/srd/legal_information_2.html">
    Legal Information
  </a></small>
</xsl:template>
</xsl:stylesheet>
