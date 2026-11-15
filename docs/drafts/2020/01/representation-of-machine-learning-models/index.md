---
title: Representation of Machine Learning Models
created: '2020-01-05T15:32:24-08:00'
date: '2026-11-15T12:20:36-08:00'
authors:
  - bendu
label: representation-of-machine-learning-models
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - serialization
  - model representation
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [Open Neural Network Exchange (ONNX)](https://onnx.ai/)

https://github.com/onnx

https://github.com/onnx/onnxmltools

## [Predictive Model Markup Language (PMML)](http://dmg.org/pmml/v4-4/GeneralStructure.html)

https://github.com/jpmml/sklearn2pmml

[PMML4S](https://github.com/autodeployai/pmml4s)
is a PMML (Predictive Model Markup Language) scoring library for Scala. It provides both Scala and Java Evaluator API for PMML.

[JPMML-Evaluator](https://github.com/jpmml/jpmml-evaluator)
is a Java evaluator API for PMML.

## [Plain Old Java Object (POJO)]

H2O supports exporting models into POJO (JAR) files.

## [MLeap](https://mleap-docs.combust.ml/)

## Pickle

Some Python libraries support serializaing a model into pickle format.

## Save and Load Models in PyTorch

https://pytorch.org/docs/stable/notes/serialization.html#recommend-saving-models

## PyTorch -> ONNX -> TensorFlow

https://github.com/onnx/onnx-tensorflow/issues/491

https://towardsdatascience.com/converting-a-simple-deep-learning-model-from-pytorch-to-tensorflow-b6b353351f5d
