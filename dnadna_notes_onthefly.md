Please read carefully the tutorial, if you run things without changing parameters in config files.. 
- ..to adapt to the data, paths etc.: it might just crash
- ..to adapt to the computational resources we have: you will end up waiting forever.

Full dnadna documentation available at https://mlgenetics.gitlab.io/dnadna/index.html

Quickstart tuto 1 command lines are available on the repo (you can check that out at first to have an overview of all steps)




# Notes on the fly:

- Don't mind the tqdm warning produced by the first import cell
- df_all_param  contains all the parameters for simulating the data (such as mutation, recombination, popualation, sizes, selection coefficient etc)
- df_params contains the parameters corresponding to 21 population sizes at 21 time steps

# Information
## 1.  Running tensorboard
After training you can visualize the result using tensorboard. 
In the terminal (after login to your session with ssh):

```
cd ~/workshop_materials/a14_dnadna
conda activate dnadna
tensorboard --logdir=DLModel --port 8899 --bind_all
```

Then connect with your browser to 
http://XXXX.compute-1.amazonaws.com:8899

where you replace XXXX by the adress you had received

## 2.  Understanding networks building blocks (to build your own)

https://pytorch.org/docs/stable/nn.html

In particular you can get inspiration from:
- https://pytorch.org/docs/stable/generated/torch.nn.Linear.html#torch.nn.Linear  for classical fully connected layer 
- https://pytorch.org/docs/stable/nn.html#convolution-layers  for convolutional layers
- https://pytorch.org/docs/stable/nn.html#pooling-layers  for pooling layers
- https://pytorch.org/docs/stable/nn.html#dropout-layers for adding dropout
... 

## 3. Implementing transforms
- Try yourself, then check some of the transform in this [repo](https://github.com/EvoGenomicsAI/Workshop/blob/main/dnadna/) 
- E.g. if you want use Matteo's ranking function (ranking lines) as a pluggin, see
https://github.com/EvoGenomicsAI/Workshop/blob/main/dnadna/sort_rows_freq.py
and https://github.com/EvoGenomicsAI/Workshop/blob/main/dnadna/DLModel_training_config_with_sort_rows.yml  (to check how it's called in the dataset_transforms section of the training config file)


# References
- J Cury, B Haller, G Achaz, F Jay (2022). Simulation of bacterial populations with SLiM.   10.24072/pcjournal.72 - Peer Community Journal, Volume 2, article no. e7. [Link](dx.doi.org/10.24072/pcjournal.72)
  
  presents the simulator, based on SLiM to generate the datasets using [BactSLiMulator](https://github.com/jeanrjc/BacterialSlimulations) 


- T Sanchez, J Cury, G Charpiat, F Jay (2020). Deep learning for population size history inference: design, comparison and combination with approximate Bayesian computation. Molecular Ecology Ressources [Link](https://www.lri.fr/~fjay/papers/sanchez_etal_2020_MER.pdf)
  
  presents CustomCNN and SPIDNA networks


- T Sanchez*, EM Bray*, P Jobic, J Guez, A-C Letournel, G Charpiat, J Cury°, F Jay° (2021) Dnadna: Deep Neural Architecture for DNA - A deep learning framework for population genetic inference [Link](https://hal.archives-ouvertes.fr/hal-03352910v2)  
  
  preprint describing dnadna software:
  
  
- For building blocks of new networks, see: https://pytorch.org/docs/stable/nn.html
