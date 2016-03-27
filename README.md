# WhatShouldWeTagMe Auto Tagging Software

A set of binary classifiers for image data. Given an image this program contains a function that maps the image data
of the input and a selected class to a probability measure.

`wswtm` does not include feature location detection so the training data should be data samples centered to the middle
point of each image.

> THIS IS A WORK IN PROGRESS

## Project structure

This is a Maven project with external dependencies.

### FANN Library

A wrapper library is used to make calls to the native FANN library which must be installed on the system.

[FANN Homepage](http://leenissen.dk/fann/wp/)


