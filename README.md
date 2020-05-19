# etcetera
Dataset sharing via cloud storage (S3, Google Storage)

## Mental model
A dataset is an immutable collection of files organized in directories (e.g `train/`, `val/`).

A dataset can have a `meta.json` file, which is a collection of arbitraty key/value pairs.

Dataset can be local or remote. Local datasets are kept in `~/.etc/`. Remote datasets are `tgz` files stored in cloud storage.

PyPI package `etcetera` provides:
* a command-line utility `etc`
* Python package `etcetera`

### Using Command Line

`etc ls` list local datasets.

`etc ls --remote` list remote datasets.

`etc pull <DATASET> [-f/--force]` downloads remote dataset and installs it locally.

`etc push <DATASET> [-f/--force]` packages local dataset and uploads it to the cloud storage.

`etc register <LOCAL_DIR> <DATASET> [-f/--force]` validates dataset and registers it as a local dataset

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

## Configuration
`~/.etc.yaml` contains configuration for the service:

Example:
```yaml
url: "s3://my-bucket"
aws_access_key_id: Axxxx
aws_secret_access_key: Axxx
public: false
```

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

