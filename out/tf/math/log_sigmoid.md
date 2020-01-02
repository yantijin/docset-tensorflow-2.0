<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.log_sigmoid" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.log_sigmoid

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



<!-- Start diff -->
Computes log sigmoid of `x` element-wise.

### Aliases:

* `tf.compat.v1.log_sigmoid`
* `tf.compat.v1.math.log_sigmoid`
* `tf.compat.v2.math.log_sigmoid`


``` python
tf.math.log_sigmoid(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Specifically, `y = log(1 / (1 + exp(-x)))`.  For numerical stability,
we use `y = -tf.nn.softplus(-x)`.

#### Args:


* <b>`x`</b>: A Tensor with type `float32` or `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A Tensor with the same type as `x`.
