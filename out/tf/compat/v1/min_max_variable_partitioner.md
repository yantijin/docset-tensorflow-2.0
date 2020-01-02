<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.min_max_variable_partitioner" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.min_max_variable_partitioner

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/partitioned_variables.py">View source</a>



<!-- Start diff -->
Partitioner to allocate minimum size per slice.

``` python
tf.compat.v1.min_max_variable_partitioner(
    max_partitions=1,
    axis=0,
    min_slice_size=(256 << 10),
    bytes_per_string_element=16
)
```



<!-- Placeholder for "Used in" -->

Returns a partitioner that partitions the variable of given shape and dtype
such that each partition has a minimum of `min_slice_size` slice of the
variable. The maximum number of such partitions (upper bound) is given by
`max_partitions`.

#### Args:


* <b>`max_partitions`</b>: Upper bound on the number of partitions. Defaults to 1.
* <b>`axis`</b>: Axis along which to partition the variable. Defaults to 0.
* <b>`min_slice_size`</b>: Minimum size of the variable slice per partition. Defaults
  to 256K.
* <b>`bytes_per_string_element`</b>: If the `Variable` is of type string, this provides
  an estimate of how large each scalar in the `Variable` is.


#### Returns:

A partition function usable as the `partitioner` argument to
`variable_scope` and `get_variable`.