import os
import sys
from .fmap import fmap

#-------------------------------------------------------------------------------

def process_args(args):
    import argparse
    parser = argparse.ArgumentParser(prog='fmap')

    parser.add_argument('-p', '--preview', dest='preview', default=False,
                        action='store_true',
                        help="Don't apply the command; print command invoations"
                        " that would be performed")
    parser.add_argument('-v', '--verbose', dest='verbose', default=False,
                        action='store_true',
                        help="Print command invocations as they are performed")
    parser.add_argument('-d', '--apply-dirs', dest='apply_dirs', default=False,
                        action='store_true',
                        help="Apply the command to directories "
                        "after it is applied to files")
    parser.add_argument('-l', '--follow-links', dest='follow_links', 
                        default=False, action='store_true',
                        help="Follow symbolic links")
    parser.add_argument('-b', '--bottom-up', dest='top_down', default=True,
                        action='store_false',
                        help="Walk the tree from the bottom up")
    parser.add_argument('-e', '--abort-on-errors', dest="abort_on_errors",
                        default=False, action="store_true",
                        help="Abort execution for file listing errors")
    parser.add_argument('-z', '--max-depth', dest="max_depth", default=-1,
                        type=int,
                        help="Maximum recursion depth")
    parser.add_argument('-x', '--exclude', action='append', metavar='PATTERN',
                        dest='excludes',
                        help="Shell filename expansion patterns that specify "
                        "which files to exclude applying the command to")
    parser.add_argument('-r', '--root', type=str, dest='root', metavar='DIR',
                        default=os.getcwd(),
                        help='Directory in which to begin the traversal')
    parser.add_argument('command', metavar='CMD', type=str,
                        help="The command to apply; the file to be applied may "
                        "be optiontionally specified by '{}'")
    parser.add_argument('patterns', metavar='PATTERNS', nargs='*', 
                        help="Shell filename expansion patterns that specify "
                        "which files to apply the command to")
    
    opts = parser.parse_args(args)
    if opts.preview:
        opts.verbose = True
    if '{}' not in opts.command:
        opts.command += ' {}'
    if not opts.patterns:
        opts.patterns = ['*']

    return opts

#-------------------------------------------------------------------------------

def main(*args):
    if not args:
        args = sys.argv[1:]
    
    opts = process_args(args)
    fmap(**vars(opts))

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
