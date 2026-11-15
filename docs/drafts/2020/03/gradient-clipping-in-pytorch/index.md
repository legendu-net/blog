---
title: Gradient Clipping in PyTorch
created: '2020-03-04T16:12:45-08:00'
date: '2026-11-15T12:20:37-08:00'
authors:
  - bendu
label: gradient-clipping-in-pytorch
license: CC-BY-4.0
tags:
  - programming
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```
:::python
optimizer.zero_grad()        
output = model(data)
loss = F.nll_loss(output, target)
loss.backward()
torch.nn.utils.clip_grad_norm_(model.parameters(), args.clip)
optimizer.step()
```

1. Use `torch.nn.utils.clips_grad_norm_` (which is in-place)
   instead of `torch.nn.utils.clips_grad_norm` (which returns a copy and has been deprecated).

## References

https://discuss.pytorch.org/t/proper-way-to-do-gradient-clipping/191

[About torch.nn.utils.clip_grad_norm](https://discuss.pytorch.org/t/about-torch-nn-utils-clip-grad-norm/13873)

[How to do gradient clipping in pytorch?](https://stackoverflow.com/questions/54716377/how-to-do-gradient-clipping-in-pytorch)
