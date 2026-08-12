---
title: Tips on scikit-learn
created: '2019-12-01T10:06:27-08:00'
date: '2026-08-11T22:19:28-07:00'
authors:
  - bendu
label: tips-on-scikit-learn
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - scikit-learn
  - sklearn
  - pipeline
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Cross validation in scikit-learn supports pipeline in addition to vanilla models.
   Please refer to
   [Cross Validation Pipeline](https://chrisalbon.com/machine_learning/model_evaluation/cross_validation_pipeline/)
   for more details.

1. [Label encoding](https://scikit-learn.org/stable/modules/preprocessing_targets.html#label-encoding)
   is an easy way to convert a categorical response/target variable to a numeric one and back to the raw value space.
   For transform of response/target varible in regression,
   please refer to [Transforming Target in Tegression](https://scikit-learn.org/stable/modules/compose.html#transforming-target-in-regression).

1. [Skorch](https://github.com/skorch-dev/skorch)

## Metrics

- [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html)

- [precision_recall_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve)

- [average_precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score)

## References

https://scikit-learn.org/stable/modules/compose.html#transforming-target-in-regression

[Split a Dataset into Train and Test Datasets in Python](split-a-dataset-into-train-and-test-datasets-in-python)
