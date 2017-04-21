#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################
# v0.1 2 march 2017
#######################

import glob
import os
# numpy
# import numpy
# improved system calls
import random


# def get_uniform(min, max):
#     return numpy.random
# .uniform(min, max)

##############
# constants
##############
devices = 3
cycles = 120
exported_file_path = "variability.scs"
prefix = "\t+ cycle < "
prefix_end = "\t+ cycle < "
# + cycle < 1 ? 1.100 :
df_names = ["cycle_dependent_ron_p", "cycle_dependent_ron_n",
            "cycle_dependent_scl_p", "cycle_dependent_scl_n"]
df_mus = [1, 1, 5, 7]
df_sigmas = [0.4, 0.4, 1, 1.2]
dfs = len(df_names)

# uniform values:
# numpy.random.uniform(min, max, cycles)

# gaussian

############################
# preparing folder
############################
# folder where python is executed
executing_path = os.path.abspath(".")
# # create final folder
# if not os.path.exists(generated_files_folder):
#     os.makedirs(generated_files_folder)
# # change folder
# os.chdir(generated_files_folder)

fl_var = open(exported_file_path, 'w')
fl_var.write("simulator lang=spectre\n\n")
for i in range(0, devices):
    fl_var.write("\n\n// File " + str(i) + "\n\n")
    for df in range(0, dfs):
        fl_var.write("real " + df_names[df] +
                     "_" + str(i) + "( real cycle ) {\n")
        fl_var.write("\treturn\n")
        for c in range(0, cycles):
            new_val = random.gauss(df_mus[df], df_sigmas[df])
            fl_var.write(prefix + str(c) + " ? " + str(new_val) + " :\n")
        fl_var.write(prefix_end + str(df_mus[df]) + ";\n")
        fl_var.write("}\n\n")
fl_var.close()
