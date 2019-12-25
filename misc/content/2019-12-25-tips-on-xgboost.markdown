Status: published
Date: 2019-12-25 12:21:22
Author: Benjamin Du
Slug: tips-on-xgboost
Title: Tips on XGBoost
Category: AI
Tags: AI, data science, machine learning, XGBoost

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


## Parameters

### Number of Decision Trees (`n_estimators`)

### Size of Decision Trees (`max_depth`)



### Early Stopping (`early_stopping_rounds`)

### learning_rate

### subsample

`subsample` is for each tree the percentage of rows taken to build the tree. 
I recommend not taking out too many rows, 
as performance will drop a lot. Take values from 0.8 to 1.

### colsample_bytree

number of columns used by each tree. In order to avoid some columns to take too much credit for the prediction (think of it like in recommender systems when you recommend the most purchased products and forget about the long tail), take out a good proportion of columns. Values from 0.3 to 0.8 if you have many columns (especially if you did one-hot encoding), or 0.8 to 1 if you only have a few columns.

### gamma

A regularization parameter. 
Either 0, 1 or 5.



## References

https://machinelearningmastery.com/tune-number-size-decision-trees-xgboost-python/

https://towardsdatascience.com/fine-tuning-xgboost-in-python-like-a-boss-b4543ed8b1e