---
title: Tips on AutoGluon
created: '2020-01-27T15:28:00-08:00'
date: '2026-11-15T09:21:33-08:00'
authors:
  - bendu
label: tips-on-autogluon
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - AutoGluon
  - AutoML
  - deep learning
  - ENAS
  - ProxylessNAS
  - gluon
  - MXNet
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://github.com/awslabs/autogluon

https://autogluon.mxnet.io/

AutoGluon automatically inferences the problem type.
However,
you are still able to specify the problem type
if AutoGluon fails to infer the right problem type.

1. AutoGluon auto saves all models into the specified output directory during training.
   And the save models can be load back using the `load` method of the corresponding predictor.

1. GPU support in AutoGluon is for image/text but not Tabular data currently.
   For more details,
   please refer to
   [issue 262](https://github.com/awslabs/autogluon/issues/262).

## Questions

Can I choose a model to save and choose a model to load?

## Customization

[Search Space and Decorator](https://autogluon.mxnet.io/tutorials/course/core.html)

[Search Algorithms](https://autogluon.mxnet.io/tutorials/course/algorithm.html)

[Customize User Objects](https://autogluon.mxnet.io/tutorials/course/object.html)

[Customize Training Script](https://autogluon.mxnet.io/tutorials/course/script.html)

## Hyperparameter Tuning

[Use AutoGluon for Hyperparameter Optimization for MNIST Training in PyTorch](https://autogluon.mxnet.io/tutorials/torch/hpo.html)

## Neural Architecture Search

https://autogluon.mxnet.io/tutorials/nas/enas_mnist.html

## References

https://futurumresearch.com/aws-releases-autogluon-an-innovative-open-source-tooling-for-automated-machine-learning/

https://www.amazon.science/amazons-autogluon-helps-developers-get-up-and-running-with-state-of-the-art-deep-learning-models-with-just-a-few-lines-of-code

https://towardsdatascience.com/autogluon-deep-learning-automl-5cdb4e2388ec

https://venturebeat.com/2020/01/09/amazons-autogluon-produces-ai-models-with-as-little-as-three-lines-of-code/

https://autogluon.mxnet.io/tutorials/course/distributed.html
