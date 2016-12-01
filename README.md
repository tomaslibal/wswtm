# WhatShouldWeTagMe Auto Tagging Software

Given an image this program contains a function that maps the image data of the input to text labels which represent some probabilistically inferred possible labels.

> THIS IS A WORK IN PROGRESS

## Use the library

```python

from wswtm import wswtm

tagger = wswtm()
tags = tagger.image2tags('/some/image/path.png')

print tags

[('flower', 0.9), ('petals', 0.87), ('orchid', 0.71)]

```

## Dependencies

- See the [requirements.txt](requirements.txt) file for Python requirements.
- Python 2.7
- pip

## Project structure

This is a Python 2.7 project with external dependencies. The program is essentially an infrastructure for feeding labelled pixel data to a Keras model, training the model, saving the trained model into `json` and `hdf5` output, loading a trained Keras model, and evaluating new data using the loaded model.




