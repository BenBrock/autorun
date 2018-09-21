#!/usr/bin/env python3
import argparse
import json

import ast
import sys
import os

def get_config_fname(args):
    binary_path = os.path.dirname(os.path.realpath(__file__))
    fname = binary_path + '/conf/'
    return 'conf.' + args.config

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='autorun, an automatic job \
             generator for HPC queueing systems')
    parser.add_argument('--config', dest='config', type=str,
                        help='Batch file template', required=True)

    parser.add_argument('--node-range', dest='node_range', type=str,
                        help='Numbers of nodes to run on. e.g. [1, 2, 4]', required=True)

    parser.add_argument('--npernode', dest='npernode', type=str,
                        help='Number of ranks to launch per node.', required=True)

    parser.add_argument('--job-name', dest='jobname', type=str,
                        help='Job title', required=True)

    parser.add_argument('--command', dest='commands', type=str,
                        help='Command to run', required=True)

    parser.add_argument('--account', dest='account', type=str,
                        help='Account to charge', required=True)

    parser.add_argument('--runtime', dest='runtime', type=str,
                        help='Job runtime', required=True)

    args = parser.parse_args()

    args.node_range = ast.literal_eval(args.node_range)
    args.commands = ast.literal_eval(args.commands)

    if isinstance(args.commands, str):
        args.commands = [args.commands]

    config_fname = get_config_fname(args)
    tmplt = __import__(config_fname).__dict__[args.config]

    try:
        success = os.makedirs(args.jobname)
    except:
        print("Could not make directory '%s'" % (args.jobname,))
        sys.exit()
    os.chdir(args.jobname)

    for nnodes in args.node_range:
        args.nnodes = nnodes

        gend_fname = '{jobname}_{nnodes}.batch'.format(**args.__dict__)
        gend_batchfile = tmplt.template.format(**args.__dict__)
        for command in args.commands:
            args.command = command
            launch_command = tmplt.launcher.format(**args.__dict__)
            gend_batchfile += "echo \"%s\"" % (launch_command) + "\n";
            gend_batchfile += launch_command + "\n"

        open(gend_fname, 'w').write(gend_batchfile)
