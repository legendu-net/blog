Status: published
Date: 2019-12-24 13:51:40
Author: Benjamin Du
Slug: libraries-for-gradient-boosting
Title: Libraries for Gradient Boosting
Category: AI
Tags: AI, machine learning, data science, gradient boosting, XGBoost, LightGMB, CatBoost

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## XGBoost

https://xgboost.ai/

[XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/)

## Speedup XGBoost

https://machinelearningmastery.com/best-tune-multithreading-support-xgboost-python/


## XGBoost with Spark

https://xgboost.readthedocs.io/en/latest/jvm/xgboost4j_spark_tutorial.html

https://xgboost.ai/2016/10/26/a-full-integration-of-xgboost-and-spark.html

https://databricks.com/session/building-a-unified-data-pipeline-with-apache-spark-and-xgboost

https://medium.com/cloudzone/xgboost-distributed-training-and-predicting-with-apache-spark-1127cdfb31ae

https://news.developer.nvidia.com/gpu-accelerated-spark-xgboost/

https://towardsdatascience.com/pyspark-and-xgboost-integration-tested-on-the-kaggle-titanic-dataset-4e75a568bdb

https://www.kdnuggets.com/2016/03/xgboost-implementing-winningest-kaggle-algorithm-spark-flink.html

## LightGBM

## CatBoost

https://catboost.ai/news/best-in-class-inference-and-a-ton-of-speedups

## Comparisons

Even though CatBoost claims to be faster than XGBoost and LightGBM,
most other resources says the opposite. 
CatBoost is seldomly used in Kaggle competitions.
LightGBM is faster than XGBoost and is used more and more in Kaggle competitions.
If you need a mature and stable solution,
XGBoost is the right choice.
If you need high speed,
LightGBM is the way to go.

https://datascience.stackexchange.com/questions/49567/lightgbm-vs-xgboost-vs-catboost

https://medium.com/data-design/getting-the-most-of-xgboost-and-lightgbm-speed-compiler-cpu-pinning-374c38d82b86
