<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.threading.get_inter_op_parallelism_threads" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.threading.get_inter_op_parallelism_threads

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/framework/config.py">View source</a>



<!-- Start diff -->
Get number of threads used for parallelism between independent operations.

### Aliases:

* `tf.compat.v1.config.threading.get_inter_op_parallelism_threads`
* `tf.compat.v2.config.threading.get_inter_op_parallelism_threads`


``` python
tf.config.threading.get_inter_op_parallelism_threads()
```



<!-- Placeholder for "Used in" -->

Determines the number of threads used by independent non-blocking operations.
0 means the system picks an appropriate number.

#### Returns:

Number of parallel threads
