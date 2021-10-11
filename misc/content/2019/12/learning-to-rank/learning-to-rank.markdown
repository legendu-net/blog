Status: published
Date: 2019-12-10 14:27:43
Author: Benjamin Du
Slug: learning-to-rank
Title: Learning to Rank
Category: AI
Tags: AI, data science, machine learning, learning to rank, machine learned ranking, MLR
Modified: 2021-10-08 12:13:57

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

https://www.kaggle.com/c/home-credit-default-risk/discussion/61613

https://studylib.net/doc/18339870/yetirank--everybody-lies

http://proceedings.mlr.press/v14/gulin11a/gulin11a.pdf

<table style="width:100%">
  <tr>
    <th> Model </th>
    <th> Architecture </th>
    <th> Ranking Category </th>
    <th> SOTA </th>
    <th> Comments </th>
    <th> Paper </th>
  </tr>
  <tr>
    <td> RankNet </td>
    <td> NN </td>
    <th> Pairwise </th>
    <td> </td>
    <td> ? </td>
    <td> ? </td>
  </tr>
  <tr>
    <td> LambdaRank </td>
    <td> NN </td>
    <th> Pairwise </th>
    <td> </td>
    <td> ? </td>
    <td> ? </td>
  </tr>
  <tr>
    <td> LambdaMART </td>
    <td> boosted decision trees </td>
    <th> Listwise </th>
    <td> 2010 </td>
    <td> ? </td>
    <td> ? </td>
  </tr>
</table>

[A quick guide to Learning to Rank models](https://practicaldatascience.co.uk/machine-learning/a-quick-guide-to-learning-to-rank-models)

## Tutorials 

https://github.com/sophwats/learning-to-rank

## Neural Network Based Approaches

[PT-RANKING: A BENCHMARKING PLATFORM FOR NEURAL LEARNING-TO-RANK](https://arxiv.org/pdf/2008.13368.pdf)

[Learning to Rank with Deep Neural Networks](https://dial.uclouvain.be/memoire/ucl/fr/object/thesis:4596/datastream/PDF_01/view)

[AN ATTENTION-BASED DEEP NET FOR LEARNING TO RANK](https://openreview.net/pdf?id=BJgxzlSFvr)

[Ranking with Deep Neural Networks](https://www.researchgate.net/publication/322489214_Ranking_with_Deep_Neural_Networks)

[Learning to Rank using Gradient Descent](https://icml.cc/2015/wp-content/uploads/2015/06/icml_ranking.pdf)

[The LambdaLoss Framework for Ranking Metric Optimization](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/1e34e05e5e4bf2d12f41eb9ff29ac3da9fdb4de3.pdf)

[Pairwise Learning to Rank by Neural Networks Revisited: Reconstruction, Theoretical Analysis and Practical Performance](https://ecmlpkdd2019.org/downloads/paper/400.pdf)

[A cross-benchmark comparison of 87 learning to rank methods](https://ris.utwente.nl/ws/portalfiles/portal/6420086/ipm2015-preprint.pdf)

[Fast Attention-based Learning-To-Rank Model for Structured Map Search](https://dl.acm.org/doi/abs/10.1145/3404835.3462904)

[Neural Attention for Learning to Rank Questions in Community Question Answering](https://aclanthology.org/C16-1163.pdf)

https://arxiv.org/pdf/1702.06106.pdf#:~:text=For%20learning%20to%20rank%2C%20neural,search%20results%20as%20the%20input.


## Learning to Rank in LightGBM

https://mlexplained.com/2019/05/27/learning-to-rank-explained-with-code/

https://github.com/microsoft/LightGBM/tree/master/examples/xendcg

https://github.com/microsoft/LightGBM/tree/master/examples/lambdarank

## Learning to Rank in XGBoost

Use the objective `rank:pairwise`

https://www.jianshu.com/p/9caef967ec0a

https://tech.olx.com/ranking-ads-with-machine-learning-ee03d7734bf4

## Benchmark 

[Domain: Learning to Rank](http://www.bigdatalab.ac.cn/benchmark/bm/Domain?domain=Learning%20to%20Rank)

## References

 - [Data for Learning to Rank](http://www.legendu.net/misc/blog/data-for-learning-to-rank)

- [From RankNet to LambdaRank to LambdaMART: An Overview](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf)

- [What is the intuitive explanation of Learning to Rank and algorithms like RankNet, LambdaRank and LambdaMART? In what types of data/variables can these techniques be used? What are their strengths and limitations?
](https://www.quora.com/What-is-the-intuitive-explanation-of-Learning-to-Rank-and-algorithms-like-RankNet-LambdaRank-and-LambdaMART-In-what-types-of-data-variables-can-these-techniques-be-used-What-are-their-strengths-and-limitations)

- https://mlexplained.com/2019/05/27/learning-to-rank-explained-with-code/

- https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418

- https://en.wikipedia.org/wiki/Learning_to_rank

- https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf

- http://times.cs.uiuc.edu/course/598f14/l2r.pdf
