<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental.VirtualDeviceConfiguration" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="memory_limit"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.config.experimental.VirtualDeviceConfiguration

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/eager/context.py">View source</a>



## Class `VirtualDeviceConfiguration`

<!-- Start diff -->
Configuration class for virtual devices for a PhysicalDevice.



### Aliases:

* Class `tf.compat.v1.config.experimental.VirtualDeviceConfiguration`
* Class `tf.compat.v2.config.experimental.VirtualDeviceConfiguration`


<!-- Placeholder for "Used in" -->


#### Fields:


* <b>`memory_limit`</b>: (optional) Maximum memory (in MB) to allocate on the virtual
  device. Currently only supported for GPUs.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="/code/stable/tensorflow/python/eager/context.py">View source</a>

``` python
@staticmethod
__new__(
    cls,
    memory_limit=None
)
```

Create new instance of VirtualDeviceConfiguration(memory_limit,)




## Properties

<h3 id="memory_limit"><code>memory_limit</code></h3>






