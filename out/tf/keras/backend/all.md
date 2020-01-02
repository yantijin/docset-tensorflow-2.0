<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.all" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.all

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Bitwise reduction (logical AND).

### Aliases:

* `tf.compat.v1.keras.backend.all`
* `tf.compat.v2.keras.backend.all`


``` python
tf.keras.backend.all(
    x,
    axis=None,
    keepdims=False
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`axis`</b>: axis along which to perform the reduction.
* <b>`keepdims`</b>: whether the drop or broadcast the reduction axes.


#### Returns:

A uint8 tensor (0s and 1s).
