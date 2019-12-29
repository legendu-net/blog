Status: published
Date: 2019-12-28 23:32:48
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

https://medium.com/data-design/xgboost-gpu-performance-on-low-end-gpu-vs-high-end-cpu-a7bc5fcd425b

xgboost GPU is fast. 
Very fast. 
As long as it fits in RAM and you do not care about getting reproducible results (and getting crashes).
To keep getting those epic, 
stable and reproducible results (or if data is just too big for GPU RAM), 
keep using the CPU. There’s no real workaround (yet).


## XGBoost with Spark

https://towardsdatascience.com/build-xgboost-lightgbm-models-on-large-datasets-what-are-the-possible-solutions-bf882da2c27d

https://xgboost.readthedocs.io/en/latest/jvm/xgboost4j_spark_tutorial.html

https://xgboost.ai/2016/10/26/a-full-integration-of-xgboost-and-spark.html

https://databricks.com/session/building-a-unified-data-pipeline-with-apache-spark-and-xgboost

https://medium.com/cloudzone/xgboost-distributed-training-and-predicting-with-apache-spark-1127cdfb31ae

https://news.developer.nvidia.com/gpu-accelerated-spark-xgboost/

https://towardsdatascience.com/pyspark-and-xgboost-integration-tested-on-the-kaggle-titanic-dataset-4e75a568bdb

https://www.kdnuggets.com/2016/03/xgboost-implementing-winningest-kaggle-algorithm-spark-flink.html

## [LightGBM](https://github.com/microsoft/LightGBM)

### LightGBM with Spark 

https://github.com/Azure/mmlspark

https://www.reddit.com/r/datascience/comments/9w2qn8/deploying_a_lightgbm_model_with_spark/

https://towardsdatascience.com/build-xgboost-lightgbm-models-on-large-datasets-what-are-the-possible-solutions-bf882da2c27d

## CatBoost

https://catboost.ai/news/best-in-class-inference-and-a-ton-of-speedups

## Comparisons

The paper [Benchmarking and Optimization of Gradient Boosting Decision Tree Algorithms](https://arxiv.org/pdf/1809.04559.pdf)
compares the 3 libraries from the 3 perspectives/questions below
and claims that there is no clear win among the 3 libraries.

    1. How much acceleration can be expected when using GPU-based training routines?
    2. How well does this GPU-acceleration translate to reduced time-to-solution in the context of Bayesian hyper-parameter optimization?
    3. How well do the resulting models generalize to unseen data?

The article 
[Gradient Boosting Decision trees: XGBoost vs LightGBM (and catboost)](https://medium.com/kaggle-nyc/gradient-boosting-decision-trees-xgboost-vs-lightgbm-and-catboost-72df6979e0bb)
claims that LightGBM improves on XGBoost.

> In summary, 
> LightGBM improves on XGBoost. 
> The LightGBM paper uses XGBoost as a baseline and outperforms it in training speed and the dataset sizes it can handle. 
> The accuracies are comparable. 
> LightGBM in some cases reaches it’s top accuracy in under a minute and while only reading a fraction of the whole dataset. 
> This goes to show the power of approximation algorithms 
> and intelligently sampling a dataset to extract the most information as fast as possible.

The article [Xgboost vs Catboost vs Lightgbm: which is best for price prediction?](https://blog.griddynamics.com/xgboost-vs-catboost-vs-lightgbm-which-is-best-for-price-prediction/)
also claims that LightGMB was the clear winner in terms of speed
and XGBoost was the clear winner in terms of model accuracy.
(However, 
people on Kaggles says that speed is the most important thing in Kaggle competitions
as you can try more features and model iterations 
which eventually lead to higher model accuracy).

> As the table above demonstrates, 
> lightgbm was the clear winner in terms of speed, 
> consistently outperforming catboost and xgboost. 
> In terms of model accuracy, 
> xgboost was the clear winner in both GridSearchCV and RandomizedSearchCV, 
> with the lowest root mean squared error. 
> For early stopping, 
> lightgbm was the winner, 
> with a slightly lower root mean squared error than xgboost.


CatBoost is seldomly used in Kaggle competitions.
LightGBM is faster than XGBoost and is used more and more in Kaggle competitions.
If you need a mature and stable solution,
XGBoost is the right choice.
If you need high speed,
LightGBM is the way to go.

https://www.kaggle.com/c/LANL-Earthquake-Prediction/discussion/89909

https://towardsdatascience.com/catboost-vs-light-gbm-vs-xgboost-5f93620723db

https://datascience.stackexchange.com/questions/49567/lightgbm-vs-xgboost-vs-catboost

https://medium.com/data-design/getting-the-most-of-xgboost-and-lightgbm-speed-compiler-cpu-pinning-374c38d82b86
