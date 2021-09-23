# cluster-preprocess

## Prerequisites

Following tools should be installed.

-   **Seq2Vec** - used for kmer count
    
-   **DSK** - used for calculate the kmer coverage
        
-   **tqdm** - used to display runtime progress

### SEQ2VEC 
refer https://github.com/anuradhawick/seq2vec#readme

### DSK
refer https://github.com/GATB/dsk#readme

### TQDM
```
conda install -c conda-forge tqdm
```

> [OPTIONAL] Add the paths to the executables to your path for tools `seq2vec` and `dsk`, `dsk2ascii` in dsk.

## Usage

1. Provide the paths for the plasmid, chromosome, extra-plasmid fragments in the constants file.
    ``` python
    plas_write_path = "/path/to/fragments" 
    chrom_write_path = "/path/to/fragments" 
    extra_plasmid_write_path = "/path/to/fragments"
    ```

2. If you haven't added the paths to the executables to your path, add them to the constants file.
    ``` python
    seq2vec_path = "/path/to/executable"
    dsk_path = "/path/to/executable"
    dsk2ascii_path = "/path/to/executable"
    ```

3. Change the `thread_count`, `batch_size`, `k = 3`, `cov_k = 15` parameters as necessary in the constants file.

   ```python
   thread_count = 8
   batch_size = 1000
   k = 3    # k for kmer count 
   cov_k = 15   # k for kmer coverage
   ```

4. Executing each of the files mentioned below provide the results. The output will be a folder `result` in the current directory.

   | File        | Description                                                  |
   | ----------- | :----------------------------------------------------------- |
   | [trinucleotide.py](./trinucleotide.py)     | The kmer frequencies(k=3) of each fragment  |
   | [kmer-coverage.py](./kmer-coverage.py)     | Kmer coverage(k=15) of each fragment        |
