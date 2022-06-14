Please read carefully the tutorial, if you run things without changing parameters in config files.. 
- ..to adapt to the data, paths etc.: it might just crash
- ..to adapt to the computational resources we have: you will end up waiting forever.

Full dnadna documentation available at https://mlgenetics.gitlab.io/dnadna/index.html

Quickstart tuto 1 command lines are available on the repo (you can check that out at first to have an overview of all steps)




# Notes on the fly:
## 1 Running tensorboard
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

## 2
... 


# References
- J Cury, B Haller, G Achaz, F Jay (2022). Simulation of bacterial populations with SLiM.   10.24072/pcjournal.72 - Peer Community Journal, Volume 2, article no. e7. [Link](dx.doi.org/10.24072/pcjournal.72)
  
  presents the simulator, based on SLiM to generate the datasets using [BactSLiMulator](https://github.com/jeanrjc/BacterialSlimulations) 


- T Sanchez, J Cury, G Charpiat, F Jay (2020). Deep learning for population size history inference: design, comparison and combination with approximate Bayesian computation. Molecular Ecology Ressources [Link](https://www.lri.fr/~fjay/papers/sanchez_etal_2020_MER.pdf)
  
  presents CustomCNN and SPIDNA networks


- T Sanchez*, EM Bray*, P Jobic, J Guez, A-C Letournel, G Charpiat, J Cury°, F Jay° (2021) Dnadna: Deep Neural Architecture for DNA - A deep learning framework for population genetic inference [Link](https://hal.archives-ouvertes.fr/hal-03352910v2)  
  
  preprint describing dnadna software:
  
  
- For building blocks of new networks, see: https://pytorch.org/docs/stable/nn.html
