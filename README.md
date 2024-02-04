# Project on RNA folding problem 2023-2024

_by Kamély LUMIÈRE_

This repository contains all the scripts  used to do this project, aimed to calculate the estimated Gibbs free energy of the RNA conformation of one pdb file. 


## Install


Install the required packages with the correct versions
```markdown
$ pip install -r requirements.txt
```

Clone the project 
```markdown
$ git clone https://github.com/klumiere/RNA_fold.git
```

Then, go to the folder `RNA_fold` and run this following command:
```markdown
$ chmod a+x training_script.py plot_script.py scoring_script.py
```
 

## 1/ Training

Run the script `training_script.py`.


```markdown
$ ./training_script.py ./TRAIN/train_pdb_list.txt ./TRAIN/training_pdb_files/ ./PLOT/ trainset_dist
```
- This will allow you to download PDB files for the trainset from the [RCSB PDB](https://www.rcsb.org) database from a list containing PDB identifiers.
- This will generate 20 files for 20 pairs of bases in which each line corresponds to an interval of interactomic distance in the folder `PLOT`

## 2/ Plot

Run the script `plot_script.py` 
```markdown
$ ./plot_script.py ./PLOT/
```

## 3/ Scoring

Run the script `scoring_script.py`
```markdown
$ ./scoring_script.py ./SCORING/list_test_pdb.txt ./SCORING/ ./SCORING/2O3Y.txt ./PLOT/ ./score_without_interpolation.txt
```


