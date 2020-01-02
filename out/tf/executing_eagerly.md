<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.executing_eagerly" />
<meta itemprop="path" content="Stable" />
</div>

# tf.executing_eagerly

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/eager/context.py">View source</a>



<!-- Start diff -->
Returns True if the current thread has eager execution enabled.

### Aliases:

* `tf.compat.v1.executing_eagerly`
* `tf.compat.v2.executing_eagerly`


``` python
tf.executing_eagerly()
```



<!-- Placeholder for "Used in" -->

Eager execution is typically enabled via
<a href="../tf/compat/v1/enable_eager_execution.md"><code>tf.compat.v1.enable_eager_execution</code></a>, but may also be enabled within the
context of a Python function via tf.contrib.eager.py_func.