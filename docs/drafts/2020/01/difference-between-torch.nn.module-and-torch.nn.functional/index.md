---
title: Difference between torch.nn.Module and torch.nn.functional
created: '2020-01-07T11:26:38-08:00'
date: '2026-08-11T22:19:27-07:00'
authors:
  - bendu
label: difference-between-torch.nn.module-and-torch.nn.functional
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - PyTorch
  - torch.nn.Module
  - torch.nn.functional
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Modules in `torch.nn` are internal implemented based on `torch.nn.functional`.
Modules in `torch.nn` are easier to use while `torch.nn.functional` is more flexible.
It is recommended to use `nn.Conv2d` because it uses the `nn.Module` abstraction
and nicely ties into the torch.optim framework well.

Based on my understanding,
it is always safe to use modules in torch.nn if available
and it is suggested that you do it this way.
However,
for modules/layers that do not have parameters to optimize,
you can also use the functional equivalence (which is the underlying implementation of the modules/layers).

Similarly for loss functions.

## References

https://discuss.pytorch.org/t/what-is-the-difference-between-torch-nn-and-torch-nn-functional/33597

https://discuss.pytorch.org/t/how-to-choose-between-torch-nn-functional-and-torch-nn-module/2800

https://discuss.pytorch.org/t/what-is-the-difference-between-torch-nn-and-torch-nn-functional/33597

https://discuss.pytorch.org/t/beginner-should-relu-sigmoid-be-called-in-the-init-method/18689

https://stackoverflow.com/questions/54662984/pytorch-why-loss-functions-are-implemented-both-in-nn-modules-loss-and-nn-funct
