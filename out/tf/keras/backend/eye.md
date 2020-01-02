<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.eye" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.eye

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Instantiate an identity matrix and returns it.

### Aliases:

* `tf.compat.v1.keras.backend.eye`
* `tf.compat.v2.keras.backend.eye`


``` python
tf.keras.backend.eye(
    size,
    dtype=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`size`</b>: Integer, number of rows/columns.
* <b>`dtype`</b>: String, data type of returned Keras variable.
* <b>`name`</b>: String, name of returned Keras variable.


#### Returns:

A Keras variable, an identity matrix.



#### Example:


```python
    >>> from keras import backend as K
    >>> kvar = K.eye(3)
    >>> K.eval(kvar)
    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]], dtype=float32)
```