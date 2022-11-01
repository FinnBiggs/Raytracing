import os
import numpy as np

# usage:
# 	lens_filename	see README_lens.txt for prescription
# 	z_init		initial z location of ray to trace
# 	y_init		initial y location of ray to trace
# 	slope_init	initial tangent (delta_y/delta_z) of ray
# 	[z_screen]	optional screen location for analysis of intercept
def one_2d(lens_filename, z_init, y_init, slope_init, z_screen = None):
    if z_screen is not None:
        os.system( "python one_2d.py {} {} {} {} {}".format(lens_filename, z_init, y_init, slope_init, z_screen) )
    else:
        os.system( "python one_2d.py {} {} {} {}".format(lens_filename, z_init, y_init, slope_init) )

# usage:
# 	lens_filename	see README_lens.txt for prescription
# 	z_init		initial z location of ray average (center) to trace
# 	y_init		initial y location of ray average (center) to trace
# 	slope_init	initial tangent (delta_y/delta_z) of parallel ray set
# 	offset		+/- y offset around center (separation is twice this)
# 	[z_screen]	optional screen location for analysis of ray positions
def par_2d(lens_filename, z_init, y_init, slope_init, offset, z_screen = None):
    if z_screen is not None:
        os.system( "python par_2d.py {} {} {} {} {} {}".format(lens_filename, z_init, y_init, slope_init, offset, z_screen) )
    else:
        os.system( "python par_2d.py {} {} {} {} {}".format(lens_filename, z_init, y_init, slope_init, offset) )

# usage:
# 	lens_filename	see README_lens.txt for prescription
# 	z_init		z location of ray intersection (point)
# 	y_init		y location of ray intersection (point)
# 	slope_init	initial tangent (delt_y/delt_z) of average (centerline)
# 	offset_angle	+/- slope offset around centerline (sep. is twice this)
# 	[z_screen]	optional screen location for analysis of ray positions
def point_2d(lens_filename, z_init, y_init, slope_init, offset_angle, z_screen=None):
    if z_screen is not None:
        os.system( "python point_2d.py {} {} {} {} {} {}".format(lens_filename, z_init, y_init, slope_init, offset_angle, z_screen) )
    else:
        os.system( "python point_2d.py {} {} {} {} {}".format(lens_filename, z_init, y_init, slope_init, offset_angle) )