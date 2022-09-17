"""
Pair Best Similarity/Distance.
---------------------------------------

This module contains classes to find the best similarity/distance equation based on the target match.
"""

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_curve, auc
from tqdm.autonotebook import tqdm
import random
import measurenary.similarity as sim
import measurenary.distance as dis
from measurenary.utility import *

# disable runtime warning
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

class PairBestMeasure():
    """
    Class to get the best similarity and distance based on target pairs.

    Parameters
    ----------
    show_result : bool, optional
        Set True to show result. The default is False.
    result_count : int, optional
        Set the number of result to show. The default is 5.
    """
    def __init__(self, show_result = False, result_count = 5):
        # set up all similarity and dissimilarity equation
        self.f_sim = [val for _, val in sim.__dict__.items() if callable(val)][6:]
        self.f_dis = [val for _, val in dis.__dict__.items() if callable(val)][3:]
        self.name_f_sim = [eq.__name__ + ' similarity' for eq in self.f_sim]
        self.name_f_dis = [eq.__name__ + ' distance' for eq in self.f_dis]
        self.result_count = result_count
        self.show_result = show_result

    def _find_confusion_matrix(self, df_source, index_start, index_end):
        """
        method to generate a confusion matrix and similarity/distance results from every record pair in data binary dataframe on specific index.

        Parameters
        ----------
        df_source : pandas.DataFrame
            dataframe source
        index_start : int
            start index
        index_end : int
            end index

        Returns
        -------
        list
            List of confusion matrix and similarity/distance values.
        """
        # initiate return list
        res_list = []
        nan_value_equation = []

        # loop for every row in data
        for index, row in tqdm(df_source.iloc[index_start:, :].iterrows()):
            if index == index_end:
                break
            # print('sample', index, 'of', index_end)
            for _index, _row in df_source.iloc[index+1:, :].iterrows():
                # generate a confusion matrix
                cm = confusion_matrix(row.to_list(), _row.to_list()).ravel()
                # match the reference column
                ## 1 if match
                ## 0 if it doesn't match
                is_match = True if int(df_source.iloc[index, -1]) == int(df_source.iloc[_index, -1]) else False
                if not isinstance(is_match, bool):
                    print(index, _index, is_match)
                
                # calculate the similarity/distance value based on confusion matrix before
                _sim = []
                for _, f in enumerate(self.f_sim):
                    try:
                        sim = f(cm[3], cm[2], cm[1], cm[0], sum(cm))
                        if sim == None: 
                            sim = np.nan
                            nan_value_equation.append(f.__name__ + ' similarity')
                            # continue
                    except:
                        sim = np.nan
                        nan_value_equation.append(f.__name__ + ' similarity')
                        # continue
                    _sim.append(sim)

                for _, f in enumerate(self.f_dis):
                    try:
                        dis = 1 - (f(cm[3], cm[2], cm[1], cm[0], sum(cm)))**2
                        if dis == None:
                            dis = np.nan
                            nan_value_equation.append(f.__name__ + ' distance')
                            # continue
                    except:
                        dis = np.nan
                        nan_value_equation.append(f.__name__ + ' distance')
                        # continue
                    _sim.append(dis)

                # combine confusion matrix and similarity/distance result
                res_list.append([index, _index, cm.ravel(), is_match] + _sim)
        
        return res_list, set(nan_value_equation)

    def fit(self, df, use_seed=False, num_sample=20, **kwargs):
        """
        Train data to generate a suitable similarity/distance equation.

        Parameters
        ----------
        df : pandas.DataFrame
            dataframe source
        use_seed : bool, optional
            Set True to use seed. The default is False.
        num_sample : int, optional
            Set the number of sample to generate. The default is 20.

        Returns
        -------
        None
        """
        # set up show result and result count in kwargs
        if 'show_result' in kwargs:
            self.show_result = kwargs['show_result']
        if 'result_count' in kwargs:
            self.result_count = kwargs['result_count']

        # check boolean value of use_seed
        if not isinstance(use_seed, bool):
            raise Exception('use_seed must be boolean')

        # check df is pandas dataframe
        if not isinstance(df, pd.DataFrame):
            raise Exception('df must be pandas dataframe')

        # check num sample
        if not isinstance(num_sample, int):
            raise Exception('num_sample must be integer')
        if num_sample > df.shape[0]:
            raise Exception('num_sample must be smaller than df.shape[0]')
        if num_sample <= 0:
            raise Exception('num_sample must be greater than 0')
        
        # set up index start and end
        index_start = 0
        index_end = df.shape[0]
        
        # print all parameters
        print('use_seed: ', use_seed)
        print('num_sample: ', num_sample)
        print()

        # get number of record
        n_row = len(df)

        res_list, nan_value_equation = self._find_confusion_matrix(df, index_start, index_end)
        res_arr = np.array(res_list, dtype=object)

        # set up equation function name
        name_f_sim, name_f_dis = self.name_f_sim, self.name_f_dis

        # create a dataframe from _find_confusion_matrix list result
        res_df = pd.DataFrame(res_arr, columns=['i', 'j', 'confussion_matrix', 'is_match'] + name_f_sim + name_f_dis)

        # print excluded equation that produce nan
        if len(nan_value_equation) != 0:
            name_f_sim = [e for e in name_f_sim if e not in nan_value_equation]
            name_f_dis = [e for e in name_f_dis if e not in nan_value_equation]
            print(UserWarning('{} not included, it produce nan value'.format(nan_value_equation)))
            # remove column
            res_df.drop(list(nan_value_equation), axis=1, inplace=True)

        # get value of similarity/distance measurement
        sim_df = pd.DataFrame(res_df.iloc[:, 4:], columns=name_f_sim + name_f_dis)

        # get column name that has nan in sim_df and drop it
        column_nan = sim_df.columns[sim_df.isnull().any()].tolist()
        sim_df.drop(column_nan, axis=1, inplace=True)

        # change dtype to float for better calculation
        sim_df = sim_df.astype(float)

        # get column name that has inf value and drop it
        column_inf = sim_df.columns[np.isinf(sim_df).any()].tolist()
        sim_df.drop(column_inf, axis=1, inplace=True)

        # # normalize dataframe
        # scaled_sim_df = minMaxNormalization(sim_df)
        # # combine normalized dataframe with is_match column
        # scaled_sim_df = pd.concat([scaled_sim_df, res_df['is_match']], axis=1)
        # _column_nan = scaled_sim_df.columns[scaled_sim_df.isnull().any()].to_list()
        # scaled_sim_df.drop(_column_nan, axis=1, inplace=True)

        # test without scaling
        sim_df = pd.concat([sim_df, res_df['is_match']], axis=1)

        # separate is_match from scaled_sim_df to true_df and false_df
        true_df = sim_df[sim_df['is_match'] == True]
        false_df = sim_df[sim_df['is_match'] == False]

        # get length of 1's and 0's
        n_true = len(true_df)
        n_false = len(false_df)
        # drop is_match column and transform to list
        auc_list = [sim_df.drop('is_match', axis=1).columns.to_list()]
        seed_list = []
        for i in tqdm(range(num_sample)):
            # set seed
            if use_seed:
                seed = i * 10
                random.seed(seed)
                seed_list.append(seed)

            # handle imbalance data
            if n_true <= n_false:
                sample_index = random.sample(range(0, n_false), n_true)
                false_sample_df = false_df.iloc[sample_index, :]
                combined_df = pd.concat([true_df, false_sample_df])
            else:
                sample_index = random.sample(range(0, n_true), n_false)
                true_sample_df = true_df.iloc[sample_index, :]
                combined_df = pd.concat([true_sample_df, false_df])

            _auc_list = []
            for column in combined_df.drop('is_match', axis=1).columns:
                # print(combined_df.drop('is_match', axis=1)[column])
                fpr, tpr, _ = roc_curve(combined_df['is_match'].astype(int), combined_df.drop('is_match', axis=1)[column])
                roc_auc = auc(fpr, tpr)
                _auc_list.append(roc_auc)
            
            auc_list.append(_auc_list)
        
        auc_arr = np.array(auc_list)
        auc_df = pd.DataFrame(auc_arr.T, columns=['sim/dis name'] + ['iter %d' % (i+1) for i in range(num_sample)])
        auc_df['mean_auc']  = auc_df.iloc[:, 1:].astype(float).mean(axis=1)
        auc_df = auc_df.sort_values(by='mean_auc', ascending=False, ignore_index=True)

        self.res_arr = res_arr
        self.res_df = res_df
        self.sim_df = sim_df
        # self.scaled_sim_df = scaled_sim_df
        self.auc_arr = auc_arr
        self.auc_df = auc_df
        self.seed_list = seed_list

        # print result if self.show_result is True
        if self.show_result:
            print('\nfinal {} best similarity: '.format(str(self.result_count)))
            print(auc_df[['sim/dis name', 'mean_auc']].head(self.result_count))

    def get_result(self, csv = False):
        """
        Get result of training.

        Parameters
        ----------
        csv : bool, optional
            Set True to get result in csv format. The default is False.
        
        Returns
        -------
        pandas.DataFrame
            dataframe result
        
        Raises
        ------
        Exception
            If method fit() is not called before this function.
        """

        if self.auc_df.empty:
            raise Exception('Fit your data first with \'fit\' method')
        if csv:
            self.auc_df.to_csv('result.csv', index=False)
        
        return self.auc_df

