<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.squeeze" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.squeeze

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Removes a 1-dimension from the tensor at index "axis".

### Aliases:

* `tf.compat.v1.keras.backend.squeeze`
* `tf.compat.v2.keras.backend.squeeze`


``` python
tf.keras.backend.squeeze(
    x,
    axis
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: Axis to drop.


#### Returns:

A tensor with the same data as `x` but reduced dimensions.
