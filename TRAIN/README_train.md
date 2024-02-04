# TRAIN folder

At the end, in the subfolder training_pdb_files will contains files named as:
- `pdb_id .txt`: file with extracted colum that are "ATOM" and belong tho the C3'
- `pdb_id_dist.txt`: with the pair base int he first column and in the second colum the IAD
- `trainset_dist.txt`: produced by the script trainning_script.py that have all the IAD of all the PDB file from the training set

The last file will be used to calculate the score using the formula in the TP paper.

