# SAE-aerothon-2022

Every year SAE holds a Aerothon in which the participants are given certain tasks that need to be completed onboard a UAV/UAS.

The task for Aerothon 2022 was to "Develop an autonomous aerial system that can detect a target on a field, among dummy targets, and is able to drop a payload on the center of the target."

### Technologies Used -
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Raspberry Pi Badge](https://img.shields.io/badge/Raspberry%20Pi-A22846?logo=raspberrypi&logoColor=fff&style=for-the-badge)

### Workflow-

- Detect the target in the open field
- Find the center of the target and calculate the GPS coordinate for the same
- Make the drone fixate on the GPS coodinate
- Repeat the first 3 steps, to reduce error
- DROP!!

### Implementation-

The entire system was deployed on a Raspberry Pi.

A default flight path is pre-set, during which when a taget is detected, certain commmands are run.
The Models folder contains a custom implementation of UNET proposed by [Ronneberger et al.](https://arxiv.org/pdf/1505.04597.pdf) using Tensorflow. The model was trained over a custom dataset of the target which was shot through a drone.
From the output of the model, we first find the last and first pixel of the mask which allows us to find the center of the target(i.e. square) using [helper.py](https://github.com/AvyaRathod/SAE-aerothon-2022/blob/main/helper.py).
We then calcuate the GPS coordinate.
GPS lock is set and the process is continued for n number of iterations to reduce the random error.
Then the payload in dropped to the center of the target.🤞
