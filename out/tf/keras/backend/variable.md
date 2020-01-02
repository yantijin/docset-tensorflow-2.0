<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.variable" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.variable

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Instantiates a variable and returns it.

### Aliases:

* `tf.compat.v1.keras.backend.variable`
* `tf.compat.v2.keras.backend.variable`


``` python
tf.keras.backend.variable(
    value,
    dtype=None,
    name=None,
    constraint=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`value`</b>: Numpy array, initial value of the tensor.
* <b>`dtype`</b>: Tensor type.
* <b>`name`</b>: Optional name string for the tensor.
* <b>`constraint`</b>: Optional projection function to be
    applied to the variable after an optimizer update.


#### Returns:

A variable instance (with Keras metadata included).



#### Examples:


```python
    >>> import numpy as np
    >>> from keras import backend as K
    >>> val = np.array([[1, 2], [3, 4]])
    >>> kvar = K.variable(value=val, dtype='float64', name='example_var')
    >>> K.dtype(kvar)
    'float64'
    >>> print(kvar)
    example_var
    >>> kvar.eval()
    array([[ 1.,  2.],
           [ 3.,  4.]])
```