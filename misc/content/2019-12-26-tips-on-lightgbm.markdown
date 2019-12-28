Status: published
Date: 2019-12-27 23:02:16
Author: Benjamin Du
Slug: tips-on-lightgbm
Title: Tips on LightGBM
Category: AI
Tags: AI, data science, machine learning, LightGBM

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. It is strongly suggested that you specify categorical variables as categorical. 

		:::bash
		lgb_train = lgb.Dataset(x_train, y_train, feature_name=features,
			categorical_feature=categorical_features)

1. LightGBM supports distributed training on multiple machines (without Spark).

    https://github.com/microsoft/LightGBM/tree/master/examples/parallel_learning

## Parameter Tuning

https://sites.google.com/view/lauraepp/parameters

https://lightgbm.readthedocs.io/en/latest/Parameters.html

## References

https://lightgbm.readthedocs.io/en/latest/_modules/lightgbm/sklearn.html

https://www.kaggle.com/nicapotato/multi-class-lgbm-cv-and-seed-diversification

https://sefiks.com/2018/10/13/a-gentle-introduction-to-lightgbm-for-applied-machine-learning/

https://github.com/microsoft/LightGBM/blob/master/examples/python-guide/sklearn_example.py

https://github.com/microsoft/LightGBM/tree/master/examples/python-guide

https://www.kaggle.com/tapioca/multiclass-lightgbm

https://lightgbm.readthedocs.io/en/latest/Features.html

https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.train.html

