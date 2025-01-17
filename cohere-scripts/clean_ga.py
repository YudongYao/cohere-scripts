# #########################################################################
# Copyright (c) , UChicago Argonne, LLC. All rights reserved.             #
#                                                                         #
# See LICENSE file.                                                       #
# #########################################################################


"""
This script formats data for reconstruction according to configuration.
"""

import sys
import argparse
import os
import shutil


__author__ = "Barbara Frosik"
__copyright__ = "Copyright (c) 2016, UChicago Argonne, LLC."
__docformat__ = 'restructuredtext en'
__all__ = ['clean_gen',
           ]


def clean_gen(experiment_dir, leave_last_gen, rec_id=None):
    experiment_dir = experiment_dir.replace(os.sep, '/')
    def clean_res_dir(r_dir, keep_all):
        # find the last generation subdirectory in phasing results
        dirs = os.listdir(r_dir)
        gen_dirs = [subdir for subdir in dirs if subdir.startswith('g_')]
        if len(gen_dirs) == 0:
            return  # there are no phasing results generated by GA
        gen_dirs_dict = {int(gen_dir.split('_')[-1]): gen_dir for gen_dir in gen_dirs}
        last_gen = max(gen_dirs_dict, key=int)
        last_gen_dir = results_dir + '/' + gen_dirs_dict[last_gen]
        # remove last generation from dictionary
        gen_dirs_dict.pop(last_gen)
        # delete all subdirectories except the one with last generation
        for subdir in gen_dirs_dict.values():
            shutil.rmtree(results_dir + '/' + subdir)
        if keep_all is False:
            print('keep all', keep_all)
            # move best subdir in last generation to results_dir
            best = shutil.move(last_gen_dir + '/0', r_dir)
            # delete entire last generation subdirectory
            shutil.rmtree(last_gen_dir)

    if rec_id is None:
        post = ''
    else:
        post = '_' + rec_id

    results_dir = experiment_dir + '/results_phasing' + post
    clean_res_dir(results_dir, leave_last_gen)

    # clean also results_viz directory if exists
    results_dir = experiment_dir + '/results_viz' + post
    if os.path.isdir(results_dir):
        clean_res_dir(results_dir, leave_last_gen)


def main(arg):
    parser = argparse.ArgumentParser()
    parser.add_argument("experiment_dir", help="experiment directory")
    parser.add_argument("--leave_last_gen", choices=('True', 'False'), help="if True the entire last generation will be left, otherwise only the best")
    parser.add_argument("--rec_id", help="reconstruction id, a postfix to 'results_phasing_' directory")
    args = parser.parse_args()
    leave_last_gen = args.leave_last_gen == 'True'
    clean_gen(args.experiment_dir, leave_last_gen, rec_id=args.rec_id)


if __name__ == "__main__":
    main(sys.argv[1:])
