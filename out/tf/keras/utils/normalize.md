<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.normalize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.normalize

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/utils/np_utils.py">View source</a>



<!-- Start diff -->
Normalizes a Numpy array.

### Aliases:

* `tf.compat.v1.keras.utils.normalize`
* `tf.compat.v2.keras.utils.normalize`


``` python
tf.keras.utils.normalize(
    x,
    axis=-1,
    order=2
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Numpy array to normalize.
* <b>`axis`</b>: axis along which to normalize.
* <b>`order`</b>: Normalization order (e.g. 2 for L2 norm).


#### Returns:

A normalized copy of the array.
