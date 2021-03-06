# etcetera
[![Build Status](https://travis-ci.org/pgmmpk/etcetera.svg?branch=master)](https://travis-ci.org/pgmmpk/etcetera)
[![PyPI version](https://badge.fury.io/py/etcetera.svg)](https://badge.fury.io/py/etcetera)
[![Documentation Status](https://readthedocs.org/projects/etcetera/badge/?version=latest)](https://etcetera.readthedocs.io/en/latest/?badge=latest)

Dataset sharing via cloud storage (S3, Google Storage)

## Mental model
A dataset is an immutable collection of files organized in directories (e.g `train/`, `val/`).

A dataset can have a `meta.json` file, which is a collection of arbitraty key/value pairs.

Dataset can be local or remote. Local datasets are kept in `~/.etc/`. Remote datasets are `tgz` files stored in cloud storage.

PyPI package `etcetera` provides:
* a command-line utility `etc`
* Python package `etcetera`

### Using Command Line

```bash
etc -h
usage: etc [-h] {ls,register,pull,push,purge} ...

etcetera: managing cloud-hosted datasets

positional arguments:
  {ls,register,pull,push,purge}
                        command
    ls                  List datasets
    register            Register directory as a dataset
    pull                Pull dataset from repository
    push                Push dataset to the repository
    purge               Purge local dataset

optional arguments:
  -h, --help            show this help message and exit
```

### Using Python
```python
import etcetera as etc

dataset = etc.dataset('flower', auto_install=True)
dataset.keys()
>> { 'test', 'train' }

for filename in dataset['train'].iterdir():
    print(filename)
>> "~/.etc/flower/train/data00001.txt"
>> "~/.etc/flower/train/data00002.txt"

dataset.meta
>> {}
dataset.root
>> "~/.etc/flower"
```

## Installing
```
pip install 'etcetera[s3]'
```
Installs `etceters` with the support for S3 cloud.

## Configuration

`~/.etc.toml` contains configuration for the service in TOML format. Example:

```toml
url = "s3://my-bucket"
```

Another example:

```toml
url = "s3://my-bucket"
public = false
aws_access_key_id = "Axxxx"
aws_secret_access_key = "Kxxx"
endpoint_url = "https://s3.amazonaws.com"
```

A configuration file is required for remote operations (`pull`, `push`, `ls -r`). It is not required for local operations (`ls`, `register`).

In configuration file `url` value is required. The rest is optional.

* `url`: URL of the remote repository. For example, `s3://my-bucket`.
* `public`: set to `true` if you want `push` to create publicly-readable cloud files.
   Default is `false`.
* `aws_access_key_id`, `aws_secret_access_key`, `endpoint_url`: configuration files to access
   AWS api. If not set, the defaults from global AWS config will be used.

## Command-line example
```bash
etc ls
etc ls -r
etc pull MNIST
etc register <directory> as SuperMNIST
```

## Creating a dataset
A dataset must have:
1. `data` directory (non-empty)
2. `data` directory must not have any files, only sub-directories (we call them "partitions")

Optional:
1. `meta.json`
2. `README.md`
3. other sub-directories, for example `assets/`

### A minimal dataset example
```
sample/
    data/
        train/
            data00001.json
            data00002.json
            data00003.json
```

### A general dataset example
```
sample/
    README.md
    meta.json
    assets/
        Analysis.ipynb
        DataCleanup.ipynb
    data/
        train/
            data00001.json
            ...
        test/
            test00001.json
            ...
        val/
            val00001.json
            ...
```
