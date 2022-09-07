![GitHub](https://img.shields.io/github/license/dwikiramdhani53/measurenary)

# Measurenary

Measurenary is a Python library for computing your suitable similarity matrix from your binary data.

### Installation
To use Measurenary, first install it using pip:
```console
   (.venv) $ pip install measurenary
```
### Get started
To get started, you can import the library and use the `AgglomerativeBestMeasure` or `PairBestMeasure` class:
```python
   import measurenary

   # Instatntiate a Besimlarity object
   aggbs = measurenary.AgglomerativeBestMeasure()
   
   # Call the fit function
   aggbs.fit(X)

   # Print out the result
   print(aggbs.get_result())
```
