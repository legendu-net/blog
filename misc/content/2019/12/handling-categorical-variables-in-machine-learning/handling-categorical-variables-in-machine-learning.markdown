Status: published
Date: 2019-12-24 10:44:18
Author: Benjamin Du
Slug: handling-categorical-variables-in-machine-learning
Title: Handling Categorical Variables in Machine Learning
Category: AI
Tags: AI, machine learning, data science, categorical variables, encoding, One-hot
Modified: 2022-03-26 22:21:23

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Categorical variables are very common in a machine learning project.
On a high level,
there are two ways to handle a categorical variable.

1. Drop a categorical variable 
    if a categorical variable won't help the model 
    and especially when the categorical variable has a large cardinality.
    User id is such an example
    when you build a user-level model.
    Of course,
    you can use feature hashing to reduce the dimension/cardinality of a categorical variable,
    and let the training process decides 
    whether the categorical variable should be included into the model or not.

2. Encode a categorical variable. 
    Below are some popular ways of encoding a categorical variable.

        - One-Hot Encoding
        - Label Encoding
        - Target Encoding
        - Feature Hashing
        - Weight of Evidence
        - Light G-Boost Encoding

    Please refer to 
    [Know about Categorical Encoding, even New Ones!](https://towardsdatascience.com/know-about-categorical-encoding-even-new-ones-c266227b9cbd)
    and
    [Dealing with Categorical Variables in Machine Learning](https://medium.com/swlh/dealing-with-categorical-variables-in-machine-learning-4401b949b093)
    for more detailed discussions.
    Notice that LightGBM has it's own way (Light G-Boost Encoding)
    of handling categorical variables.
    Please refer to
    [Handle Categorical Variables in LightGBM](http://www.legendu.net/misc/blog/handle-categorical-variables-in-lightgbm)
    for more discussions
    .

## References

- [Know about Categorical Encoding, even New Ones!](https://towardsdatascience.com/know-about-categorical-encoding-even-new-ones-c266227b9cbd)

- [Dealing with Categorical Variables in Machine Learning](https://medium.com/swlh/dealing-with-categorical-variables-in-machine-learning-4401b949b093)

