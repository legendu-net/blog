Status: published
Date: 2020-08-24 12:29:58
Author: Benjamin Du
Slug: visualization-for-ai-concepts
Title: Visualization for AI Concepts
Category: Computer Science
Tags: Computer Science, AI, concept, visualization, data science, machine learning, shap, visual, design, neural network, deep learning
Modified: 2021-09-24 23:11:26

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Tools for (approximately) visualizing the architures of existing neural networks
or for visualizing the traing process (training/validation loss/accuracy, activation, etc.)
are extremely helpful!
TensorBoard is one of the best tools for this purpose.
However,
I personally don't think visual neural network design platforms/frameworks are of any practical value.
The reason is that average users won't care that much about the architecture design of neural networks,
but instead they just use pretrained models or fine tune them.
When users (mainly researchers) need to twist the architecture of an existing neural work
or design an new neural network,
visual neural network design tools are not able to provide the kind of customization and control of complicated neural network architectures. 
It would much easier to customize or design a neural network using coding.

## Use TensorBoard to Visualize PyTorch Training Process

Even though TensorBoard was develop for TensorFlow in the beginning,
it can also be used with PyTorch. 

[Visualizing Models, Data, and Training with Tensorboard](https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html)

[torch.utils.tensorboard](https://pytorch.org/docs/stable/tensorboard.html?highlight=tensorboard)

### Add Non-matplotlib Figures

1. Make a plot use your favorite visualization library.
2. Save the plot to a PNG image.
3. Load the image. 
4. Add it to TensorBoard using `SummaryWriter.add_image`.

### ModuleNotFoundError: No module named 'past'

When you call `SummaryWriter.add_graph` to add a graph to TensorBoard, 
it might throw the error "ModuleNotFoundError: No module named 'past'"
due to a few causes.
One case of the error that I encounted was due to passing an object which is not a PyTorch model.
The object was a customized trainer class which wraps a model. 
Pass the innter wrapped model to `SummaryWriter.add_graph` solved the problem.

### Customize TensorBoard 

The article [Read TensorBoard Logs](http://www.legendu.net/misc/blog/read-tensorboard-logs)
demonstrate a few ways to read TensorBoard logs 
(for generating customized visualization).
The issue
[A more customizable and interactive TensorBoard](https://github.com/tensorflow/tensorboard/issues/5333)
in the TensorBoard GitHub repository 
propose to make TensorBoard more customizable and interactive.

## Other Useful Visualization Tools

1. [A Visual Production to Probability and Statistics](https://seeing-theory.brown.edu/)

2. [slundberg/shap](https://github.com/slundberg/shap)
    is a Python library 
    providing a unified approach to explain the output of any machine learning model.

3. [ResidentMario/missingno](https://github.com/ResidentMario/missingno)
    is a Python library 
    for missing data visualization.


## Alternative Visual AI Tools

1. [Nvidia Digits](https://developer.nvidia.com/digits)

2. [visdom](https://github.com/fossasia/visdom) 
    is a flexible tool for creating, organizing, and sharing visualizations of live, rich data. 
    It supports Torch and Numpy.

3. [Deep Learning Studio](https://deepcognition.ai/deep-learning-studio/)
    let users build AI deep learning models without coding.

4. [Design, Train & Share AI Models from your browser](https://aifiddle.io/)

5. [PrototypeML](https://prototypeml.com/)
    is a powerful & intuitive visual neural network design platform for PyTorch.

## Python Libraries

### [pydot/pydot](https://github.com/pydot/pydot)

## References

[Exploring Neural Networks with Activation Atlases](https://distill.pub/2019/activation-atlas/)

[Tools to Design or Visualize Architecture of Neural Network](https://github.com/ashishpatel26/Tools-to-Design-or-Visualize-Architecture-of-Neural-Network)

[Nvidia Digits](https://developer.nvidia.com/digits)
