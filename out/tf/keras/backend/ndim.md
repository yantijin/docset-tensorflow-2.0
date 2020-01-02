<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.ndim" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.ndim

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Returns the number of axes in a tensor, as an integer.

### Aliases:

* `tf.compat.v1.keras.backend.ndim`
* `tf.compat.v2.keras.backend.ndim`


``` python
tf.keras.backend.ndim(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.


#### Returns:

Integer (scalar), number of axes.



#### Examples:


```python
    >>> from keras import backend as K
    >>> input = K.placeholder(shape=(2, 4, 5))
    >>> val = np.array([[1, 2], [3, 4]])
    >>> kvar = K.variable(value=val)
    >>> K.ndim(input)
    3
    >>> K.ndim(kvar)
    2
```