Status: published
Date: 2013-03-07 11:12:36
Author: Ben Chuanlong Du
Title: Loss Functions for Machine Learning Models
Slug: ai-loss-function
Category: AI
Tags: AI, loss function, statistics, machine learning, cross entry, log likelihood
Modified: 2022-05-08 16:26:29

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**
 
## Tips and Traps

1. A Loss function is always non-negative. 
    If you get a negative loss when training a model,
    there must be something wrong with the code. 
    For example, 
    maybe you chosed a loss function incorrectly.

## Loss Functions

### 0-1 Loss 

Or sometimes called binary loss function.

### SSE

### Cross-entropy

### Negative Log Likelihood

## Comparisons of Loss Functions

### Cross Entropy vs Negative Log Likelihood

Please refer to
[Entropy](https://www.legendu.net/misc/blog/entropy)
for detailed discussions.

### MSE (L2 Loss) vs L1 Loss

MSE is a L2 loss function. 
Both L1 and L2 loss functions are special cases of $L_p$ ($p>0$) loss functions.
$L_p$ loss functions are typicall used for regression problems.
Compared to L1 loss, 
L2 loss gives larger weights on larger (absolute) errors.
In many real applications, 
we often observe the following 2 phenomena.
    1. Real/training data is not uniformly distribution across all scenarios.
        There are often a lot more samples which generate small respoonse values. 
    2. During training, large response values often have larger errors.
If samples generating larger response values (errors)
are not important (or can be treated as outliers)
then a L1 loss (or even $L_p$ where $0<p<1$) is a better choice than a L2 loss.
If samples generating larger response values (errors)
cannot be treated as outliers 
or even more important, 
then a L2 loss (or even $L_p$ where $p>1$) is better than a L1 loss.

## Loss Functions in PyTorch

nn.CrossEntropyLoss

[nn.NLLLoss](https://pytorch.org/docs/stable/nn.html#nllloss)

https://discuss.pytorch.org/t/what-is-the-difference-between-using-the-cross-entropy-loss-and-using-log-softmax-followed-by-nll-loss/14825

https://discuss.pytorch.org/t/build-your-own-loss-function-in-pytorch/235

https://medium.com/udacity-pytorch-challengers/a-brief-overview-of-loss-functions-in-pytorch-c0ddb78068f7

## References

https://pytorch.org/docs/stable/nn.html

[PyTorch Loss Functions: The Ultimate Guide](https://neptune.ai/blog/pytorch-loss-functions)

https://gombru.github.io/2019/04/03/ranking_loss/

https://discuss.pytorch.org/t/writing-warp-loss-layer/3715

