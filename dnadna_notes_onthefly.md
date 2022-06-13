Read carefully the tutorial, if you run things without changing a few parameters 
- to adapt to the data, paths etc., it might just crash
- to adapt to the computational resources we have, you will end up waiting forever.

Full dnadna documentation available at https://mlgenetics.gitlab.io/dnadna/index.html

Quickstart tuto 1 command lines are available on the repo (you can check that out at first to have an overview of all steps)




Notes on the fly:
After training you can visualize the result using tensorboard. In a terminal run:
tensorboard --logdir=DLModel --port 8601 --bind_all
http://XXXX.compute-1.amazonaws.com:8601
Replace XXXX by the adress you had received


