Status: published
Date: 2020-02-27 20:11:55
Author: Benjamin Du
Slug: tips-on-apache-ray
Title: Tips on Apache Ray
Category: Programming
Tags: programming, Apache Ray, distributed computing

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Deploy Apache Ray

Please refer to 
[Deploy Apache Ray](http://www.legendu.net/misc/blog/deploy-apache-ray/)
for details.

## Tutorials and Examples

[How to scale Python multiprocessing to a cluster with one line of code](https://medium.com/distributed-computing-with-ray/how-to-scale-python-multiprocessing-to-a-cluster-with-one-line-of-code-d19f242f60ff)
demonstrates how you can scale a Python multiprocess application 
to run an Apache Ray cluster 
with only one line change of your code 
(change `import multiprocessing.Pool` to `ray.util.multiprocessing.Pool`).


## References

[Fault Tolerance](https://ray.readthedocs.io/en/latest/fault-tolerance.html#fault-tolerance)

[Development Tips](https://ray.readthedocs.io/en/latest/development.html)

[RaySGD: Distributed Training Wrappers](https://ray.readthedocs.io/en/latest/raysgd/raysgd.html)

[Distributed Iterators](https://ray.readthedocs.io/en/latest/iter.html)

[Distributed Scikit-learn / Joblib](https://ray.readthedocs.io/en/latest/joblib.html)

[https://ray.readthedocs.io/en/latest/multiprocessing.html](Distributed multiprocessing.Pool)

[Distributed PyTorch Using Apache Ray](https://ray.readthedocs.io/en/latest/raysgd/raysgd_pytorch.html)

https://github.com/ParallelSSH/parallel-ssh

https://ray.readthedocs.io/en/latest/walkthrough.html#remote-functions-tasks

https://arrow.apache.org/docs/python/plasma.html#the-plasma-in-memory-object-store

https://readthedocs.org/projects/ray/downloads/pdf/latest/

https://ray.readthedocs.io/en/latest/package-ref.html

https://towardsdatascience.com/benchmarking-python-distributed-ai-backends-with-wordbatch-9872457b785c

https://ray.readthedocs.io/en/latest/tune.html

https://ray.readthedocs.io/en/latest/rllib.html
