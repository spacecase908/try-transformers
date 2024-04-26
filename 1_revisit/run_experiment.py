## Andrew Marione
## The purpose of this program is to execute a given experiment based on a configuration file. 
## I expect this to evolve a lot as I learn more about what experiments I want to run.

import pandas as pd
import numpy as np
import random


## Step 1 - import the configuration

## Step 2 - generate sequences

### Fetch the data

### Generate train sequences - take in the data and generate arrays with given sequence lenght and given subset of features
def generate_train_sequence(data, sequence_length, features):
  train_data = data['features'].values
  for start, stop in zip(## TODO - figure out what this zip should be)
    ## TODO - figure out what should be returned or yielded. Why use an iterator here?

### Generate test sequences


## Step 3 - generate model


## Step 4 - Run the actual experiment!!!

## i.e. for each sequence and model, perform this analysis

## Save results here


## RETURN - the results of the experiment
