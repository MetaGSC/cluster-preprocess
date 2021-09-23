import os

from constants import *

# def find_mean(sum, divisor):
#     if divisor == 0:
#         return 0
#     return float(sum)/divisor

def timestamp():
    import datetime
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def create_dir_if_needed(path):
    if not os.path.exists(path):
        os.makedirs(path)

def delete_dir_if_exist(path):
  if os.path.exists(path):
    os.remove(path)

def create_kmer_files():
    # kmer files
    create_dir_if_needed(plas_7mer_write_path)
    create_dir_if_needed(chrom_7mer_write_path)
    create_dir_if_needed(ex_plas_7mer_write_path)
