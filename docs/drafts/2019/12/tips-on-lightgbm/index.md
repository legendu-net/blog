---
title: Tips on LightGBM
created: '2019-12-03T01:26:29-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-lightgbm
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - LightGBM
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. It is strongly suggested that you load data into a pandas DataFrame
   and handle categorical variables
   by specifying a `dtype` of `"category"` for those categorical variables.

   ```
    :::bash
    df.cat_var = df.cat_var.astype("category")
   ```

   This is the easiest way to handle categorical variables in LightGBM.
   For more details,
   please refer to
   [Handle Categorical Variables in LightGBM](handle-categorical-variables-in-lightgbm)
   .

1. The sklearn wrapper of LightGBM lag behind the development of sklearn.
   Be aware of the latest supported version of sklearn
   when you use sklearn wrapper of LightGBM.
   It is suggested that you use the original API of LightGBM to avoid version issues.

1. It is suggested that you always specify an validation dataset
   when you train a model using the function `train`.

1. LightGBM supports distributed training on multiple machines (without Spark).

   https://github.com/microsoft/LightGBM/tree/master/examples/parallel_learning

## Hyper Parameter Tuning

[Optuna](tips-on-optuna)
is a good framework for tuning hyper parameters.

https://sites.google.com/view/lauraepp/parameters

https://lightgbm.readthedocs.io/en/latest/Parameters.html

## GPU

https://lightgbm.readthedocs.io/en/latest/GPU-Tutorial.html

## References

[Handle Categorical Variables in LightGBM](handle-categorical-variables-in-lightgbm)

[Parameters](https://lightgbm.readthedocs.io/en/latest/Parameters.html#parameters)

[Metric Parameters](https://lightgbm.readthedocs.io/en/latest/Parameters.html#metric-parameters)

[LightGMB Benchmark](https://lightgbm.readthedocs.io/en/latest/Experiments.html)

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.Dataset.html#lightgbm-dataset

https://lightgbm.readthedocs.io/en/latest/_modules/lightgbm/sklearn.html

https://www.kaggle.com/nicapotato/multi-class-lgbm-cv-and-seed-diversification

https://sefiks.com/2018/10/13/a-gentle-introduction-to-lightgbm-for-applied-machine-learning/

https://github.com/microsoft/LightGBM/blob/master/examples/python-guide/sklearn_example.py

https://github.com/microsoft/LightGBM/tree/master/examples/python-guide

https://www.kaggle.com/tapioca/multiclass-lightgbm

https://lightgbm.readthedocs.io/en/latest/Features.html

https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.train.html
