<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.not_equal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.not_equal

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



<!-- Start diff -->
Returns the truth value of (x != y) element-wise.

### Aliases:

* `tf.compat.v1.math.not_equal`
* `tf.compat.v1.not_equal`
* `tf.compat.v2.math.not_equal`
* `tf.compat.v2.not_equal`
* `tf.not_equal`


``` python
tf.math.not_equal(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

**NOTE**: `NotEqual` supports broadcasting. More about broadcasting [here](
https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`y`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type bool with the same size as that of x or y.
