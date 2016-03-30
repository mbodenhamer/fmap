import os
from fmap import fmap

DIR = os.path.abspath(os.path.dirname(__file__))
TESTDIR = os.path.join(DIR, 'tree')

#-------------------------------------------------------------------------------

def test_fmap():
    seen = []
    def accum(name):
        seen.append(name)

    fmap(TESTDIR, accum)
    assert set(seen) == {'c', 'd', 'f', 'g', 'h'}

    del seen[:]
    fmap(TESTDIR, accum, max_depth=0)
    assert set(seen) == {'c', 'd'}

    del seen[:]
    fmap(TESTDIR, accum, apply_dirs=True)
    assert set(seen) == {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}

    del seen[:]
    fmap(TESTDIR, accum, apply_dirs=True, max_depth=0)
    assert set(seen) == {'a', 'b', 'c', 'd'}

    del seen[:]
    fmap(TESTDIR, accum, excludes=['a'])
    assert set(seen) == {'c', 'd', 'h'}

    del seen[:]
    fmap(TESTDIR, accum, patterns=['g', 'd', 'h'], excludes=['a'])
    assert set(seen) == {'d', 'h'}

#-------------------------------------------------------------------------------

def test_fmap_invocation():
    pass

#-------------------------------------------------------------------------------
