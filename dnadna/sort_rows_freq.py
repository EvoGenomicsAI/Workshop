from dnadna.transforms import Transform
import numpy as np

class sort_rows_freq(Transform):
    def __call__(self, data):
        sample, lp, scen = data
        snp, pos = sample.snp, sample.pos
        
        uniques, counts = np.unique(snp, return_counts=True, axis=0)
        snp_sorted = np.array([uniques[j] for j in counts.argsort()[::-1] for z in range(counts[j])])
       
        sample = sample.copy_with(snp=snp_sorted, pos=pos)
        return (sample, lp, scen)
