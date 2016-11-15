# Bogo One
A one line implementation of bogosort in python.

**How to use:**
* import bogo1 (until I make this a real package with setup.py it must be in the same directory as whatever module imports it)
* bogo1.sort(list)
* *optionally* bogo1.sort(list,sys.maxsize)
* Default patience value is 1000, which works for smaller lists most of the time.

**Known issuses:**
* It will return None if it fails to sort the data quick enough
* It will continue sorting the data if it has already successfully sorted the data
If you have a working fix for either of theses issues please make a pull request.
