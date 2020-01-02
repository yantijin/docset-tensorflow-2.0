<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.digamma" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.digamma

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



<!-- Start diff -->
Computes Psi, the derivative of Lgamma (the log of the absolute value of

### Aliases:

* `tf.compat.v1.digamma`
* `tf.compat.v1.math.digamma`
* `tf.compat.v2.math.digamma`


``` python
tf.math.digamma(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

`Gamma(x)`), element-wise.

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
