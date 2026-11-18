# Temporal Convolutional Network Architecture

## Rationale
A Temporal Convolutional Network applies one-dimensional convolutions to ordered sequences. Causal convolutions prevent an output at a time step from depending on future inputs. Dilated convolutions expand the receptive field without requiring a correspondingly deep stack of ordinary convolutions.

These properties make TCNs a candidate architecture for learning patterns in time-ordered electricity-consumption data.

## Architecture details to report
The final implementation should state:
- number of TCN blocks;
- filters per convolution;
- kernel size and dilation rates;
- padding and causal-convolution configuration;
- activation functions and regularization;
- output layer and activation;
- optimizer, learning rate, and loss function.

## Configuration explored
A configuration discussed in the research notebooks uses 64 filters, kernel size 3, dilation rates [1, 2, 4, 8], and a sigmoid output for binary classification.

This records a configuration explored in draft notebooks; it is not a claim that this is the final validated model. Confirm it against the reproducible training run.

## Input and output
Document the input shape (samples, time steps, features) and the exact meaning and encoding of the binary target label.

## Framework
The draft notebooks include TensorFlow/Keras model code. The final codebase should use one consistent framework and list its tested version.
