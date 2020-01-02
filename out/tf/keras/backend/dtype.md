<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.dtype" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.dtype

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Returns the dtype of a Keras tensor or variable, as a string.

### Aliases:

* `tf.compat.v1.keras.backend.dtype`
* `tf.compat.v2.keras.backend.dtype`


``` python
tf.keras.backend.dtype(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.


#### Returns:

String, dtype of `x`.



#### Examples:


```python
    >>> from keras import backend as K
    >>> K.dtype(K.placeholder(shape=(2,4,5)))
    'float32'
    >>> K.dtype(K.placeholder(shape=(2,4,5), dtype='float32'))
    'float32'
    >>> K.dtype(K.placeholder(shape=(2,4,5), dtype='float64'))
    'float64'
    # Keras variable
    >>> kvar = K.variable(np.array([[1, 2], [3, 4]]))
    >>> K.dtype(kvar)
    'float32'
    >>> kvar = K.variable(np.array([[1, 2], [3, 4]]), dtype='float32')
    >>> K.dtype(kvar)
    'float32'
```