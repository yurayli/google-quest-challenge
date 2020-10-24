# Google quest challenge

----
solution to the competition https://www.kaggle.com/c/google-quest-challenge. 240 place with no post-processing. With post-processing, the output of the model could be in the silver medal zone.

## Overview
### Task
Computers are good at answering questions with single, verifiable answers. But humans are often still better at answering questions about opinions, recommendations, or personal experiences. The task is predictive modeling for natural language understanding about intents of questions, and how they answered, i.e. helpful, interesting, or well-written. Evaluated by [Spearman's correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient).

### Networks
* BERT
* Pooling and then concatenation of last few hidden states from BERT
* Multi-sample dropout

<img src="arch.png" width="460"/>

### Data
* 5-fold split
* Augmentation with multiple truncations of the sequence (head, tail, mix)
* TTA, same from multiple truncations

### Optimizer
* AdamW with linear warmup and linear annealing learning rate schedule
* BCE Loss for 30 multi-labels


### Environment
kaggle kernel with nvidia tesla p100  
nvidia [apex](https://www.kaggle.com/shutil/nvidia-apex)  
pytorch 1.2.0  
