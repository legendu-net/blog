Status: published
Date: 2021-09-16 11:38:52
Modified: 2021-09-16 21:26:05
Author: Benjamin Du
Slug: study-notes-on-knowledge-graph
Title: Study Notes on Knowledge Graph
Category: Computer Science
Tags: Computer Science, Knowledge Graph, KG, machine learning, deep learning, data science

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[Data Modeling with RDF(S)](https://graphdb.ontotext.com/free/devhub/rdfs.html)

[Learn OWL and RDFS](https://cambridgesemantics.com/blog/semantic-university/learn-owl-rdfs/rdfs-vs-owl/)
 
RDF: Resource Description Framework
OWL: Web Ontology Language

## Products 

### neo4j

### RDFox
Unique features of RDFox include the very powerful rule language (roughly equal to SPARQL query language) and incremental maintenance of materialised edges. It is also very high performance; typically orders of magnitude faster than other KGs.

### Amazon Neptune
Neptune can support very large KGs, but it doesn’t support rules/reasoning, and is very slow compared to RDFox. We have a collaboration with Neptune where we use RDFox to support reasoning and fast query answering over large KGs stored in Neptune.

### TopBraid

AFAIK Top Braid has a relatively limited language (SHACL), mainly for defining constraints. RDFox can load SHACL, but it supports much more powerful rules for generating new edges.

### Allegro 

Allegro graph is a triple store, but AFAIK it has very limited support for ontologies/rules.
