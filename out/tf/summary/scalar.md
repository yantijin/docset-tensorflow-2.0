<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.scalar" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.scalar

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/scalar/summary_v2.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



<!-- Start diff -->
Write a scalar summary.

### Aliases:

* `tf.compat.v2.summary.scalar`


``` python
tf.summary.scalar(
    name,
    data,
    step=None,
    description=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`name`</b>: A name for this summary. The summary tag used for TensorBoard will
  be this name prefixed by any active name scopes.
* <b>`data`</b>: A real numeric scalar value, convertible to a `float32` Tensor.
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to <a href="../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a>, which must
  not be None.
* <b>`description`</b>: Optional long-form description for this summary, as a
  constant `str`. Markdown is supported. Defaults to empty.


#### Returns:

True on success, or false if no summary was written because no default
summary writer was available.



#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  <a href="../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a> is None.