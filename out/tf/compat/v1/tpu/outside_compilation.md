<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.outside_compilation" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.outside_compilation

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/tpu/tpu.py">View source</a>



<!-- Start diff -->
Builds part of a computation outside any current TPU replicate scope.

``` python
tf.compat.v1.tpu.outside_compilation(
    computation,
    *args,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`computation`</b>: A Python function that builds the computation to
  place on the host.
* <b>`*args`</b>: the positional arguments for the computation.
* <b>`**kwargs`</b>: the keyword arguments for the computation.


#### Returns:

The Tensors returned by computation.
