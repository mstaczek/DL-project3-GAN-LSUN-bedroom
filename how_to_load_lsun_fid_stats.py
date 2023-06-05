# source: https://github.com/GaParmar/clean-fid/tree/main

# usage:
# 1. download the stats files from the google drive link in the readme
# 2. put the files in the same directory as this script
# 3. run the script below

fid_filename = "lsun_bedroom_clean_custom_na.npz"

from shutil import copyfile
import os
from cleanfid import fid
os.makedirs(os.path.join(os.path.dirname(fid.__file__), 'stats'), exist_ok=True)
copyfile(fid_filename, os.path.join(os.path.dirname(fid.__file__), 'stats', fid_filename))

custom_name = "lsun_bedroom"
does_fid_exists_now = fid.test_stats_exists(custom_name, mode="clean")
print(f'Successfully loaded FID stats: {does_fid_exists_now}')

# generated files are copied from current dir into the stats dir of clean_fid
# I assume you do not have to copy the files every execution, but only once.


# 4. use the fid function as usual

generator_model = ... # your generator model
nz = ... # your latent space dimension, same as input length
num_gen = ... # number of generated images, say 1000

score = fid.compute_fid(gen=generator_model, dataset_name="lsun_bedroom", dataset_split="custom", z_dim=nz, num_gen=num_gen, num_workers=2)