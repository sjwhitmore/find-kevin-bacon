# Six Degrees of Kevin Bacon

To run:

1. Unzip the films.tar.gz file into a folder.  Change the path variable in the main() function in the script (line 76) to match the path to the unzipped films folder.  You will also need to change the path variable on line 23.

2. You can now use the script on the command line like so:
```python
> python find_kevin.py "Demi Moore"
The tool will take multiple arguments as well if you want to search a few at once.
i.e.
```python
> python find_kevin.py "Demi Moore" "Ashton Kutcher" "Brad Pitt"