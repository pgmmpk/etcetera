from etcetera import dataset, register, push, pull, ls, purge, Config
from unittest import mock
from etcetera.impl.mock import MockRepo
import tempfile


def test_01():
    with tempfile.TemporaryDirectory() as d:
        config = Config('mock://', home=d)
        with mock.patch('etcetera.api.Repo.load') as m:
            mock_repo = MockRepo()
            m.return_value = mock_repo
            datasets = list(ls(remote=True, config=config))
            assert len(datasets) == 0

            mock_repo.repo['sample.tgz'] = b''

            datasets = list(ls(remote=True, config=config))
            assert datasets == ['sample']
