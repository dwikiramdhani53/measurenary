Usage
=====

Installation
------------

To use Measurenary, first install it using pip:

.. code-block:: console

   (.venv) $ pip install measurenary

Quickstart
----------

Assume we have a binary pandas ``DataFrame`` with 9 features (A to I) and 1 target column.::
   
   >> import pandas as pd

   >> df = pd.DataFrame(data={
   'A': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
   'B': [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
   'C': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
   'D': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
   'E': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
   'F': [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
   'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   'H': [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
   'I': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   'Target': [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]})

   >> df
      A  B  C  D  E  F  G  H  I  Target
   0  1  0  0  0  0  0  0  0  0     0
   1  1  0  0  0  0  0  0  1  0     0
   2  0  1  0  0  0  0  0  1  0     0
   3  0  1  0  0  0  0  0  1  0     1
   4  0  0  1  0  0  1  0  1  0     1
   5  0  0  1  0  0  1  0  1  0     1
   6  0  0  0  1  0  1  0  0  0     1
   7  0  0  0  1  0  1  0  0  0     1
   8  0  0  0  0  1  1  0  0  0     1
   9  0  0  0  0  1  0  0  0  0     0

The form of data that can be processed by this class is limited only in the form of an example. 
If you have other forms of data, make sure to transform the data so that it has n binary feature columns and 1 target column.

measurenary.AgglomerativeBestSimilarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can use the ``measurenary.AgglomerativeBestMeasure()`` class to fit your data with best similarity/distance equation
based on Agglomerative Clustering. This class also can find best linkage method based on the used similarity/distance.
Make sure your target class are in the last column of your dataframe.

In this case, we already have a binary dataframe with target class in the last and have 2 cluster.
So we can pass it to ``measurenary.AgglomerativeBestMeasure()`` class::
   
   >> from measurenary import AgglomerativeBestMeasure

   >> aggbs = AgglomerativeBestMeasure()

   >> aggbs.fit(df, n_clusters=2)

   100%|████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:03<00:00,  1.06s/it]

To get the result, we can call ``get_result()`` method to our object. It return a pandas ``DataFrame`` with 5 best similarity/distance recommendation::
   
   >> result = aggbs.get_result()

   >> print(result.head())
      linkage           equation  homogeneity  completeness  v_measure   adjusted_rand_index
   0  complete          sim gower     0.628236      0.609987   0.618977             0.013972
   1  complete         sim stiles     0.573438      0.631777   0.601196             0.013972
   2   average         sim peirce     0.432538      0.432538   0.432538             0.010967
   3  complete  sim fager_mcgowan     0.331560      0.445928   0.380332             0.010204
   4   average  sim fager_mcgowan     0.331560      0.445928   0.380332             0.005673

Or, if you want to calculate based on pair of your target, you can use ``measurenary.PairBestMeasure()`` class instead.

measurenary.PairBestMeasure
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This class uses the pair of combinations of each row to determine whether the combination has a large similarity value or not and 
with the appropriate target or not. If the target is the same, then the two lines should have a large similarity value. 
Make sure your target class are in the last column of your dataframe.

In our case, we can just pass our data to the class and use ``fit()`` method to find the recommended equations::

   >> from measurenary import PairBestMeasure

   >> pbs = PairBestMeasure(show_result=True, result_count=5)

   >> bs.fit(df, use_seed=True, num_sample=2)

   1it [00:00, 96.36it/s]
   100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00, 21.34it/s]

to get our result, we can call ``get_result()`` method to our object. It return a pandas ``DataFrame`` with 5 best similarity/distance recommendation::

   >> print(bs.get_result())

   final 5 best similarity:
                  sim/dis name  mean_auc
   0          jaccard similarity       1.0
   1            gower similarity       1.0
   2     hellinger dissimilarity       1.0
   3  pearson_heron_1 similarity       1.0
   4           dice_2 similarity       1.0