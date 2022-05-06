Status: published
Author: Ben Chuanlong Du
Date: 2013-04-22 12:21:46
Title: Entropy
Slug: entropy
Category: AI
Tags: statistics, AI, entropy, data science, machine learning, deep learning, Shannon entropy, cross entropy, K-L divergence
Modified: 2022-05-04 09:50:54

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Entropy and Related Concepts

1. Entropy
2. Shannon Entropy
3. Cross Entropy
4. K-L divergence

## Tips

1. The entropy concept was first introduced for discrete distributions (called Shannon entropy),
    which is defined as
    $$H(X) = E[log(\frac{1}{f(x)})]$$
    where $X$ stands for a discrete random variable (distribution)
    and $f(x)$ is the probability density function of $X$.
    Shannon Entropy is non-negative.
    It is zero if and only if the discrete distribution is degenerate 
    (all mass concentrate on one point).

2. Shannon entropy is proven to be the lower bound of bits per symbol
    ($log_2(x)$ is used instead of $log(x)$)
    to transfer identifiable information from a source to a destination 
    through a communication channel without data loss. 

3. Shanno entropy is equivalent to entropy in thermodynamics (an area of physics).

3. Entropy is a good metric to measure the magnitude of "information" in features/variables in machine learning.
    It can be used to filter out non-useful features/variables.

4. The entropy concept can be extended to continuous distributions.
    However, 
    the entropy of a continuous distribution can be negative.
    As a matter of fact,
    the entropy of a continuous distribution has a range of $(-\infty, \infty)$.
    Taking the exponential distribution with the density function $\frac{1}{\mu}e^{-\frac{x}{\mu}}$ as example,
    its entropy is $log(\mu)+1$ which goes to $\infty$ as $\mu$ goes to $\infty$ 
    and it goes to $-\infty$ as $\mu$ goes to 0.

5. For the reason in bullet point 4,
    entropy is not a good measure for continuous distributions
    Cross-entropy and K-L divergence are more commonly used for both discrete and continuous distributions.
    The cross-entropy of a distribution q with respect to p is defined as 
    $$H(p, q) = E_p[-log(q)]$$
    And the K-L divergence (also called relative entropy) is defined as
    $$D_{KL}(p, q) = E_p[log(\frac{1}{q}) - log(\frac{1}{p})] = H(p, q) - H(p)$$
    Notice that the K-L divergence is always non-negative.

6. In a multi-class classification problem,
    the following are equivalent.

    - minimizing the cross-entropy 
    - minimizing the K-L divergence
    - maximizing the log likelihood of the corresponding multi-nomial distribution
    - minimizing the negative log likelihood (NLL) of the corresponding multi-nomial distribution

    The above conclusion suggests that the cross-entropy loss, K-L loss and the NLL loss are equivalent.
    However, 
    be aware that PyTorch defines cross-entropy loss to be different from the NLL loss.
    The cross-entropy loss in PyTorch is defined on the raw output of a neural network layer
    while the NLL loss is defined on the output of a log softmax layer.
    This means that in PyTorch the cross-entropy loss is equivalent to log_softmax + nll_loss.

## Misc

Fisher information explanation

likelihood based tests: LRT, wald, score 

expected fisher, 

observed fisher (sum, log, law of large number)

## References

- [A Gentle Introduction to Cross-Entropy for Machine Learning](https://machinelearningmastery.com/cross-entropy-for-machine-learning/)

