---
title: Keywords Extracting from Text
created: '2014-11-22T13:08:04-08:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: keywords-extracting-from-text
license: CC-BY-4.0
tags:
  - machine learning
  - text mining
  - data mining
  - data science
  - NLP
  - deep learning
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Word Stemming

1. existing stemming method such as NLTK.PorterStem, etc.

1. didn't -> did not, there's -> there is, etc.
   Mr. -> Mister
   Mrs. -> ...
   Ms. -> ...

## Other things

1. it seems that it is hard to get useful information using 1-gram

1. URLs in text are often important and is relatively easy to extract.

1. After handing URLs, you can replace "/" and "." with spaces to avoid confusing them with real long words.

1. long words often contain useful information,
   however, you have to be careful about words of the form "and/or", etc.
   And do not confuse it with URLs.

1. the idea of keeping upper/lower quantile (e.g., 5%) of long words, 2-grams, etc. is a very good idea
