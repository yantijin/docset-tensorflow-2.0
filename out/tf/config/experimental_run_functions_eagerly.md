<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental_run_functions_eagerly" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental_run_functions_eagerly

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/eager/def_function.py">View source</a>



<!-- Start diff -->
Enables / disables eager execution of <a href="../../tf/function.md"><code>tf.function</code></a>s.

### Aliases:

* `tf.compat.v1.config.experimental_run_functions_eagerly`
* `tf.compat.v2.config.experimental_run_functions_eagerly`


``` python
tf.config.experimental_run_functions_eagerly(run_eagerly)
```



<!-- Placeholder for "Used in" -->

After calling <a href="../../tf/config/experimental_run_functions_eagerly.md"><code>tf.config.experimental_run_functions_eagerly(True)</code></a> all
invocations of tf.function will run eagerly instead of running through a graph
function.

This can be useful for debugging or profiling.

Similarly, calling <a href="../../tf/config/experimental_run_functions_eagerly.md"><code>tf.config.experimental_run_functions_eagerly(False)</code></a> will
revert the behavior of all functions to graph functions.

#### Args:


* <b>`run_eagerly`</b>: Boolean. Whether to run functions eagerly.