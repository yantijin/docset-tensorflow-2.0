<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.sigmoid" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.sigmoid

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/activations.py">View source</a>



<!-- Start diff -->
Sigmoid.

### Aliases:

* `tf.compat.v1.keras.activations.sigmoid`
* `tf.compat.v2.keras.activations.sigmoid`


``` python
tf.keras.activations.sigmoid(x)
```



<!-- Placeholder for "Used in" -->

Applies the sigmoid activation function. The sigmoid function is defined as
1 divided by (1 + exp(-x)). It's curve is like an "S" and is like a smoothed
version of the Heaviside (Unit Step Function) function. For small values
(<-5) the sigmoid returns a value close to zero and for larger values (>5)
the result of the function gets close to 1.
Arguments:
    x: A tensor or variable.

#### Returns:

A tensor.

Sigmoid activation function.

#### Arguments:


* <b>`x`</b>: Input tensor.


#### Returns:

The sigmoid activation: `(1.0 / (1.0 + exp(-x)))`.
