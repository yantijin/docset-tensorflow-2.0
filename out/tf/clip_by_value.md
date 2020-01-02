<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.clip_by_value" />
<meta itemprop="path" content="Stable" />
</div>

# tf.clip_by_value

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/clip_ops.py">View source</a>



<!-- Start diff -->
Clips tensor values to a specified min and max.

### Aliases:

* `tf.compat.v1.clip_by_value`
* `tf.compat.v2.clip_by_value`


``` python
tf.clip_by_value(
    t,
    clip_value_min,
    clip_value_max,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor `t`, this operation returns a tensor of the same type and
shape as `t` with its values clipped to `clip_value_min` and `clip_value_max`.
Any values less than `clip_value_min` are set to `clip_value_min`. Any values
greater than `clip_value_max` are set to `clip_value_max`.

Note: `clip_value_min` needs to be smaller or equal to `clip_value_max` for
correct results.

#### For example:



```python
A = tf.constant([[1, 20, 13], [3, 21, 13]])
B = tf.clip_by_value(A, clip_value_min=0, clip_value_max=3) # [[1, 3, 3],[3, 3, 3]]
C = tf.clip_by_value(A, clip_value_min=0., clip_value_max=3.) # throws `TypeError`
as input and clip_values are of different dtype
```

#### Args:


* <b>`t`</b>: A `Tensor` or `IndexedSlices`.
* <b>`clip_value_min`</b>: A 0-D (scalar) `Tensor`, or a `Tensor` with the same shape
  as `t`. The minimum value to clip by.
* <b>`clip_value_max`</b>: A 0-D (scalar) `Tensor`, or a `Tensor` with the same shape
  as `t`. The maximum value to clip by.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A clipped `Tensor` or `IndexedSlices`.



#### Raises:


* <b>`ValueError`</b>: If the clip tensors would trigger array broadcasting
  that would make the returned tensor larger than the input.
* <b>`TypeError`</b>: If dtype of the input is `int32` and dtype of
the `clip_value_min' or `clip_value_max` is `float32`