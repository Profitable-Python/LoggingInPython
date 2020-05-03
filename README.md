# Logging in Python

## Here is the live stream [replay](https://youtu.be/R8YH8O6tu1k) of me going through the [Real Python](https://realpython.com/python-logging/) article by [Abhinav Ajitsaria](https://realpython.com/team/aajitsaria/)

## pre-requisite knowledge

- `**kwargs` << `dictionaries` [>>>](./ex_kwargs.py)
- `os.path` << `os` 
  - create cross platform compatible file paths
- basic python oop ( object oriented programming )

## good to have but not required knowledge

- windows subsystem for linux (wsl) [>>>](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

## root logger

- defaults log level to warning

## logging to a file

- `filemode='w'` :: rewrites the log every time the script is run
- `filemode='a'` :: default mode is append, log continues to grow with each script
- best practice for logging stack trace so it can be easily parsed with analytics like pandas?
  - format the result with the log level at the beginning so conditional logic can applied (if log level == ERROR then while loop )

## resources

- [Official Python3 Logger Docs](https://docs.python.org/3/library/logging.html#logging.basicConfig)
  - Data fields that can be added to your logger [>>>](https://docs.python.org/3/library/logging.html#logrecord-attributes)
- [Real Python Blog Article](https://realpython.com/python-logging/)
- How to format datetime strings in python 
  - [strftime.org](https://strftime.org/)
  - [Python3 Official Docs](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

