---
title: Cross Validation in Machine Learning
created: '2013-04-03T00:00:00-07:00'
date: '2026-11-15T09:19:13-08:00'
authors:
  - bendu
label: cross-validation-in-machine-learning
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - cross validation
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Training and Testing Data Set

- good when you have large amount of data

- usually use 1/5 to 1/3 of the data as testing data set.

## K-fold CV

- suitable when you have medium number of data

- K=10 is popular

- computationally extensive

## Leave-k-out CV

- Use this way only when you have very limited number of data.

- Leave-1-out is a specially case of the K-fold CV.

- computationally very extensive

## Some Rules:

- 10 times number of parameters, probably in good shape

- 20 times number of parameters, usually perfect good
