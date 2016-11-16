# Bogo1
A one line implementation of bogosort in python.

**How to use:**
* import bogo1 (until I make this a real package with setup.py it must be in the same directory as whatever module imports it)
* bogo1.sort(list)

**Known issuses:**
* It will throw an exception if it doesn't sort the list before it shuffles sys.maxsize times
If you have a working fix for this issue please make a pull request
