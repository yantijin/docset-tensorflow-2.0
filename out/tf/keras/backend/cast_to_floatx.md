<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.cast_to_floatx" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.cast_to_floatx

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Cast a Numpy array to the default Keras float type.

### Aliases:

* `tf.compat.v1.keras.backend.cast_to_floatx`
* `tf.compat.v2.keras.backend.cast_to_floatx`


``` python
tf.keras.backend.cast_to_floatx(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Numpy array or TensorFlow tensor.


#### Returns:

The same array (Numpy array if `x` was a Numpy array, or TensorFlow tensor
if `x` was a tensor), cast to its new type.



#### Example:


```python
    >>> from tensorflow.keras import backend as K
    >>> K.floatx()
    'float32'
    >>> arr = numpy.array([1.0, 2.0], dtype='float64')
    >>> arr.dtype
    dtype('float64')
    >>> new_arr = K.cast_to_floatx(arr)
    >>> new_arr
    array([ 1.,  2.], dtype=float32)
    >>> new_arr.dtype
    dtype('float32')
```