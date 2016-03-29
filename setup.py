from setuptools import setup, find_packages

def read(fpath):
    with open(fpath, 'r') as f:
        return f.read()

def requirements(fpath):
    return list(filter(bool, read(fpath).split('\n')))

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
    install_requires = requirements('requirements.txt'),
    entry_points = {
        'console_scripts': [
            'fmap = fmap.__main__:main',
        ]
    },
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities'
    ]
)
