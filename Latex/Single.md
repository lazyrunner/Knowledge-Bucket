# Single Latex Documentation
This documentation is to show how to write a report using a single latex document. The same can be achieved by multiple latex file but will be handled in a separate section. A sample Latex Template can be found [here](https://github.com/SudeshnaBora/Knowledge-Bucket/blob/main/docs/SinglePageStructure.tex).


#### Author: Sudeshna Bora

#### Application Used : Overleaf .
But can work with tekmaker etc.

---
## <a name="Preamble"> Preamble </a>
---
The first portion of the Latex document is the preamble. This marks the details of the documents, packages to be used , special commands (spacing, headers etc).

<pre>
# gives us the type of documents
\documentclass[10pt]{report}

# import package [] is an optional argument for the package
\usepackage[<optional_parameter>]{package_name}

# Additional sections for other configuration
</pre>

### <a name="Header"> Create Custom Header Configuration</a>
<b>Package used: </b> \usepackage{fancyhdr}
<br>
<pre>
\pagestyle{fancy}

#fancy head and foot
\fancyhf{} 
\setlength\headheight{15pt}
\fancyhead[L]{Lab Rotation}

#adds pagenumber
\rhead{ \thepage} 
</pre>

### <a name="Page_Number">Adding Page Numbering</a>

If using fancyhdr package. Page numbering can be done by using <b>\thepage</b>. In the [header](#Header) section , we are placing the header in right head (rhead) portion of the page.

---
## <a name="Main_Document"> Main Document </a>
---

The main document starts with 

<pre>\begin{document}</pre>

and ends with

<pre>\end{document}</pre>

### <a name="Title"> Title Page</a>

The title section/page starts with \title{}. To add author \author{} and to render the title we use \maketitle. A simple example is shown below. 

<pre>
\title{ \normalsize \textsc{Lab Rotation}
		\\ [2.0cm]
		\HRule{0.5pt} \\
		\LARGE \textbf{\uppercase{IMAGE RECONSTRUCTION OF RETINOMORPHIC EVENT CAMERA}}
		\HRule{2pt} \\ [0.5cm]
		\normalsize  \vspace*{5\baselineskip}}

\date{} #Adding this here to remove date present in the definition of @maketitle

\author{
		Sudeshna Bora \\
        Guided By - Prof. Dr. Guillermo Gallego  \\
Bernstein Center for Computational Neuroscience, Berlin\\ }

\maketitle

\newpage
</pre>

<b>Note:</b> Adding \date{} removes the date present in the maketitle definition.

### <a name="new_page"> How to create new page </a>

The command to create new page is <b>\newpage</b>

### <a name="table_of_contents"> Table of Contents</a>

The command to create table of contents is \tableofcontents. Remember to add \newpage before and after it for it to be in a new page.

All [numbered](#Numbering_Sections) sections (chapters, sections and subsections) would be added to the Table of Contents. If a section is not numbered add <pre>\addcontentsline{toc}{[subsection]}{[Functioning of Event Camera]}. Another benefit of adding this is the title in the contents and the actual section heading can be different</pre>

#### <a name="Numbering_Sections">How to Number Sections/Chapters etc </a>

The direct way of adding numbers to a section is to use \section , \chapters , \subsection etc without *. In case we are using * , to add numbers we can use <pre>\renewcommand{\thesection}{\Roman{section}}</pre>. Another important point is by using \renewcommand , we can change the numbering style of the chapters/sections/ subsections.

#### <a name="numbering_style"> Changing numbering style in sections/chapters etc </a>

To change numbering style use <pre>\renewcommand{\thesection}{\Roman{section}}</pre>. 

#### <a name="Different_name"> How to have different names in TOC and in actual page </a>

To have different names in TOC and in actual page we can use \chapter[]{} or section etc. The content inside [] gives the name in the table of content whereas the {} gives the name in the actual page.

### <a name="Equations"> How to write Equations </a>

To write equations use 

<pre>
\begin{equation}
  \Delta L(X_{k},t_{k}) = L(X_{k},t_{k}) - L(X_{k},t_{k} - \Delta t_{k})
\end{equation}
</pre>

To [reference](#reference) equation we can add <pre>\label{}</pre> .

### <a name="Figures"> Add Multiple figure in same line </a>

To add multiple figures

<pre>
\begin{figure}
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{positive_ESIM.PNG}
  \caption{Image of the positive event voxelgrid where events are created by ESIM}
  \label{fig:positive event}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{self_event.png}
  \caption{Image of the negative event voxelgrid where events are created by Algorithm}
  \label{fig:negative_event}
\end{subfigure}
\caption{Voxelgrid of events}
\label{fig:events}
\end{figure}
</pre>

The labels are used for [referencing](#reference)

### <a name="reference"> Referencing Figures , Equations etc </a>

To reference any entity (except bibliography) we use <pre>\ref{[label_name]}</pre>. For an entity to be referenceble , add <pre>\label{[label_name]}</pre>

---

## <a name="Bibliography"> Bibliography</a>

To add bibliography . We can either add it at the last or make a separate bibliography file with extention (.bib) [preferred]. Bibliography is initialised and incorporated as 

<pre>
\bibliographystyle{[acm]}
\bibliography{all}
</pre>

Unless any content of the bibliography is not reference by <pre>\cite</pre> , that entry from the bib file is not added into the Bibliography/Reference page. Inorder to show all the contents of the bib file without being reference use <pre>\nocite{*}</pre>.






