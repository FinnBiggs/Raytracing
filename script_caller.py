import os
import numpy as np

file_name = "data.txt"

def set_file_name(f):
    file_name = f

def clear_file():
    with open(file_name, "w") as d:
        pass

# usage:
# 	lens_filename	see README_lens.txt for prescription
# 	z_init		initial z location of ray to trace
# 	y_init		initial y location of ray to trace
# 	slope_init	initial tangent (delta_y/delta_z) of ray
# 	[z_screen]	optional screen location for analysis of intercept
def one_2d(lens_filename, z_init, y_init, slope_init, z_screen = None):
    cmd_str = "python one_2d.py {} {} {} {}".format(lens_filename, z_init, y_init, slope_init)
    if z_screen is not None:
        cmd_str += " {}".format(z_screen)
    cmd_str += " >> {}".format(file_name)
    os.system(cmd_str)

# usage:
# 	lens_filename	see README_lens.txt for prescription
# 	z_init		initial z location of ray average (center) to trace
# 	y_init		initial y location of ray average (center) to trace
# 	slope_init	initial tangent (delta_y/delta_z) of parallel ray set
# 	offset		+/- y offset around center (separation is twice this)
# 	[z_screen]	optional screen location for analysis of ray positions
def par_2d(lens_filename, z_init, y_init, slope_init, offset, z_screen = None):
    cmd_str = "python par_2d.py {} {} {} {} {}".format(lens_filename, z_init, y_init, slope_init, offset)
    if z_screen is not None:
        cmd_str += " {}".format(z_screen)
    cmd_str += " >> {}".format(file_name)
    os.system(cmd_str)

# usage:
# 	lens_filename	see README_lens.txt for prescription
# 	z_init		z location of ray intersection (point)
# 	y_init		y location of ray intersection (point)
# 	slope_init	initial tangent (delt_y/delt_z) of average (centerline)
# 	offset_angle	+/- slope offset around centerline (sep. is twice this)
# 	[z_screen]	optional screen location for analysis of ray positions
def point_2d(lens_filename, z_init, y_init, slope_init, offset_angle, z_screen=None):
    cmd_str = "python point_2d.py {} {} {} {} {}".format(lens_filename, z_init, y_init, slope_init, offset_angle)
    if z_screen is not None:
        cmd_str += " {}".format(z_screen)
    cmd_str += " >> {}".format(file_name)
    os.system(cmd_str)