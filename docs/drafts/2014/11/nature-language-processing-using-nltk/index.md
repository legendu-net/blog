---
title: Nature Language Processing Using NLTK
created: '2014-11-22T14:30:18-08:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: nature-language-processing-using-nltk
license: CC-BY-4.0
tags:
  - machine learning
  - data mining
  - text mining
  - data science
  - NLP
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

nltk.util.ngrams
nltk.bigrams
nltk.PorterStemmer

```
:::python
from nltk.util import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 6
sixgrams = ngrams(sentence.split(), n)
for grams in sixgrams:
    print grams
```
