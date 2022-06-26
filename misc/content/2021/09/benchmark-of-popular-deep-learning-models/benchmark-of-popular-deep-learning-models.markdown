Status: published
Date: 2021-09-16 11:21:11
Modified: 2021-09-16 13:21:39
Author: Benjamin Du
Slug: benchmark-of-popular-deep-learning-models
Title: Benchmark of Popular Deep Learning Models
Category: Computer Science
Tags: Computer Science, data science, AI, machine learning, deep learning

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Memory 

1. ResNet152 inferencing requies about (a little bit less than) 2G GPU memory
    and training can be done with 8G GPU memory (need to set a small batch size).
    Deeper ResNet cannot be trained with 8G GPU memory.

## Speed

1. Training ResNet 152 on GeForce RTX 3070 8GB is about 15x faster 
    than training it on Intel Core i9-10850K (5.2 GHz Turbo) (20-Thread) (10-Core) 3.6 GHz + 64G memory.

## Accuracy
