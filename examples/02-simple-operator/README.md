=======================
# Simple Operator Example <img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=e8da2de2-769b-48e2-a194-a1efb25883f6&page=example-02&title=Simple Operator Example" />


This example includes a simple operator that is built using `Kopf
<https://kopf.readthedocs.io>`_. Kopf makes bootstrapping of the operator
very easy.


## Running example

In order to run this example, you can use ``poetry`` in this project::

``` sh
poetry run kopf run examples/02-simple-operator/watcher.py --verbose
```

Note that if you aren't using ``poetry``, you can also run this simply by
installing all dependencies in a virtualenv and running:

``` sh
kopf run examples/02-simple-operator/watcher.py --verbose
```

