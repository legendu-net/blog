Status: published
Date: 2019-12-27 10:06:38
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

2. There are 2 types of boosters (`gbtree` and `gblinear`), 
    It is suggested that you always use tree booster (`gbtree`) 
    as it always outperformas the linear booster (`gblinear`).

3. Instead of training, validation and testing sets,
    people typically use training and testing sets 
    and parameter tuning is done using cross validation based on the training data.
    The advantage of this way is that the data is better used. 

## Parameters

### General Parameters

It is suggested that you keep the default values for the general parameters 
(`booster`, `silent` and `nthrad`).

#### booster [default=gbtree]

The booster parameter specifies the type of model to run. 
It has 2 options `gbtree` (tree-based models) and `gblinear` (linear models).
It is suggested that you keep the default value (`gbtree`) 
as `gbtree` always outperforms `gblinear`.

#### silent [default=0]

The silent mode is activated (no running messages will be printed) when the `silent` parameter is set to 1.
It is suggested that you keep the default value (deactivate the silent mode)
which helps you understanding the model and training.

#### nthread [default to maximum number of threads available]

Number of threads to be used in training.
It is suggested that you keep the default value.


### Number of Decision Trees (`n_estimators`)

### max_features

### Depth of Decision Trees (`max_depth`)

### Early Stopping (`early_stopping_rounds`)

Prevent overfitting.

### Learning Rate (`learning_rate`, `eta`)

The default value of `eta` is 0.3 in XGBoost.
The typical final values to be used is between 0.01 and 0.2.

### subsample

`subsample` is for each tree the percentage of rows taken to build the tree. 
I recommend not taking out too many rows, 
as performance will drop a lot. Take values from 0.8 to 1.

### colsample_bytree

Maximum percentage of features used by each tree.

number of columns used by each tree. In order to avoid some columns to take too much credit for the prediction (think of it like in recommender systems when you recommend the most purchased products and forget about the long tail), take out a good proportion of columns. Values from 0.3 to 0.8 if you have many columns (especially if you did one-hot encoding), or 0.8 to 1 if you only have a few columns.

## Booster Parameters

### min_child_weight [default=1]

Defines the minimum sum of weights of all observations required in a child.
It is used to control over-fitting. 
Higher values prevent a model from learning relations 
which might be highly specific to the particular sample selected for a tree.
Too high values can lead to under-fitting hence, 
it should be tuned using CV.

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

https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/

## Questions 

Any difference between xgboost.cv and the cross validation in sklearn?
which one should I use?

## References

https://machinelearningmastery.com/tune-number-size-decision-trees-xgboost-python/

https://towardsdatascience.com/fine-tuning-xgboost-in-python-like-a-boss-b4543ed8b1e

https://towardsdatascience.com/a-beginners-guide-to-xgboost-87f5d4c30ed7

https://www.datacamp.com/community/tutorials/xgboost-in-python

https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/
