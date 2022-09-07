import unittest
from measurenary import AgglomerativeBestMeasure
import pandas as pd
import numpy as np

class TestAgglomerativeBestMeasure(unittest.TestCase):
    def setUp(self) -> None:
        self.agglomerative_best = AgglomerativeBestMeasure()
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
        self.df_false = [[], 120, np.array([1,2,3])]
        self.n_clusters = [-1, 0, 1, 2, 3, 11, 100]
        self.affinity_string = ['manhattan', 'intersection', 'yuleq', 'all', '', 'lorem impsum']
        self.affinity_list = [['manhattan'], ['intersection'], ['yuleq', 'intersection'], ['all'], ['lorem impsum'], []]
        self.linkage = ['complete', 'average', 'single', 'lorem impsum', [], '', 'ward']

    def tearDown(self) -> None:
        pass

    def test_df(self):
        with self.assertRaises(Exception):
            for _df in self.df_false:
                self.agglomerative_best.fit(_df)
        
        self.agglomerative_best.fit(self.df)
        self.assertIsInstance(self.agglomerative_best.get_result(), pd.DataFrame)

    def test_n_clusters(self):
        for _n_clusters in self.n_clusters[:3]:
            with self.assertRaises(Exception):
                self.agglomerative_best.fit(self.df, _n_clusters)

        for _n_clusters in self.n_clusters[3:5]:
            self.agglomerative_best.fit(self.df, _n_clusters)
            self.assertIsInstance(self.agglomerative_best.get_result(), pd.DataFrame)

        for _n_clusters in self.n_clusters[5:]:
            with self.assertRaises(ValueError):
                self.agglomerative_best.fit(self.df, _n_clusters)

    def test_affinity(self):
        for _affinity in self.affinity_string[:4]:
            self.agglomerative_best.fit(self.df, affinity=_affinity)
            self.assertIsInstance(self.agglomerative_best.get_result(), pd.DataFrame)

        for _affinity in self.affinity_list[:4]:
            self.agglomerative_best.fit(self.df, affinity=_affinity)
            self.assertIsInstance(self.agglomerative_best.get_result(), pd.DataFrame)

        with self.assertRaises(Exception):
            for _affinity in self.affinity_string[4:]:
                self.agglomerative_best.fit(self.df, affinity=_affinity)

            for _affinity in self.affinity_list[4:]:
                self.agglomerative_best.fit(self.df, affinity=_affinity)

    def test_linkage(self):
        for _linkage in self.linkage[:3]:
            self.agglomerative_best.fit(self.df, linkage=_linkage)
            self.assertIsInstance(self.agglomerative_best.get_result(), pd.DataFrame)

        for _linkage in self.linkage[3:]:
            with self.assertRaises(Exception):
                self.agglomerative_best.fit(self.df, linkage=_linkage)