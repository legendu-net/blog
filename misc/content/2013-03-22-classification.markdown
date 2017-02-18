UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Classification
Date: 2013-03-22 00:00:00
Tags: CART, machine learning, random forests, statistics, classification, SVM, neuron network, regression
Category: Statistics
Slug: classification
Author: Ben Chuanlong Du

**Things on this page are fragmentary and immature notes/thoughts of the author. It is not meant to readers but rather for convenient reference of the author and future improvement.**
 

## Support Vector Machine (SVM)
The basic version of SVM is a linear separation.
This is obvious since SVM uses a hyperplane to separate data points.
The kenel version (nonlinear transformation) of SVM uses curves/curved surfaces to separate data points.
The Gaussian kenel is a popular choice.
The kenel version (nonlinear transformation) of SVM is good for situations 
where different classes are separated by simple non-linear functions.
Another way to classify non-separable data points is to use the soft margin version.
The soft margin version of SVM is good situations 
whether most data points except a few data points can be separate by a hyperplane.
In this situation it is often a bad idea to use the kenel version (nonlinear transformation).

- The optimization problem in SVM is a quadratic programming problem,
so it's relatively easy to solve.

- SVM is claimed to be one of the most effective classification methods (though debatable). 

- SVM scales well to high dimension data.
Acutally the kenel version of SVM allows it to deal with data of infinite dimensions.

- The expected prediction error is bounded by $\frac{n}{N-1}$,
where $n$ is the number of support vectors 
and $N$ is the number of observations.

- SVM can be generalized to the multi-class problems. 


- Logistic Regression 
Linear separation. 
Logistic Regression is a specially case of the generalized linear regression,
where the response is binary. 
The Newton's algorithm can be used to optimize the likelihood.
Can be generalized to the multi-class classification problem using the multinomial distribution.

- Neuron Network
Use the backpropagation algorithm to learn parameters.
Apply observations 1 by 1, which is a stochastic gradient descent algorithm.
The complexity of Neuron Network is related to the number of nodes in the hidden layers. 

- Tree

- Nearest Neighbour

- Naive Bayesian Classification
Called naive becuase the assumption of conditional independent of covariates given the response variable. 
Despite the assumption is obviously wrong, 
the Naive Bayesian classification is very effective in text mining, 
e.g. predict whether an email is a spam or not. 
The way is works is to carefully select a list of words (according to expert knowledge about whether they can distinguish usually email and spam email or not).
The size of the list is typically around 50,000 (the multinomial approach is nature but have too many parameters, this is why the conditionally independent assumption is used).
Problem arise when words not in the dictionary appears in emails. 
A simple way to add 1 to each category to avoid numerical problems. 
This is caled Laplace smoothing. 
There's actually Bayesian explanation to this Laplace smoothing approach.
It's similar to use priors for parameters. 
This is a very useful trick in many problems though very simple. 

Multivariate Bernoulli Event Model

Another better way is to also take into account of the number of times that each word appears in the email.
This lead to a multivariate multinomial event model.
There are other more complicated models which take into account of order of words in emails,
however, for this specific example, they only do slightly better than the Multivariate Multinomial model mentioned here. 

also a linear classifier, falls into the the category of logistic regression. 

- Linear and Quadratic Discrimination
Linear Discrimation because we use a line or hyper-plane to separate data.
The linear discrimination assumes multinormal which is a very strong assumption and implies a logistic regression model. 
In the contrast logistic regression does not implies linear discrimination. 
Actually, exponential Family distributed given classes also implies a logistic regression.
The reverse is not true.
This means that logistic regression is a very robust assumption. 
The advantage of Linear Discrimination is that with more assumptions, 
less data is needed to fit a "OK" model. 
However, when we have enough data, 
we want to make fewer assumptions and the Linear Discrimination is often not a good choice. 

## Some Tips for Classification

1. Use `-1` and `1` to code classes for binary case instead of `0` and `1`.

2. Do not forget the const/bias variable/feature.

3. Create new variables/features if not many.

4. Select useful variables/features if there are too many.

