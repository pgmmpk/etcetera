Etcetera
========

Dataset sharing via cloud storage (S3, Google Cloud).

Standard Dataset Structure
--------------------------

Dataset in ``etcetera`` is a collection of files organized into partitions. File content and type
can be anything. Optionally, one can attach a meta information to this collection.

A directory ``sample/`` is a valid dataset iff:

1. There is a sub-directory ``data/``
2. ``data/`` contains only directories (we call them "partitions")
3. there is at least one partition in ``data/``

Optionally, one can have a file named ``meta.json`` in the root of directory ``sample/`` with
arbitraty JSON content.

Other files and directories can be there as well. They will be stored and transported as-is.

Here is a sample dataset::

   sample/
      data/
         train/
            data00001.xml
            data00002.xml
            ...
         test/
            data00001.xml
            data00002.xml
            ...
      meta.json
      README.md
      assets/
         DataPreparation.ipynb

Installation
------------
We recommend installing with ``pip`` into virtual environment:

.. code-block:: bash

   python3 -m venv .venv   # create virtual environment
   . .venv/bin/activate    # activate it
   pip3 install etcetera   # install etcetera from PyPI

Installed Python package provides:
* command-line utility ``etc``
* Python package `etcetera` for programmatic access to datasets

Quick Start
-----------

First, lets create a directory with a minimal dataset:

.. code-block:: bash

   $ mkdir sample
   $ mkdir sample/data
   $ mkdir sample/data/train
   $ touch sample/data/train/data00001.txt

Now, lets register the dataset with the `etcetera`:

.. code-block:: bash

   $ etc register sample

We can list available local datasets:

.. code-block:: bash

   $ etc list
   >> sample

Form your Python code, accessing dataset is easy::

   import etcetera

   dataset = etcetera.dataset('sample')
   dataset.partitions()
   >> train

   for fname in dataset['train'].iterdir():
      print(fname)
   >> sample/train/data00001.txt


.. toctree::
    :maxdepth: 2
    :caption: Manual:

    tutorial.rst
    reference.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :ref:`glossary`