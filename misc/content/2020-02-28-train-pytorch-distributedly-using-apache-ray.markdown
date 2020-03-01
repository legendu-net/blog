Status: published
Date: 2020-02-29 21:03:42
Author: Benjamin Du
Slug: train-pytorch-distributedly-using-apache-ray
Title: Train PyTorch Distributedly Using Apache Ray
Category: AI
Tags: AI, data science, machine learning, deep learning, PyTorch, distributed, Apache Ray

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Training a Model Implemented in PyTorch

https://github.com/ray-project/ray/tree/master/python/ray/util/sgd/pytorch/examples

[Distributed PyTorch Using Apache Ray](https://ray.readthedocs.io/en/latest/raysgd/raysgd_pytorch.html)

[RaySGD: Distributed Training Wrappers](https://ray.readthedocs.io/en/latest/raysgd/raysgd.html)


## Hyperparameter Optimization for Models Implemented in PyTorch

https://ray.readthedocs.io/en/latest/tune-examples.html

Is the following example running distributed or not?
Do I need to use tags to tell Ray to run it on multiple machines?

```
import torch.optim as optim
from ray import tune
from ray.tune.examples.mnist_pytorch import (
    get_data_loaders, ConvNet, train, test)


def train_mnist(config):
    train_loader, test_loader = get_data_loaders()
    model = ConvNet()
    optimizer = optim.SGD(model.parameters(), lr=config["lr"])
    for i in range(10):
        train(model, optimizer, train_loader)
        acc = test(model, test_loader)
        tune.track.log(mean_accuracy=acc)


analysis = tune.run(
    train_mnist, config={"lr": tune.grid_search([0.001, 0.01, 0.1])})

print("Best config: ", analysis.get_best_config(metric="mean_accuracy"))

# Get a dataframe for analyzing trial results.
df = analysis.dataframe()
```

## References

https://github.com/ray-project/ray/issues/3609

https://github.com/ray-project/ray/issues/3520

[Accelerating Deep Learning Using Distributed SGD — An Overview](https://towardsdatascience.com/accelerating-deep-learning-using-distributed-sgd-an-overview-e66c4aee1a0c)

[Distributed training of Deep Learning models with PyTorch](https://medium.com/intel-student-ambassadors/distributed-training-of-deep-learning-models-with-pytorch-1123fa538848)

https://github.com/dmmiller612/sparktorch

[Awesome Distributed Deep Learning](https://github.com/bharathgs/Awesome-Distributed-Deep-Learning)

[Intro to Distributed Deep Learning Systems](https://medium.com/@Petuum/intro-to-distributed-deep-learning-systems-a2e45c6b8e7)

[Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour](https://arxiv.org/pdf/1706.02677.pdf)
