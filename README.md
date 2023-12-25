# graph-invariants-leukemia-detection

This repo contains of 4 parts that represent every part of the modelling process:

* **data_augmentation**
* **invariants_generation**
* **feature_analysis**
* **model_training_evaluation**

Each part has been placed into the corresponding folder. There you can find .ipynb notebooks that contains all the details. 

**Steps to run the code:**

1. All code was tested on Python 3.10. Please be sure that you have installed all the recommended packages from ```requirements.txt``` file by using command:

```
pip install -r requirements.txt
```

2. **data_augmentation**: To create your own augmented dataset you need to use base dataset as input. In the paper, we have used ALL_IDB1 dataset from https://scotti.di.unimi.it/all/

3. **invariants_generation**: Some invariants from the list require quite complex computations (for example, global efficiency) and therefore one need to wait for several hours until full completion of invariants generation according to the script. 

4. **feature_analysis**: For reproduction of this part one will need to generate all the features from the previous step. However, if you desire to directly train the model and don't spend much time on generating all features - there is a possibility to generate only the features described in paper.

5. **model_training_evaluation**: This step should be straight-forward as long as you have installed all the recommended packages and went through all the previous steps. Worth to mention that GPU is not needed for the code execution, everything was tested on CPU. 
