import unittest
import measurenary.utility as util
import pandas as pd
import numpy as np

class TestConvertEquation(unittest.TestCase):
    def setUp(self):
        self.vals = [12, 12.51, 0, '12', None]
        self.types = [1, 2, 3, '1', 4]
        self.gammas = [0.25, 0.002, 1, -5, 12]
        self.eq_types = ['S', 'D', 'Similarity', 'Distance', 12]

    def tearDown(self) -> None:
        return super().tearDown()

    def test_types_vals(self):
        # types 1
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[0]), -11)
        self.assertAlmostEqual(util.convertEquation(self.vals[1], self.types[0]), -11.51)
        self.assertAlmostEqual(util.convertEquation(self.vals[2], self.types[0]), 1)
        with self.assertRaises(TypeError):
            for _val in self.vals[3:]:
                util.convertEquation(_val, self.types[0])

        # types 2
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[1]), 121)
        self.assertAlmostEqual(util.convertEquation(self.vals[1], self.types[1]), 132.4801)
        self.assertAlmostEqual(util.convertEquation(self.vals[2], self.types[1]), 1)
        with self.assertRaises(TypeError):
            for _val in self.vals[3:]:
                util.convertEquation(_val, self.types[1])

        # types 3
        ## with eq_type S
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2]), 6.14421E-06)
        self.assertAlmostEqual(util.convertEquation(self.vals[1], self.types[2]), 3.68957E-06)
        self.assertAlmostEqual(util.convertEquation(self.vals[2], self.types[2]), 1)
        with self.assertRaises(TypeError):
            for _val in self.vals[3:]:
                util.convertEquation(_val, self.types[2])

        ## with eq_type D
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2], eq_type = self.eq_types[1]), -2.48490665)
        self.assertAlmostEqual(util.convertEquation(self.vals[1], self.types[2], eq_type = self.eq_types[1]), -2.526528324)
        with self.assertRaises(TypeError):
            for _val in self.vals[2:]:
                util.convertEquation(_val, self.types[2], eq_type=self.eq_types[1])

        with self.assertRaises(ValueError):
            for _type in self.types[3:]:
                util.convertEquation(self.vals[0], _type)
        
    def test_gammas(self):
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2], self.gammas[0]), 0.049787068)
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2], self.gammas[1]), 0.97628571)
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2], self.gammas[2]), 6.14421E-06)
        with self.assertRaises(ValueError):
            for _gamma in self.gammas[3:]:
                util.convertEquation(self.vals[0], self.types[2], _gamma)
                
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2], self.gammas[0], self.eq_types[1]), -9.939626599)
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2], self.gammas[1], self.eq_types[1]), -1242.453324894)
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2], self.gammas[2], self.eq_types[1]), -2.48490665)
        with self.assertRaises(ValueError):
            for _gamma in self.gammas[3:]:
                util.convertEquation(self.vals[0], self.types[2], _gamma, self.eq_types[1])

    def test_eq_type(self):
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2]), 6.14421E-06)
        self.assertAlmostEqual(util.convertEquation(self.vals[0], self.types[2], eq_type = self.eq_types[1]), -2.48490665)
        with self.assertRaises(Exception):
            for _eq_type in self.eq_types[2:]:
                util.convertEquation(self.vals[0], self.types[2], eq_type=_eq_type)

    
class TestMinMaxNormalization(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(data={'A': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            'B': [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                            'C': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                            'D': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                            'E': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                            'F': [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
                            'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'H': [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                            'I': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})
        self.dfs = [[1,2,3,4,5], 1, 'String', None]

    def tearDown(self) -> None:
        return super().tearDown()

    def test_df(self):
        self.assertIsInstance(util.minMaxNormalization(self.df), pd.DataFrame)
        self.assertIsInstance(util.minMaxNormalization(self.dfs[0]), np.ndarray)

        with self.assertRaises(ValueError):
            for _df in self.dfs[1:]:
                util.minMaxNormalization(_df)

class TestRandomSamplingData(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.DataFrame(data={'A': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            'B': [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                            'C': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                            'D': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                            'E': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                            'F': [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
                            'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'H': [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                            'I': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})
        
        self.df_false = [[1,2,3,4,5], 1, 'String', None]
        self.sample_rates = [0.1, 0.5, 1, 0, -1, 12, 'S', None]
        self.seeds = [None, 1, -5, 'String']

    def tearDown(self) -> None:
        return super().tearDown()

    def test_df(self):
        self.assertIsInstance(util.random_sampling_data(self.df), pd.DataFrame)
        
        with self.assertRaises(Exception):
            for _df in self.df_false:
                util.random_sampling_data(_df)

    def test_sample_rates(self):
        for _sample_rate in self.sample_rates[:3]:
            self.assertIsInstance(util.random_sampling_data(self.df, _sample_rate), pd.DataFrame)                

        with self.assertRaises(Exception):
            for _sample_rate in self.sample_rates[3:]:
                util.random_sampling_data(self.df, _sample_rate)
        
    def test_seed(self):
        for _seed in self.seeds[:2]:
            self.assertIsInstance(util.random_sampling_data(self.df, seed = _seed), pd.DataFrame)

        with self.assertRaises(ValueError):
            for _seed in self.seeds[2:]:
                util.random_sampling_data(self.df, seed = _seed)

class TestStratifiedSamplingData(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.DataFrame(data={'A': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            'B': [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                            'C': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                            'D': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                            'E': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                            'F': [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
                            'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'H': [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                            'I': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})
        
        self.df_false = [[1,2,3,4,5], 1, 'String', None]
        self.sample_rates = [0.1, 0.5, 1, 0, -1, 12, 'S', None]
        self.seeds = [None, 1, -5, 'String']

    def tearDown(self) -> None:
        return super().tearDown()

    def test_df(self):
        self.assertIsInstance(util.stratified_sampling_data(self.df), pd.DataFrame)
        
        with self.assertRaises(Exception):
            for _df in self.df_false:
                util.stratified_sampling_data(_df)

    def test_sample_rates(self):
        for _sample_rate in self.sample_rates[:3]:
            self.assertIsInstance(util.stratified_sampling_data(self.df, _sample_rate), pd.DataFrame)                

        with self.assertRaises(Exception):
            for _sample_rate in self.sample_rates[3:]:
                util.stratified_sampling_data(self.df, _sample_rate)
        
    def test_seed(self):
        for _seed in self.seeds[:2]:
            self.assertIsInstance(util.stratified_sampling_data(self.df, seed = _seed), pd.DataFrame)

        with self.assertRaises(ValueError):
            for _seed in self.seeds[2:]:
                util.stratified_sampling_data(self.df, seed = _seed)
    