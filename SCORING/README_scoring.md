# SCORING folder

At the end, in the folder training_pdb_files will contains files named as:
-`list_test_pdb.txt`: "list" that contains one id of PDB (list because to use the same function from trainsing_script.py)
- `2O3Y.pdb`: PDB file downloaded from the [RCSB PDB](https://www.rcsb.org) database using the function `download_pdf_file()` from the `training_script.py` 
- `2O3Y.txt`: file with the extracted column "ATOM", "C3'" ...
- `2O3Y_dist.txt`: file with the IAD computed bu the function `interatomic_distance()` from the `training_script.py`
