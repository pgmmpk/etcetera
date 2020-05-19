from etcetera.dataset import Dataset
import tempfile
from pathlib import Path
import pytest


def test_dataset():
    with pytest.raises(ValueError, match=r'Directory .*blah-blah does not exist$'):
        Dataset('blah-blah')

    with tempfile.TemporaryDirectory() as d:
        with pytest.raises(ValueError, match=r'Directory .* expect "data/" subdirectory to exist$'):
            Dataset(d)

        d = Path(d)
        (d / 'data').mkdir()

        with pytest.raises(ValueError, match=r'Directory .* must have at least one partition in it$'):
            Dataset(d)

        (d / 'data' / 'train').mkdir()
        dataset = Dataset(d)
        assert dataset.keys() == {'train'}

        assert dataset['train']

        with pytest.raises(ValueError, match=r'Partition val does not exist in dataset .*'):
            dataset['val']
