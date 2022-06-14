from dnadna.transforms import Transform

class MyTransform(Transform):
    def __call__(self, data):
        sample, lp, scen = data
        snp, pos = sample.snp, sample.pos
        
        idx = np.random.choice(snp.n_indiv, size=snp.n_indiv, replace=False)
        
        sample = sample.copy_with(snp=snp[idx, :], pos=pos)
        return (sample, lp, scen)
