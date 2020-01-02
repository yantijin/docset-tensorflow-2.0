<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.pow" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.pow

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



<!-- Start diff -->
Computes the power of one value to another.

### Aliases:

* `tf.RaggedTensor.__pow__`
* `tf.compat.v1.RaggedTensor.__pow__`
* `tf.compat.v1.math.pow`
* `tf.compat.v1.pow`
* `tf.compat.v2.RaggedTensor.__pow__`
* `tf.compat.v2.math.pow`
* `tf.compat.v2.pow`
* `tf.pow`


``` python
tf.math.pow(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for
corresponding elements in `x` and `y`. For example:

```python
x = tf.constant([[2, 2], [3, 3]])
y = tf.constant([[8, 16], [2, 3]])
tf.pow(x, y)  # [[256, 65536], [9, 27]]
```

#### Args:


* <b>`x`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, or `complex128`.
* <b>`y`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, or `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`.