<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.unravel_index" />
<meta itemprop="path" content="Stable" />
</div>

# tf.unravel_index

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



<!-- Start diff -->
Converts a flat index or array of flat indices into a tuple of

### Aliases:

* `tf.compat.v1.unravel_index`
* `tf.compat.v2.unravel_index`


``` python
tf.unravel_index(
    indices,
    dims,
    name=None
)
```



<!-- Placeholder for "Used in" -->

coordinate arrays.



#### Args:


* <b>`indices`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  An 0-D or 1-D `int` Tensor whose elements are indices into the
  flattened version of an array of dimensions dims.
* <b>`dims`</b>: A `Tensor`. Must have the same type as `indices`.
  An 1-D `int` Tensor. The shape of the array to use for unraveling
  indices.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `indices`.


#### Numpy Compatibility
Equivalent to np.unravel_index
