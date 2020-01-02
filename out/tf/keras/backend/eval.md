<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.eval" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.eval

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Evaluates the value of a variable.

### Aliases:

* `tf.compat.v1.keras.backend.eval`
* `tf.compat.v2.keras.backend.eval`


``` python
tf.keras.backend.eval(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A variable.


#### Returns:

A Numpy array.



#### Examples:


```python
    >>> from keras import backend as K
    >>> kvar = K.variable(np.array([[1, 2], [3, 4]]), dtype='float32')
    >>> K.eval(kvar)
    array([[ 1.,  2.],
           [ 3.,  4.]], dtype=float32)
```