<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.gfile.remove" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.gfile.remove

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/lib/io/file_io.py">View source</a>



<!-- Start diff -->
Deletes the path located at 'path'.

### Aliases:

* `tf.compat.v1.io.gfile.remove`
* `tf.compat.v2.io.gfile.remove`


``` python
tf.io.gfile.remove(path)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, a path


#### Raises:


* <b>`errors.OpError`</b>: Propagates any errors reported by the FileSystem API.  E.g.,
NotFoundError if the path does not exist.