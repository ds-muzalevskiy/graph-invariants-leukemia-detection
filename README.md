## Image Classification of Leukemic Cells Using Invariants of Triangle-Free Graphs as Synthetic Features
### Dmitry Muzalevskiy and Ivan Torshin.

This repo consists of 4 parts that represent every part of the modelling process:

* **data_augmentation**
* **invariants_generation**
* **feature_analysis**
* **model_training_evaluation**

Each part has been placed into the corresponding folder. There you can find .ipynb notebooks that contains all the details. 

**Steps to run the code:**

1. All code was tested on Python ```3.10.12```. We recommend also use Anaconda (code was tested using version ```23.3.1```). Please be sure that you have installed all the recommended packages from ```requirements.txt``` file by using command:

```
pip install -r requirements.txt
```

2. **data_augmentation**: To create your own augmented dataset you need to use base dataset as input. In the paper, we have used ALL_IDB1 dataset (https://scotti.di.unimi.it/all/). Before running this part - download the ALL_IDB1 dataset (108 images) and put into the ```init_cells``` folder. Then after running the command all the augmented images will appear in the ```cells``` folder (3231 images).  
```
python augmentation.py
```
**Important**: please be sure that before running ```augmentation.py``` all you initial input images do not contain ```Im00``` or ```Im0``` parts in their names. The filesnames should look like ```1_1```, ```2_1```, ... , ```107_0```, ```108_0```.

3. **invariants_generation**: If you did everything correctly on the previous step you should get the augmented images placed in ```cells``` folder. Their names should look like ```1_1_0_1048```, ```1_1_0_139```, ... , ```108_0_0_965```, ```108_0_0_972```. Some invariants from the list require quite complex computations (for example, global efficiency) and therefore one need to wait for several hours until full completion of invariants generation according to the script. 

4. **feature_analysis**: For reproduction of this part one will need to generate all the features from the previous step. However, if you desire to directly train the model and don't spend much time on generating all features - there is a possibility to generate only the features described in paper.

5. **model_training_evaluation**: This step should be straight-forward as long as you have installed all the recommended packages and went through all the previous steps. Worth to mention that GPU is not needed for the code execution, everything was tested on CPU.

**Comments about model training**
In principle, if you are planning to preprocess your incoming test images and augment them before actual prediction (there can be some cases of such preprocessing pipelines) - the results of the model holds even with smaller amount of augmented train data (we have received comparable results using ```2500``` images).
If you are planning to use classical variation of the preprocessing pipeline with augmented train and raw test - please be sure that you will have bigger augmented train dataset. Comparable results were received with ```10000``` images in the training set. We also have tested the model using ```20000``` augmented images in training set and noticed more stable behaviour. So therefore if you have enough computational resources for generating bigger augmented train set (```20000``` images or more) and calculate invariants on it - we definitely can recommend to do so. We also recommend using not only augmented images in the training dataset, but also include the original images on which they are based, to increase stability (for example, if you have splitted 108 initial images randomly and end up with 80 images in training set and perform data augmentation based on these 80 images - be sure to use them in the resulting training set).

Dealing with bigger datasets you might want to use other boosting algorithms so therefore we can recommend using either **LightGBM** or **NGBoost** in such cases.

