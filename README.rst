fmap
====

.. image:: https://travis-ci.org/mbodenhamer/fmap.svg?branch=master
    :target: https://travis-ci.org/mbodenhamer/fmap
    
.. image:: https://img.shields.io/coveralls/mbodenhamer/fmap.svg
    :target: https://coveralls.io/r/mbodenhamer/fmap
    
A Python command-line utility for recursively applying a command to a filesystem tree.

Usage
-----
.. code-block:: bash

    Usage: fmap [-h] [-p] [-v] [-d] [-l] [-b] [-z <depth>] [-x <pattern>] [-r <dir>]
         <cmd> [<pattern> [<pattern> ...]]

    Recusively apply a command to a filesystem tree.

    positional arguments:
      <cmd>                 The command to apply. The file to be applied may be
			    optionionally specified by '{}'. If '{}' is not
			    supplied, the file will be passed in as the last
			    argument.
      <pattern>             Unix filename pattern that specifies which files to
			    apply the command to.

    optional arguments:
      -h, --help            Show this help message and exit
      -p, --preview         Doesn't apply the command. Instead, prints command
			    invocations that would be performed.
      -v, --verbose         Print command invocations as they are performed.
      -d, --apply-dirs      Apply the command to directories after it is applied
			    to files at each level of the tree.
      -l, --follow-links    Follow symbolic links.
      -b, --bottom-up       Walk the tree from the bottom up. By default, the tree
			    is traversed from the top down.
      -z <depth>, --max-depth <depth>
			    Maximum recursion depth. Any negative number results
			    in unlimited recursion. Default is -1.
      -x <pattern>, --exclude <pattern>
			    Unix pattern that specifies which files to exclude
			    applying the command to.
      -r <dir>, --root <dir> Directory in which to begin the traversal. Is the
			    current directory by default.
