---
title: Preparing Data for AI
created: '2020-03-17T11:27:12-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: preparing-data-for-ai
license: CC-BY-4.0
tags:
  - computer science
  - data science
  - AI
  - machine learning
  - deep learning
  - data labeling
  - crowdsourcing
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## General Tips

1. When you label individual images,
   it is better to use numerical labels
   (even though text labels are easier to understand)
   so that you can avoid mapping between numbers (use for training)
   and text labels (for human understanding) all the time.

1. If you have no labeled data to start at all,
   do NOT hurry to jumping into labeling yet.
   Check the article
   [Label Image Data Quickly Without Crowdsourcing](label-image-data-quickly-without-crowdsourcing)
   to see whether you can use any of the tips to ease the work of human labeling.

## Free Labeling Tools

- [LabelStudio](https://labelstud.io/)
  [LabelStudio](https://labelstud.io/)
  is the most flexible open source data annotation tool.
  It lets you label data types like audio, text, images, videos, and time series
  with a simple and straightforward UI and export to various model formats.
  The UI supports customization and pre-built labeling templates.

- [LabelMe](http://labelme2.csail.mit.edu/Release3.0/index.php?message=1)
  [LabelMe](http://labelme2.csail.mit.edu/Release3.0/index.php?message=1)
  provides an online annotation tool to build image databases for computer vision research.

- [DiffGram](https://diffgram.com/main/)
  [DiffGram](https://diffgram.com/main/)
  is opensource and thus free for a self-hosted service.

## Commercial Labeling Tools/Platforms

[DiffGram](https://diffgram.com/main/)

Appen

CrowdFlower

https://www.alegion.com/

[Baidu Crowd Outsourcing](https://zhongbao.baidu.com/mark/home/index)

## References

[Labeling Data for AI](preparing-data-for-ai)
