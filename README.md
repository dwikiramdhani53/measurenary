# Besimilarity

Besimilarity is a Python library for computing your suitable similarity matrix from your binary data.

### Installation
To use Besimilarity, first install it using pip:
```console
   (.venv) $ pip install besimilarity
```
### Get started
To get started, you can import the library and use the `AgglomerativeBestMeasure` or `PairBestMeasure` class:
```python
   import besimilarity

   # Instatntiate a Besimlarity object
   aggbs = besimilarity.AgglomerativeBestMeasure()
   
   # Call the fit function
   aggbs.fit(X)

   # Print out the result
   print(aggbs.get_result())
```
