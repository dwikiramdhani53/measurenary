import unittest
from measurenary import PairBestMeasure
import pandas as pd
import numpy as np

class TestPairBestMeasure(unittest.TestCase):
    def setUp(self) -> None:
        self.pair_best = PairBestMeasure()
        self.df = pd.DataFrame(data={'A': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            'B': [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                            'C': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                            'D': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                            'E': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                            'F': [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
                            'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'H': [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                            'I': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'Target': [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]})
        self.df_false = [[], 120, np.array([1,2,3]), 'this is dataframe']
        self.num_sample = [-1, 0.4, 100, 0, 1, 2, 4, 10]
        self.use_seeds = [True, False, 'True', 'False']

    def tearDown(self) -> None:
        pass

    def test_df(self):
        with self.assertRaises(Exception):
            for _df in self.df_false:
                self.pair_best.fit(_df, num_sample=2)

        self.pair_best.fit(self.df, num_sample=2)
        self.assertIsInstance(self.pair_best.get_result(), pd.DataFrame)

    def test_use_seed(self):
        for _use_seed in self.use_seeds[2:]:
            with self.assertRaises(Exception):
                self.pair_best.fit(self.df, use_seed=_use_seed, num_sample=10)
        
        for _use_seed in self.use_seeds[:2]:
            self.pair_best.fit(self.df, use_seed=_use_seed, num_sample=10)
            self.assertIsInstance(self.pair_best.get_result(), pd.DataFrame)

    def test_num_sample(self):
        for _num_sample in self.num_sample[:4]:
            with self.assertRaises(ValueError):
                self.pair_best.fit(self.df, num_sample=_num_sample)

        for _num_sample in self.num_sample[4:]:
            self.pair_best.fit(self.df, num_sample=_num_sample)
            self.assertIsInstance(self.pair_best.get_result(), pd.DataFrame)
