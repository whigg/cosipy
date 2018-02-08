"""
 This is the COSIPY configuration (init) file.
 Please make your changes here.
"""
from pathlib import Path

''' source code for repository '''
# input_netcdf=input("Path (inclusive directories) to NetCDF input: ")
# output_netcdf=input("Path (inclusive directories) to NetCDF output: ")

'''example 1D file'''
input_netcdf= 'input/input_COSIPY-example.nc'
output_netcdf = 'output/output_COSIPY-example.nc'



''' 
    source code for local development
    only used for local development
    clean for master branch!
'''
# home = str(Path.home())
# folder='/Seafile/diss/io/'
#
# # example Martell 2017
# input_Martell = 'input/input_Martell_2017.nc'
# output_Martell = 'output/output_Martell_2017.nc'
#
# # example 1D Setup
# input_Halji = 'intput/input_prepro_HAR_Halji_10_2000-10_2011_ohneKorrekturen.nc'
# output_Halji = 'ouput/output_HAR_Halji_10_2000-10_2011_ohneKorrekturen.nc'
#
# # example 2D Setup
# input_example_2D='intput/input_COSIPY2D-mask_values-example.nc'
# output_example_2D= 'output/output_COSIPY2D-mask_values-example.nc'
#
# # select setup!!!
# input_netcdf=home+folder+input_example_1D
# output_netcdf=home+folder+output_example_1D


time_start = 0                                      # time index to start
time_end = 7200                                     # len(T2) usually the length of the time series
dt = 3600                                           # 3600, 7200, 10800 [s] length of time step per iteration in seconds

debug_level = 0                                     # DEBUG levels: 0, 10, 20, 30

merging_level = 0                                   # Merge layers with similar properties:
                                                    # 0 = False
                                                    # 1 = 5. [kg m^-3] and 0.05 [K]
                                                    # 2 = 10. and 0.1

merge_snow_threshold = 0.02                         # Minimal height of layer [m]:
                                                    # thin layers rise computational needs
                                                    # of upwind schemes (e.g. heatEquation)
''' required variables '''

temperature_bottom = 268                            # bottom temperature [K]

c_stab = 0.3                                        # cfl criteria


                                                    # ToDo strings with names for parametrisations