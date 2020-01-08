Status: published
Date: 2020-01-07 16:05:35
Author: Benjamin Du
Slug: tips-on-nlp
Title: Tips on NLP
Category: AI
Tags: AI, machine learning, data science, NLP, nature language processing

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Overview of NLP

[Deep Learning for NLP: An Overview of Recent Trends](https://medium.com/dair-ai/deep-learning-for-nlp-an-overview-of-recent-trends-d0d8f40a776d)

https://nlpoverview.com/

## Semantics vs Syntactic

https://medium.com/huggingface/learning-meaning-in-natural-language-processing-the-semantics-mega-thread-9c0332dfe28e

## Coreferences

https://medium.com/huggingface/state-of-the-art-neural-coreference-resolution-for-chatbots-3302365dcf30

https://huggingface.co/coref/

https://github.com/huggingface/neuralcoref

## Machine Translation 

Transformer

In machine translation, 
self-attention also contributes to impressive results. 
For example, 
recently a model, named Transformer, 
was introduced in a paper with a rather bold title “Attention Is All You Need” [Vaswani, 2017]. 
As you can guess, 
this model relies only on self-attention without the use of RNNs. 
As a result, 
it is highly parallelizable and requires less time to train, while establishing state-of-the-art results on WMT2014.

## seq2seq 

https://github.com/IBM/pytorch-seq2seq


## Attention

The article [Attention in NLP](https://medium.com/@joealato/attention-in-nlp-734c6fa9d983)
has a very detailed summary of development and applications of Attention in NLP.


## Libraries 

[gensim](https://github.com/RaRe-Technologies/gensim)

[transformers](https://github.com/huggingface/transformers)
(formerly known as pytorch-transformers and pytorch-pretrained-bert) 
provides state-of-the-art general-purpose architectures (BERT, GPT-2, RoBERTa, XLM, DistilBert, XLNet, CTRL...) 
for Natural Language Understanding (NLU) and Natural Language Generation (NLG) 
with over 32+ pretrained models in 100+ languages and deep interoperability between TensorFlow 2.0 and PyTorch.


## References

https://github.com/huggingface/transformers
