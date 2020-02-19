import numpy as np
from scipy.stats import spearmanr

def corr(p1, p2):
    coefs = [np.corrcoef(p1[c], p2[c])[0,1] for c in cols]
    return np.mean(coefs)

def compute_rho(p1, p2):
    rhos = [spearmanr(p1[c], p2[c]).correlation for c in cols]
    # rhos = [spearmanr(p1[c], p2[c] + \
    #         np.random.normal(0, 1e-7, len(p2[c]))).correlation for c in cols]
    return np.mean(rhos)