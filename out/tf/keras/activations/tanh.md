<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.tanh" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.tanh

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/activations.py">View source</a>



<!-- Start diff -->
Hyperbolic Tangent (tanh) activation function.

### Aliases:

* `tf.compat.v1.keras.activations.tanh`
* `tf.compat.v2.keras.activations.tanh`


``` python
tf.keras.activations.tanh(x)
```



<!-- Placeholder for "Used in" -->


#### For example:



```python
# Constant 1-D tensor populated with value list.
a = tf.constant([-3.0,-1.0, 0.0,1.0,3.0], dtype = tf.float32)
b = tf.keras.activations.tanh(a) #[-0.9950547,-0.7615942,
0.,0.7615942,0.9950547]
```
Arguments:
    x: Input tensor.

#### Returns:

A tensor of same shape and dtype of input `x`.
The tanh activation: `tanh(x) = sinh(x)/cosh(x) = ((exp(x) -
exp(-x))/(exp(x) + exp(-x)))`.
