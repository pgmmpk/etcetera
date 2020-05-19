.. module:: etcetera
   :noindex:

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

   python3 -m venv .venv         # create virtual environment
   . .venv/bin/activate          # activate it
   pip3 install 'etcetera[s3]'   # install etcetera from PyPI with s3 backend

Installed Python package provides:

* a command-line utility ``etc``
* Python package ``etcetera`` for programmatic access to datasets

Quick Start
-----------

First, lets create a directory with a minimal dataset:

.. code-block:: bash

   $ mkdir -p sample/data/train
   $ touch sample/data/train/data00001.txt

Now, lets register the dataset with the ``etcetera``:

.. code-block:: bash

   $ etc register sample

We can list available local datasets:

.. code-block:: bash

   $ etc list
   >> sample

Form your Python code, accessing dataset is easy::

   import etcetera as etc

   dataset = etc.dataset('sample')
   dataset.partitions()
   >> train

   for fname in dataset['train'].iterdir():
      print(fname)
   >> sample/train/data00001.txt

   dataset.meta
   >> {}

Configure access to cloud storage
---------------------------------

Configuration is stored in ``~/.etc.toml`` and should specify at least ``url`` key:

.. code-block:: toml

   url = "s3://my-datasets"

Now remote repository is set to ``s3://my-datasets``. To be able to pull and push you
need to set the authentication parameters. For example:

.. code-block:: toml

   url = "s3://my-datasets"
   aws_access_key_id = "AAasdsffDF12SDASD"
   aws_secret_access_key = "fgT6Dfr8Bhfgt4fdr5asdffd7"
   public = false

Note the ``public`` value here. When set to ``true``, pushed datasets will be publicly-readable.

Programmatic Configuration
--------------------------

``etcetera`` api can be used to access remote repositories without ever creating a
configuration file. This is convenient if you run code on a disposable machines (like
cloud workers), avoiding extra provisioning steps. Here is an example::

   import etcetera as etc

   config = etc.Config('s3://my-datasets')

   # following will pull dataset from the repository if it is not found locally
   dataset = etc.dataset('sample', auto_pull=True, config=config)

Using :class:`Config` one can configure the location of the local datasets, repository
authentication parameters, and so on. For the detail, check the Reference section below.

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