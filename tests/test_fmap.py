import os
from fmap import fmap
from subprocess import Popen, PIPE

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
    def seen(p):
        out = p.communicate()[0].decode('utf-8')
        seen = map(os.path.basename, filter(bool, str(out).split('\n')))
        return set(seen)

    p = Popen('fmap -r {} echo'.format(TESTDIR), stdout=PIPE, shell=True)
    assert seen(p) == {'c', 'd', 'f', 'g', 'h'}

    p = Popen('fmap -r {} -z0 echo'.format(TESTDIR), stdout=PIPE, shell=True)
    assert seen(p) == {'c', 'd'}

    p = Popen('fmap -r {} -d echo'.format(TESTDIR), stdout=PIPE, shell=True)
    assert seen(p) == {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}

    p = Popen('fmap -r {} -d -z0 echo'.format(TESTDIR), stdout=PIPE, shell=True)
    assert seen(p) == {'a', 'b', 'c', 'd'}

    p = Popen('fmap -r {} -x a echo'.format(TESTDIR), stdout=PIPE, shell=True)
    assert seen(p) == {'c', 'd', 'h'}
    
    p = Popen('fmap -r {} -x a echo g d h'.format(TESTDIR), stdout=PIPE, 
              shell=True)
    assert seen(p) == {'d', 'h'}

#-------------------------------------------------------------------------------
