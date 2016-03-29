import os
from fnmatch import fnmatch

#-------------------------------------------------------------------------------
# Exclusion/Inclusion Utilities

def excluded(names, excludes):
    for name in names:
        for pattern in excludes:
            if fnmatch(name, pattern):
                yield name
                break

def applicable(names, patterns, excludes):
    excl = set(excluded(names, excludes))

    for name in names:
        if name in excl:
            continue

        for pattern in patterns:
            if fnmatch(name, pattern):
                yield name
                break

#-------------------------------------------------------------------------------

def apply_command(command, base, names, patterns, excludes, preview=False, 
                  verbose=False):
    for name in applicable(names, patterns, excludes):
        path = os.path.join(base, name)
        cmd = command.format(path)
        if verbose:
            print(cmd)
        if not preview:
            os.system(cmd)

#-------------------------------------------------------------------------------

def fmap(root=None, command='', patterns=None, excludes=None, max_depth=-1,
         top_down=True, preview=False, verbose=False, apply_dirs=False, 
         follow_links=False, abort_on_errors=False):
    
    if root is None:
        root = os.getcwd()
    if patterns is None:
        patterns = ['*']
    if excludes is None:
        excludes = []

    def error(err):
        if abort_on_errors:
            raise err
        else:
            print(err.args[0])

    depth = 0
    for base, dirs, files in os.walk(root, topdown=top_down, onerror=error,
                                     followlinks=follow_links):
        if max_depth >= 0:
            if depth > max_depth:
                return

        if top_down:
            for exdir in list(excluded(dirs, excludes)):
                dirs.remove(exdir)

        apply_command(command, base, files, patterns, excludes, preview, 
                      verbose)
        if apply_dirs:
            apply_command(command, base, dirs, patterns, excludes, preview, 
                          verbose)
        depth += 1
    
#-------------------------------------------------------------------------------

__all__ = ['fmap']

#-------------------------------------------------------------------------------
