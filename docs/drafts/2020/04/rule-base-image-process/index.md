---
title: Rule-base Image Process
created: '2020-04-07T16:29:17-07:00'
date: '2026-11-15T09:23:59-08:00'
authors:
  - bendu
label: rule-base-image-process
license: CC-BY-4.0
tags:
  - computer science
  - image processing
  - computer vision
  - CV
  - machine learning
  - data science
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

If you face a relative simple image recognition problem
which hasn't been studied by other people before
so that no public data is available for it,
it is probably less effort to develop a rule-based algorithm
rather than a complicated (CNN-based) model
(which might require lots of time to collect and label data)
to attack the problem.
Here are some basic tips for developing rule-based algorithms for image processing.

1. Always go for other simpler solutions if image processing is not absolutely necessary.

1. If shape is all that matters in your problem and color doesn't matter,
   it is suggested that you convert images to black/white or grayscale
   and develop your algorithm based on black/white or grayscale images.

1. Direct image pixle comparison is a good idea
   if the (relative) position of the object on the image is fixed/standard,
   otherwise,
   you might want to avoid direct pixle comparison.

1. If both shape and color matters,
   it is usually easier to develop a rule-based algorithm using color information.
