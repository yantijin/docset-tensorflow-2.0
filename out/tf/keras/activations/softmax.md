<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.softmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.softmax

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/activations.py">View source</a>



<!-- Start diff -->
The softmax activation function transforms the outputs so that all values are in

### Aliases:

* `tf.compat.v1.keras.activations.softmax`
* `tf.compat.v2.keras.activations.softmax`


``` python
tf.keras.activations.softmax(
    x,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->

range (0, 1) and sum to 1. It is often used as the activation for the last
layer of a classification network because the result could be interpreted as
a probability distribution. The softmax of x is calculated by
exp(x)/tf.reduce_sum(exp(x)).

#### Arguments:


* <b>`x`</b>: Input tensor.
* <b>`axis`</b>: Integer, axis along which the softmax normalization is applied.


#### Returns:

Tensor, output of softmax transformation (all values are non-negative
  and sum to 1).



#### Raises:


* <b>`ValueError`</b>: In case `dim(x) == 1`.