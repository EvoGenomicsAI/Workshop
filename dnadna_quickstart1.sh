# For detailed explanation of each step see dnadna documentation
# https://mlgenetics.gitlab.io/dnadna/
# This script corresponds to tutorial https://mlgenetics.gitlab.io/dnadna/introduction.html#quickstart-tutorial

# Note that at the end of each command a prompted message will suggest what to do next

# Simulate toy dataset
dnadna simulation init my_dataset one_event
dnadna simulation run my_dataset/my_dataset_simulation_config.yml

# Initialize dnadna config file for this dataset
dnadna init --simulation-config=my_dataset/my_dataset_simulation_config.yml my_model

# Preprocess the data (filtering, training/val/test split, ...)
dnadna preprocess my_model/my_model_preprocessing_config.yml

# Train a network
dnadna train my_model/my_model_training_config.yml

# Prediction on a dataset
# (change to wanted run and wanted target data)
dnadna predict my_model/run_000/my_model_run_000_best_net.pth my_dataset/scenario_04/*.npz

