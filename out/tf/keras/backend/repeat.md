<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.repeat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.repeat

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Repeats a 2D tensor.

### Aliases:

* `tf.compat.v1.keras.backend.repeat`
* `tf.compat.v2.keras.backend.repeat`


``` python
tf.keras.backend.repeat(
    x,
    n
)
```



<!-- Placeholder for "Used in" -->

if `x` has shape (samples, dim) and `n` is `2`,
the output will have shape `(samples, 2, dim)`.

#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`n`</b>: Python integer, number of times to repeat.


#### Returns:

A tensor.



#### Example:

```python
  >>> b = tf.constant([[1, 2], [3, 4]])
  >>> b
  <tf.Tensor: id=78, shape=(2, 2), dtype=int32, numpy=
  array([[1, 2],
         [3, 4]], dtype=int32)>
  >>> tf.keras.backend.repeat(b, n=2)
  <tf.Tensor: id=82, shape=(2, 2, 2), dtype=int32, numpy=
  array([[[1, 2],
          [1, 2]],
         [[3, 4],
          [3, 4]]], dtype=int32)>
```
