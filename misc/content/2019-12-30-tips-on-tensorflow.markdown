Status: published
Date: 2020-01-06 00:47:18
Author: Benjamin Du
Slug: tips-on-tensorflow
Title: Tips on Tensorflow
Category: AI
Tags: AI, data science, machine learning, TensorFlow, GPU

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Installation

The article
[Stop Installing Tensorflow using pip for performance sake!](https://towardsdatascience.com/stop-installing-tensorflow-using-pip-for-performance-sake-5854f9d9eb0c)
suggest installing TensorFlow using conda instead of pip
as the version installed by conda leverages Intel Math Kernel Library and is about 8 times faster overall speaking.


## GPU Runs Out of Memory

https://stackoverflow.com/questions/36927607/how-can-i-solve-ran-out-of-gpu-memory-in-tensorflow

https://stackoverflow.com/questions/34199233/how-to-prevent-tensorflow-from-allocating-the-totality-of-a-gpu-memory

https://superuser.com/questions/980216/what-happens-when-the-gpu-memory-is-not-enough
