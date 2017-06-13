# python

You're going to need Python https://www.python.org/downloads

### For Windows

Add these locations to your PATH environment variable in a command prompt after python installation for the command line to work properly.
```batch
setx /m path "%path%;%localappdata%\Programs\Python\Python36-32\python.exe"
```

Same thing for pip
```batch
setx /m path "%path%;%localappdata%\Programs\Python\Python36-32\Scripts"
```


...and you'll need to install pygame 
```python
pip install pygame
```

