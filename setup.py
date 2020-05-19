from etcetera import __version__, __author__, __author_email__
from setuptools import setup, find_packages


def read(name):
    with open(name) as f:
        return f.read()


long_description = read('README.md')

setup(
    name='etcetera',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url='http://github.com/pgmmpk/etcetera',
    description='Sharing datasets via cloud storage',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[ 'PyYAML' ],
    extras_require={
        's3': [ 'boto3' ],
    },
    entry_points={
        'console_scripts': [
            'etc = etcetera.cli:main',
        ]
    }
)