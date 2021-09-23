import subprocess as sp

from progress_bar import *
from helpers import timestamp, create_coverage_files
from constants import *
import os

def generate_coverage(k, frag_path, h5_path, write_path, pb_desc):
    try:
        progress_bar = create_progress_bar(pb_desc)
        for filename in os.listdir(frag_path):
            name = filename.split(".")[0]
            frag_file = f"{frag_path}/{filename}"
            h5_file = f"{h5_path}/{name}.h5"
            write_file = f"{write_path}/{name}"
            args = [
                dsk_path,
                '-file', str(frag_file),
                '-out', str(h5_file),
                '-nb-cores', str(thread_count),
                '-kmer-size', str(k),
            ]
            proc = sp.run(args, stdout=sp.PIPE, stderr=sp.PIPE)
            args = [
                dsk2ascii_path,
                '-file', str(h5_file),
                '-out', str(write_file),
                '-nb-cores', str(thread_count),
            ]
            proc = sp.run(args, stdout=sp.PIPE, stderr=sp.PIPE)

            update_progress_bar(progress_bar, batch_size)

        close_progress_bar(progress_bar)
    except Exception as err:
        with open(err_file, 'a') as fout:
            fout.write(f"{timestamp()} Error using dsk for file {name} {err}\n")

if __name__ == "__main__":
    create_coverage_files()
    generate_coverage(cov_k, plas_write_path, plas_coverage_h5_path, plas_coverage_write_path, plas_bar_desc)
    generate_coverage(cov_k, chrom_write_path, chrom_coverage_h5_path, chrom_coverage_write_path, chrom_bar_desc)
    generate_coverage(cov_k, extra_plasmid_write_path, ex_plas_coverage_h5_path, ex_plas_coverage_write_path, ex_plas_bar_desc)
