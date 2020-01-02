<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.optimizer.get_experimental_options" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.optimizer.get_experimental_options

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/framework/config.py">View source</a>



<!-- Start diff -->
Get experimental optimizer options.

### Aliases:

* `tf.compat.v1.config.optimizer.get_experimental_options`
* `tf.compat.v2.config.optimizer.get_experimental_options`


``` python
tf.config.optimizer.get_experimental_options()
```



<!-- Placeholder for "Used in" -->

Refer to tf.config.optimizer.set_experimental_options for a list of current
options.

Note that optimizations are only applied in graph mode, (within tf.function).
In addition, as these are experimental options, the list is subject to change.

#### Returns:

Dictionary of configured experimental optimizer options
