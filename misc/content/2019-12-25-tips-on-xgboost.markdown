Status: published
Date: 2019-12-26 23:46:11
Author: Benjamin Du
Slug: tips-on-xgboost
Title: Tips on XGBoost
Category: AI
Tags: AI, data science, machine learning, XGBoost

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. It is suggested that you use the sklearn wrapper classes `XGBClassifier` and `XGBRegressor`
    so that you can fully leverage other tools of the sklearn package.

## Parameters

### Number of Decision Trees (`n_estimators`)

### max_features

### Depth of Decision Trees (`max_depth`)

### Early Stopping (`early_stopping_rounds`)

Prevent overfitting.

### learning_rate

### subsample

`subsample` is for each tree the percentage of rows taken to build the tree. 
I recommend not taking out too many rows, 
as performance will drop a lot. Take values from 0.8 to 1.

### colsample_bytree

Maximum percentage of features used by each tree.

number of columns used by each tree. In order to avoid some columns to take too much credit for the prediction (think of it like in recommender systems when you recommend the most purchased products and forget about the long tail), take out a good proportion of columns. Values from 0.3 to 0.8 if you have many columns (especially if you did one-hot encoding), or 0.8 to 1 if you only have a few columns.

### gamma

A regularization parameter. 
Either 0, 1 or 5.

## [XGBClassifier.fit](https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=classifier#xgboost.XGBClassifier.fit)

The method `XGBClassifier.fit` takes a parameter `eval_set`
which is a list of tuples of the format (x, y).
Notice that this parameter is NOT used for grid search but for tracking performance for early stopping only.
If `eval_set` contains multiple datasets,
then only the last dataset is used for early stopping.

## Set Parameters for XGBClassifier or XGBRegressor

It is suggested that you use the method `set_params` to set parameters after creating a model
instead of setting parameter on model creation.

https://stackoverflow.com/questions/34674797/xgboost-xgbclassifier-defaults-in-python

## Parameter Tuning 

https://sites.google.com/view/lauraepp/parameters

## Questions 

Any difference between xgboost.cv and the cross validation in sklearn?
which one should I use?

## References

https://machinelearningmastery.com/tune-number-size-decision-trees-xgboost-python/

https://towardsdatascience.com/fine-tuning-xgboost-in-python-like-a-boss-b4543ed8b1e

https://towardsdatascience.com/a-beginners-guide-to-xgboost-87f5d4c30ed7

https://www.datacamp.com/community/tutorials/xgboost-in-python