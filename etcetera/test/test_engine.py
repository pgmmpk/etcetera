from pathlib import Path
from etcetera.engine import Engine
from etcetera.impl.mock import MockRepo
import tempfile


def test_smoke():

    with tempfile.TemporaryDirectory() as d:
        e = Engine(d)

        assert str(e.home) == d

        with tempfile.TemporaryDirectory() as dataset:
            dataset = Path(dataset) / 'test-dataset'
            (dataset / 'data' / 'train').mkdir(parents=True)

            dataset.joinpath('data', 'train', 'data000.txt').write_text('Hello\n')
            dataset.joinpath('data', 'train', 'data001.txt').write_text('Hello again\n')

            e.register(dataset)
            assert set(e.ls()) == {'test-dataset'}

            e.register(dataset, name='test-dataset2')
            assert set(e.ls()) == {'test-dataset', 'test-dataset2'}

            e.purge('test-dataset')
            assert set(e.ls()) == {'test-dataset2'}

            repo = MockRepo()
            e.push('test-dataset2', repo)

            e.purge('test-dataset2')
            assert set(e.ls()) == set()

            e.pull('test-dataset2', repo)
            assert set(e.ls()) == {'test-dataset2'}

            ds = e.dataset('test-dataset2')
            assert ds.partitions() == ['train']
            files = list(ds['train'].iterdir())
            assert len(files) == 2

