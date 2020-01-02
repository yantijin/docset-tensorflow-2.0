<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.gfile.listdir" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.gfile.listdir

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/lib/io/file_io.py">View source</a>



<!-- Start diff -->
Returns a list of entries contained within a directory.

### Aliases:

* `tf.compat.v1.io.gfile.listdir`
* `tf.compat.v2.io.gfile.listdir`


``` python
tf.io.gfile.listdir(path)
```



<!-- Placeholder for "Used in" -->

The list is in arbitrary order. It does not contain the special entries "."
and "..".

#### Args:


* <b>`path`</b>: string, path to a directory


#### Returns:

[filename1, filename2, ... filenameN] as strings



#### Raises:

errors.NotFoundError if directory doesn't exist
