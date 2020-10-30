# Bibliography Documents

Contains Details about Bibliography and different portions of it

#### Author: Sudeshna Bora

## <a name="usage"> How to incorporate Bibliography</a>
To add bibliography . We can either add it at the last or make a separate bibliography file with extention (.bib) [preferred]. Bibliography is initialised and incorporated as

<pre>
\bibliographystyle{[acm]}
\bibliography{all}
</pre>
Unless any content of the bibliography is not reference by <code>\cite</code> , that entry from the bib file is not added into the Bibliography/Reference page. 
Inorder to show all the contents of the bib file without being reference use
<code>\nocite{*}</code>

## <a name="nomenclature"> The style to mention bibliography </a>

<pre>
@Article{Zufferey06tro,
  author        = {Zufferey, Jean-Christophe and Floreano, Dario},
  title         = {Fly-inspired visual steering of an ultralight indoor
                  aircraft},
  journal       = tro,
  year          = 2006,
  volume        = 22,
  number        = 1,
  pages         = {137--146},
  month         = feb
}
</pre>

<b>Zufferey06tro:</b> UserYearJournal
## <a name="components"> Useful Components</a>

| Field Name  | Example  | Usage  | 
|-------------|----------|--------|
|  @string    | @string{jgg1 = "Journal of Gnats and Gnus, Series~1"}  | @string{jgg1 = "Journal of Gnats and Gnus, Series~1"}  |
|  @type | @manual ,  @Article etc  |  Different types of Bibliography documents. We get this from google scholar citations | 


