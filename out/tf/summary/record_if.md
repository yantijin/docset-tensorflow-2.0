<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.record_if" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.record_if

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/summary_ops_v2.py">View source</a>



<!-- Start diff -->
Sets summary recording on or off per the provided boolean value.

### Aliases:

* `tf.compat.v2.summary.record_if`


``` python
tf.summary.record_if(condition)
```



<!-- Placeholder for "Used in" -->

The provided value can be a python boolean, a scalar boolean Tensor, or
or a callable providing such a value; if a callable is passed it will be
invoked on-demand to determine whether summary writing will occur.

#### Args:


* <b>`condition`</b>: can be True, False, a bool Tensor, or a callable providing such.


#### Yields:

Returns a context manager that sets this value on enter and restores the
previous value on exit.
