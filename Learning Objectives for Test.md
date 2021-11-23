# BIOS0030 Learning Objectives for Test

Please read through – if you are unsure of what an objective covers please email me at philip.lewis@ucl.ac.uk for further details or an code example. 

As the test is open book it is a good idea to make a notebook (or set of notebooks) that collect examples of the skills below as a reference.

---

## GENERAL

 - print information to the screen

 - know how Python uses indentation to indicate code blocks

 - know the key data types used in Python and how to define them (int float bool str list dict tuple)

 - know which data types are mutable and which are immutable

---

## FUNCTIONS

 - how to write a Python function
     - how to define a function
     - setting and using input arguments
     - how to return output
 - how to use a function
 - understand that variables created inside a function have local scope only
 - how to create a global variable within a function

---

## MATHS

 - understand the difference between int and float data types
 - calculate a sequence given a formula
 - using Python to perform calculations
 - importing and using common functions (sqrt, sin, cos, log) from Python's math module
 - rounding numbers
 - formatting numbers for display using f-strings
 - using scientific notation

---

## CONDITIONS

 - using the if command
 - if conditions that test a string
 - if conditions that test numbers
 - working with boolean values (True and False)
 - test if greater/less/equal to etc.
 - combining test conditions using and, or, not etc.
 - combining a series of tests in an "if elif else"

---

## LOOPS

 - set up a for loop
 - set up a while loop
 - be able to loop over items in a list
 - be able to loop a set number of times
 - set up a nested loop

---

## STRINGS

 - how to create strings
 - how to add newline / tab characters in a string
 - allowed string operations:
    - joining strings,
    - accessing characters using an index
    - finding length
    - slicing
 - convert variables (e.g. numbers) into strings and vice versa
 - insert Python variables or information data into strings using f-strings
 - know how to specify formats when using f-strings

---

## LISTS

creating a list
finding the length of a list
changing the contents of a list
appending to a list
removing items from a list
ways to address elements using indices
ways to slice a list
working with nested lists (i.e. a list within a list)
looping over elements in the list

---

## DICTIONARIES

creating a Python dictionary, (with initial data)
adding to/updating information in a Python dictionary
accessing data in a dictionary
looping over elements in a dictionary

---

## TUPLES

creating a tuple
accessing data in a tuple
understand difference between tuples and lists
looping over elements in the tuple

---

## FILE ACCESS

how to open a file in Python for reading
get next line of text from a file
loop over each lines of text in a file
read all text from a file
write text to a file

---

## CLASSES 

defining an object class (and its __init__ function) based on specified attributes
adding class method functions
adding a __str__ method that displays the stored object's information
adding an  __eq__  class method to compare objects
creating and importing a class using a .py code file
save and load class objects using the pickle module

---

## WORKING WITH NUMPY

- store data into a numpy array (e.g. convert a list to a 1D numpy array, or create a 2D numpy array from a list of lists)
- create a 1D or 2D array filled with an initial value

- find the dimensions of a numpy array
- find the data type associated with a numpy array

- use indexes to select a value from a numpy array
- understand how negative indexes can be used
- use the slice operator : to make a selection from a numpy array (row, column, subset of rows/columns)
- select a set of certain rows/columns based on indexes provided

- use numpy arrays in calculations that are applied across each element

- understand the key differences between numpy arrays and Python lists

---


## WORKING WITH MATPLOTLIB

- know how to use the inline and notebook modes for matplotlib in Jupyter notebooks

- understand how to create figures and axes (either a single axis or set of axes for a figure with multiple subplots)
- be able to control figure size
- know how to save a figure to disk as an image

- understand how to plot a dataset given x and y coordinates, as a line or scatter plot
- be able to plot a function (given a formula) by defining a set of x-values and calculating the y-values
- know how to plot multiple dataseries to a plot and add a legend
- know how to plot a histogram given a dataset, with specified bin intervals

- be able to set a plot title
- know how to control the colour and style of lines and markers
- know how to set axes ranges and axes labels
- be able to add a text label to a plot

---

## WORKING WITH PANDAS

- load in a csv file into a dataframe
- create a dataframe using a list of lists, containing data row by row
- create a dataframe using a dictionary where each entry stores a column in the dataframe
- save a dataframe as a csv file

- relabel the columns
- specify labels for rows

- find key info about a dataframe (number of rows / columns, column types)
- display a dataframe (either in full, or first few rows)

- Use a dataframe to calculate statistics (mean, max, min, standard deviation) based on a column or selection from a column

- select a row from the table by label or index
- select a column from the table by label or index
- select a value from the table
- select a subset of data from the table based by specifying row and column indexes/labels ranges

- select a subset of the data using a condition

- apply a simple transformation to generate a new column (change units, take log)
- use a formula to generate new columns based on existing columns e.g. `bmi = (height**2)/mass`
- sort a dataframe either using labels or by column values

- make a scatter plot with x and y values based on columns from the data frame
- make a histogram of a column, specifying the bin intervals



