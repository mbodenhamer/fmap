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
    parser.add_argument('-d', '--dirs-only', dest='dirs_only', default=False,
                        action='store_true',
                        help="Apply the command only to directories")
    parser.add_argument('-l', '--links-only', dest='links_only', default=False,
                        action='store_true',
                        help="Apply the command only to symbolic links")
    parser.add_argument('-r', '--recursive', dest='recursive', default=False,
                        action='store_true',
                        help='Recursively apply the command down the filesystem' 
                        ' tree')
    parser.add_argument('-s', metavar='PATTERN', type=str, default='*',
                        dest='pattern',
                        help='The filename pattern to match at each directory '
                        'in which the command is applied')
    parser.add_argument('command', metavar='CMD', type=str,
                        help="The command to apply; the file to be applied may "
                        "be optiontionally specified by '{}'")
    parser.add_argument('files', metavar='FILES', type=str,
                        default='', nargs='?',
                        help="Files to apply the command to")
    
    opts = parser.parse_args(args)

    opts.files = opts.files.split()
    if opts.preview:
        opts.verbose = True

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
