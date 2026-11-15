---
title: Don't Do Statistics If You Don't Really Understand It
created: '2015-04-10T07:50:16-07:00'
date: '2026-11-15T09:20:28-08:00'
authors:
  - bendu
label: don-t-do-statistics-if-you-don-t-really-undestand-it
license: CC-BY-4.0
tags:
  - Statistics
  - independence
  - linear model
  - linear regression
  - hypothesis test
  - Ljung-Box test
---

<img src="/media/statistics/lie.jpg" height="200" width="240" align="right"/>

> Lies, damned lies, and statistics.

As a statistician I'm very glad to see
that statistics is being widely used in many areas.
However,
time after time I found that it is really dangerous
for people who don't really understand statistics to use it.
As we all know that there are 3 basic assumptions in linear regression:
independency, normality and homoscedasticity.
However, not many people really understand what these assumptions mean.
For example,
most people don't know that an "independency" test is actually with respect to some "order".
For human beings, there are 2 nature orders: time
(for which people developed time series analysis)
and space (for which people developed spatial analysis).
While we test for "independency",
mostly of the time we test for "independency" with respect to time.
Here comes the problem.
Many people do simple linear regression,
and they are "smart" enough to remember to check assumptions of linear regression.
Many people use some kind of test statistics
(e.g., the Ljung-Box test statistics) to help them
especially when there are many model candidates.
Not many of them realized that this test is probably meaningless
as they are actually testing "independency" with respect to the order of observations.
But what if I reorder the observations
(in linear regression there's usually no chronological order among observations)?
This can obviously change the decision of the "independency" test.
For example,
if I reorder the observations according the magnitude of the residuals
the Ljung-Box test will obviously be significant
and reject the null hypothesis of "independency";
and if I randomize the order of observations,
the Ljung-Box test will probably be non-significant
and fail to reject the null hypothesis of "independency".
Keep in mind that an "independency" test is with respect to some "order",
e.g., time, space or some nature grouping.
Be sure that you are not testing "independency" with respect to some meaningless order.
