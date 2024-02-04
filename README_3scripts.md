# The 3 scripts and its functions

## training_script.py

- `download_list_pdb()`:download the PDB file for the training set from the [RCSB PDB](https://www.rcsb.org) database
- `interatomic_distance()`: compute the IAD between base that are in the same chain and that are separated by at least 4 bases
- `concatene_trainset()`: concatene all the file pdb_id_dist.txt to have only one file to calculate then the log ratio of the observed frequencies and the reference frequency
- `frequencies_and_scores(): used to calculate the log ratio of the observed frequencies and the reference frequency


## plot_script.py

- `build_plot()`: to build a plot for each base pair with in the x axis the distance interval (0-20) and in the y axis the score


## scoring_plot.py

- `download_list_pdb()`:download the PDB file for the training set from the [RCSB PDB](https://www.rcsb.org) database and this function is imported from the `training_script.py` 
- `interatomic_distance()`: compute the IAD between base that are in the same chain and that are separated by at least 4 bases and this function is imported from the `training_script.py`
- `scoring()`: calculate the scoring according to the file AA.txt, AU.txt, ... obtained in the train.
- `calculation_GFE_estimation()`: it will calculate the estimated Gibbs free energy ( without making any interpolation...)

  
