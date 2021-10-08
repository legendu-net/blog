Status: published
Date: 2013-03-07 11:12:36
Author: Ben Chuanlong Du
Title: Loss Functions in Machine Learning Models
Slug: ai-loss-function
Category: AI
Tags: AI, loss function, statistics, machine learning, cross entry, log likelihood
Modified: 2021-10-07 16:57:25

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
## Tips and Traps

1. Loss is non-negative. 
    If you get a negative loss during your training,
    there must be something wrong with your code. 
    For example, 
    maybe you choosed a loss function incorrectly.

## Loss Functions

### 0-1 Loss 

Or sometimes called binary loss function.

### SSE

### Entropy

### Likelihood Function

To make the loss function convex so that optimization is easy.


https://gombru.github.io/2019/04/03/ranking_loss/


https://discuss.pytorch.org/t/writing-warp-loss-layer/3715

## Comparisons of Loss Functions

### Cross Entropy vs Negative Log Likelihood

The cross entropy loss function is the negative log likelihood loss function 
applied on softmax output.
So, 
if the last layer of your neural network is a softmax layer
you want to use the negative log likelihood loss function 
(instead of the cross entropy loss function);
and if the last layer of your neural network is a full-connected layer 
(without applying softmax)
yu wantto use the cross entropy loss function.

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
