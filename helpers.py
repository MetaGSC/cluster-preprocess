import os

from constants import *

def timestamp():
    import datetime
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def create_dir_if_needed(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_kmer_files():
    # kmer files
    create_dir_if_needed(plas_kmer_write_path)
    create_dir_if_needed(chrom_kmer_write_path)
    create_dir_if_needed(ex_plas_kmer_write_path)

def create_coverage_files():
    create_dir_if_needed(plas_coverage_h5_path)
    create_dir_if_needed(chrom_coverage_h5_path)
    create_dir_if_needed(ex_plas_coverage_h5_path)
    create_dir_if_needed(plas_coverage_write_path)
    create_dir_if_needed(chrom_coverage_write_path)
    create_dir_if_needed(ex_plas_coverage_write_path)
