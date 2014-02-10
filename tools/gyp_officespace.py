#!/usr/bin/env python
import glob
import os
import shlex
import sys

script_dir = os.path.dirname(__file__)
repo_root  = os.path.normpath(os.path.join(script_dir, os.pardir))

sys.path.insert(0, os.path.join(repo_root, 'tools', 'gyp', 'pylib'))
import gyp

# Directory within which we want all generated files (including Makefiles)
# to be written.
output_dir = os.path.join(os.path.abspath(repo_root), 'out')

def run_gyp(args):
    rc = gyp.main(args)
    if rc != 0:
        print 'Error running GYP'
        sys.exit(rc)

if __name__ == '__main__':
    args = sys.argv[1:]

    args.append(os.path.join(os.path.abspath(repo_root), 'officespace.gyp'))
    common_fn  = os.path.join(os.path.abspath(repo_root), 'common.gypi')
    options_fn = os.path.join(os.path.abspath(repo_root), 'config.gypi')

    if os.path.exists(common_fn):
        args.extend(['-I', common_fn])

    if os.path.exists(options_fn):
        args.extend(['-I', options_fn])

    args.append('--depth=' + repo_root)

    gyp_args = list(args)
    run_gyp(gyp_args)
