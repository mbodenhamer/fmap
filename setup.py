from setuptools import setup, find_packages

def read(fpath):
    with open(fpath, 'r') as f:
        return f.read()

def version(fpath):
    return read(fpath).strip()

setup(
    name = 'fmap',
    version = version('version.txt'),
    author = 'Matt Bodenhamer',
    author_email = 'mbodenhamer@mbodenhamer.com',
    description = 'A command-line utility (and library) for recursively applying a command to a filesystem tree',
    long_description = read('README.rst'),
    url = 'https://github.com/mbodenhamer/fmap',
    packages = find_packages(),
    install_requires = [],
    entry_points = [],
    license = 'MIT',
    classifiers = []
)
