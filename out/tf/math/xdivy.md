<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.xdivy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.xdivy

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



<!-- Start diff -->
Returns 0 if x == 0, and x / y otherwise, elementwise.

### Aliases:

* `tf.compat.v1.math.xdivy`
* `tf.compat.v2.math.xdivy`


``` python
tf.math.xdivy(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
