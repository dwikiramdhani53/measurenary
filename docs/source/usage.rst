Usage
=====

Installation
------------

To use Measurenary, first install it using pip:

.. code-block:: console

   (.venv) $ pip install measurenary

Quickstart
----------

- measurenary.AgglomerativeBestSimilarity
   You can use the ``measurenary.AgglomerativeBestMeasure()`` class to fit your data with best similarity/distance equation
   based on Agglomerative Clustering. This class also can find best linkage method based on the used similarity/distance.

   Make sure your target column is in the last column.::
      
      >> from measurenary import AgglomerativeBestMeasure

      >> aggbs = AgglomerativeBestMeasure()

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
      'Target': [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]})``

      >> aggbs.fit(df, n_clusters=2)

      df shape:  (10, 10)
      n_clusters:  2
      affinity:  all
      linkage:  all

      100%|████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:03<00:00,  1.06s/it]

      >> result = aggbs.get_result()

      >> print(result.head())
         linkage           equation  homogeneity  completeness  v_measure   adjusted_rand_index
      0  complete          sim gower     0.628236      0.609987   0.618977             0.013972
      1  complete         sim stiles     0.573438      0.631777   0.601196             0.013972
      2   average         sim peirce     0.432538      0.432538   0.432538             0.010967
      3  complete  sim fager_mcgowan     0.331560      0.445928   0.380332             0.010204
      4   average  sim fager_mcgowan     0.331560      0.445928   0.380332             0.005673
   
   Or, if you want to calculate based on pair of your target, you can use ``measurenary.PairBestMeasure()`` class instead.

- measurenary.PairBestMeasure
   This class uses the pair of combinations of each row to determine whether the combination has a large similarity value or not and 
   with the appropriate target or not. If the target is the same, then the two lines should have a large similarity value::

      >> from measurenary import PairBestMeasure

      >> pbs = PairBestMeasure(show_result=True, result_count=5)

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
      'Target': [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]})``

      >> bs.fit(df, use_seed=True, num_sample=2)
      use_seed:  True
      num_sample:  2

      1it [00:00, 96.36it/s]
      100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00, 21.34it/s]

      final 5 best similarity:
                     sim/dis name  mean_auc
      0          jaccard similarity       1.0
      1            gower similarity       1.0
      2     hellinger dissimilarity       1.0
      3  pearson_heron_1 similarity       1.0
      4           dice_2 similarity       1.0