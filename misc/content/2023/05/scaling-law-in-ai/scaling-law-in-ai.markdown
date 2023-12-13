Status: published
Date: 2023-05-10 14:06:11
Modified: 2023-12-12 09:30:40
Author: Benjamin Du
Slug: scaling-law-for-llm
Title: Scaling Law for LLM
Category: Computer Science
Tags: Computer Science, AI, data science, machine learning, scaling law, model

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


Performance depends strongly on scale, weakly on model shape: Model performance depends most
strongly on scale, which consists of three factors: the number of model parameters N (excluding embeddings), the size of the dataset D, and the amount of compute C used for training. Within reasonable limits,
performance depends very weakly on other architectural hyperparameters such as depth vs. width. (Section
3)
Smooth power laws: Performance has a power-law relationship with each of the three scale factors
N, D, C when not bottlenecked by the other two, with trends spanning more than six orders of magnitude
(see Figure 1). We observe no signs of deviation from these trends on the upper end, though performance
must flatten out eventually before reaching zero loss. (Section 3)
Universality of overfitting: Performance improves predictably as long as we scale up N and D in tandem,
but enters a regime of diminishing returns if either N or D is held fixed while the other increases. The
performance penalty depends predictably on the ratio N0.74/D, meaning that every time we increase the
model size 8x, we only need to increase the data by roughly 5x to avoid a penalty. (Section 4)
Universality of training: Training curves follow predictable power-laws whose parameters are roughly
independent of the model size. By extrapolating the early part of a training curve, we can roughly predict the
loss that would be achieved if we trained for much longer. (Section 5)
Transfer improves with test performance: When we evaluate models on text with a different distribution
than they were trained on, the results are strongly correlated to those on the training validation set with
a roughly constant offset in the loss – in other words, transfer to a different distribution incurs a constant
penalty but otherwise improves roughly in line with performance on the training set. (Section 3.2.2)
Sample efficiency: Large models are more sample-efficient than small models, reaching the same level of
performance with fewer optimization steps (Figure 2) and using fewer data points (Figure 4).
Convergence is inefficient: When working within a fixed compute budget C but without any other restrictions on the model size N or available data D, we attain optimal performance by training very large models
and stopping significantly short of convergence (see Figure 3). Maximally compute-efficient training would
therefore be far more sample efficient than one might expect based on training small models to convergence,
with data requirements growing very slowly as D ∼ C
0.27 with training compute. (Section 6)
Optimal batch size: The ideal batch size for training these models is roughly a power of the loss only,
and continues to be determinable by measuring the gradient noise scale [MKAT18]; it is roughly 1-2 million
tokens at convergence for the largest models we can train. (Section 5.1)
Taken together, these results show that language modeling performance improves smoothly and predictably
as we appropriately scale up model size, data, and compute. We expect that larger language models will
perform better and be more sample efficient than current models.


[Beyond neural scaling laws – Paper Explained](https://www.youtube.com/watch?v=joZaCw5PxYs)


Scaling Laws refer to the observed trend of some machine learning architectures (notably transformers) to scale their performance on predictable power law when given more compute, data, or parameters (model size), assuming they are not bottlenecked on one of the other resources. This has been observed as highly consistent over more than six orders of magnitude.

Scaling Laws Literature Review
https://epochai.org/blog/scaling-laws-literature-review#:~:text=The%20term%20%E2%80%9Cscaling%20laws%E2%80%9D%20in,width%2C%20or%20training%20compute).

Database of Scaling Laws
https://docs.google.com/spreadsheets/d/1XHU0uyCojH6daSWEq9d1SHnlrQVW7li8iqBMasawMns/edit#gid=0

## Training Large NNs

- pruning

- scaling 

[Beyond neural scaling laws – Paper Explained](https://www.youtube.com/watch?v=joZaCw5PxYs)

[WHY AND HOW OF SCALING LARGE LANGUAGE MODELS | NICHOLAS JOSEPH](https://www.youtube.com/watch?v=qscouq3lo0s)

## References

- [Jared Kaplan | Scaling Laws and Their Implications for Coding AI](https://www.youtube.com/watch?v=Suhp3OLASSo)

- [Beyond neural scaling laws: beating power law scaling via data pruning](https://arxiv.org/abs/2206.14486)

- [WHY AND HOW OF SCALING LARGE LANGUAGE MODELS | NICHOLAS JOSEPH](https://www.youtube.com/watch?v=qscouq3lo0s)


- [Scaling Laws for Neural Language Models](https://arxiv.org/pdf/2001.08361.pdf)

