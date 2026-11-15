---
title: Object Detection Using Deep Learning
created: '2021-09-20T15:41:42-07:00'
date: '2026-11-15T09:21:47-08:00'
authors:
  - bendu
label: object-detection-using-deep-learning
license: CC-BY-4.0
tags:
  - computer science
  - programming
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Concepts

Image Classification

Image Localization

Image Classification: Predict the type or class of an object in an image.
Input: An image with a single object, such as a photograph.
Output: A class label (e.g. one or more integers that are mapped to class labels).
Object Localization: Locate the presence of objects in an image and indicate their location with a bounding box.
Input: An image with one or more objects, such as a photograph.
Output: One or more bounding boxes (e.g. defined by a point, width, and height).
Object Detection: Locate the presence of objects with a bounding box and types or classes of the located objects in an image.
Input: An image with one or more objects, such as a photograph.
Output: One or more bounding boxes (e.g. defined by a point, width, and height), and a class label for each bounding box.

Image Segmentation
\- Semantic Segmentation
\- Instance segmentation

https://en.wikipedia.org/wiki/Image_segmentation

R-CNN

Fast R-CNN

Faster R-CNN

Mask R-CNN

YoLo

Faster R-CNN Mask R-CNN YoLo

## Models for Object Detection

Region-Based Convolutional Neural Networks, or R-CNNs, are a family of techniques for addressing object localization and recognition tasks, designed for model performance.
You Only Look Once, or YOLO, is a second family of techniques for object recognition designed for speed and real-time use.

## Finetune Object Detection Models in PyTorch

[Fine-tuning Faster-RCNN using pytorch](https://www.kaggle.com/yerramvarun/fine-tuning-faster-rcnn-using-pytorch)

[Beagle Detector: Fine-tune Faster-RCNN](https://haochen23.github.io/2020/06/fine-tune-faster-rcnn-pytorch.html#.YVdUzEbMKdY)

[TORCHVISION OBJECT DETECTION FINETUNING TUTORIAL](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)

## References

[Non-maximum Suppression (NMS)](https://towardsdatascience.com/non-maximum-suppression-nms-93ce178e177c)

[A Gentle Introduction to Object Recognition With Deep Learning](https://machinelearningmastery.com/object-recognition-with-deep-learning/)

[From R-CNN to Mask R-CNN](https://medium.com/@umerfarooq_26378/from-r-cnn-to-mask-r-cnn-d6367b196cfd)

[Mask R-CNN: A Beginner's Guide](https://viso.ai/deep-learning/mask-r-cnn/)

[TORCHVISION OBJECT DETECTION FINETUNING TUTORIAL](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)
