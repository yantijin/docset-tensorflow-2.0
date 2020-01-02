<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.gfile.mkdir" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.gfile.mkdir

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/lib/io/file_io.py">View source</a>



<!-- Start diff -->
Creates a directory with the name given by 'path'.

### Aliases:

* `tf.compat.v1.io.gfile.mkdir`
* `tf.compat.v2.io.gfile.mkdir`


``` python
tf.io.gfile.mkdir(path)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, name of the directory to be created
Notes: The parent directories need to exist. Use recursive_create_dir instead
  if there is the possibility that the parent dirs don't exist.

#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.