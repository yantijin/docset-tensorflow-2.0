<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.gfile.stat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.gfile.stat

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/lib/io/file_io.py">View source</a>



<!-- Start diff -->
Returns file statistics for a given path.

### Aliases:

* `tf.compat.v1.io.gfile.stat`
* `tf.compat.v2.io.gfile.stat`


``` python
tf.io.gfile.stat(path)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, path to a file


#### Returns:

FileStatistics struct that contains information about the path



#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.