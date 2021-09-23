thread_count = 8
batch_size = 1000
k = 3
cov_k = 15
err_file = "error.txt"
log_file = "log.txt"

# progress bar descriptions
plas_bar_desc  = "plasmid      "
chrom_bar_desc = "chromosome   "
ex_plas_bar_desc = "extra plasmid"

# tool paths
seq2vec_path = "seq2vec"
dsk_path = "dsk"
dsk2ascii_path = "dsk2ascii"

# fragment files
plas_write_path = "/media/gayal/Programming/FYP/code/preprocess/results/plasmid/Data/fragments" 
chrom_write_path = "/media/gayal/Programming/FYP/code/preprocess/results/chromosome/Data/fragments"
extra_plasmid_write_path = "/media/gayal/Programming/FYP/code/preprocess/results/extra-plasmid/Data/fragments"

# kmer files
plas_kmer_write_path = "results/plasmid/Data/kmers"
chrom_kmer_write_path = "results/chromosome/Data/kmers"
ex_plas_kmer_write_path = "results/extra-plasmid/Data/kmers"

# coverage files
plas_coverage_h5_path = "results/plasmid/extra/h5"
chrom_coverage_h5_path = "results/chromosome/extra/h5"
ex_plas_coverage_h5_path = "results/extra-plasmid/extra/h5"

plas_coverage_write_path = "results/plasmid/Data/coverage"
chrom_coverage_write_path = "results/chromosome/Data/coverage"
ex_plas_coverage_write_path = "results/extra-plasmid/Data/coverage"
