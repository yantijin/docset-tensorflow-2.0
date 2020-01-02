<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.minimum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.minimum

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



<!-- Start diff -->
Returns the min of x and y (i.e. x < y ? x : y) element-wise.

### Aliases:

* `tf.compat.v1.math.minimum`
* `tf.compat.v1.minimum`
* `tf.compat.v2.math.minimum`
* `tf.compat.v2.minimum`
* `tf.minimum`


``` python
tf.math.minimum(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/minimum.md"><code>math.minimum</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
