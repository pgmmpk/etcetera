from pathlib import Path
import yaml

class Config:
    def __init__(self, url:str, home=None, **conf):
        self.url  = url
        self.home = home or Path.home() / '.etc'
        self.conf = conf

    @classmethod
    def load(cls, filename=None):
        if filename is None:
            filename = Path.home() / '.etc.yaml'
        else:
            filename = Path(filename)

        if not filename.is_file():
            raise RuntimeError(f'Can not find configuration file {filename}')

        with open(filename) as f:
            conf = yaml.load(f, Loader=yaml.Loader)

        url = conf.pop('url', None)
        if url is None:
            raise RuntimeError(f'Profile {profile} in {filename} does not have "url" key')
        home = conf.pop('home', None)
        if home is None:
            home = Path.home() / '.etc'

        return Config(url, home, **conf)
