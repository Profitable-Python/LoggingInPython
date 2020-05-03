# Logging in Python

## pre-requisite knowledge

- `**kwargs` << `dictionaries` [>>>](./ex_kwargs.py)
- `os.path` << `os` 
  - create cross platform compatible file paths

## good to have but not required knowledge

- windows subsystem for linux (wsl) [>>>](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

## root logger

- defaults log level to warning

## logging to a file

- `filemode='w'` :: rewrites the log every time the script is run
- `filemode='a'` :: default mode is append, log continues to grow with each script

## resources

- [Official Python3 Logger Docs](https://docs.python.org/3/library/logging.html#logging.basicConfig)
  - Data fields that can be added to your logger [>>>](https://docs.python.org/3/library/logging.html#logrecord-attributes)
- [Real Python Blog Article](https://realpython.com/python-logging/)
- How to format datetime strings in python 
  - [strftime.org](https://strftime.org/)
  - [Python3 Official Docs](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)