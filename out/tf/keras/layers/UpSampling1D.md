<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.UpSampling1D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.layers.UpSampling1D

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/layers/convolutional.py">View source</a>



## Class `UpSampling1D`

<!-- Start diff -->
Upsampling layer for 1D inputs.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

### Aliases:

* Class `tf.compat.v1.keras.layers.UpSampling1D`
* Class `tf.compat.v2.keras.layers.UpSampling1D`


<!-- Placeholder for "Used in" -->

Repeats each temporal step `size` times along the time axis.

#### Arguments:


* <b>`size`</b>: Integer. Upsampling factor.


#### Input shape:

3D tensor with shape: `(batch, steps, features)`.



#### Output shape:

3D tensor with shape: `(batch, upsampled_steps, features)`.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="/code/stable/tensorflow/python/keras/layers/convolutional.py">View source</a>

``` python
__init__(
    size=2,
    **kwargs
)
```






