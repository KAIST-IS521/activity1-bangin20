# Simple CSV Column Printer

---



**<p align ="right"> GSIS 20193313 Changhun Song </p>**

### Development Environment

This program is developed by python 3.7 with anaconda3 in windows 10.

However, It may still works other platforms too without any additional libraries.

It uses two imported modules (csv, sys), but it is native libraries of Python3.7

So you don't need to install additional libraries for this program.

### Description

This is for IS521 *activity1* to train how to use git and github.

This program developed on python 3.7, but it still works in the other python3 versions

- How to Use
  - python3 main.py [CSV_FILE] [COLUMN_NUM]
  - COLUMN_NUM starts from 1, Not 0. (0 Column number will raise an error)
  - Any errors will return exit code 1



### Improvement Discussion

- Inefficiency : This program reads whole csv file twice (validating, column parsing)
  - If we process raw string of file to extract column, this problem can be solved

- Job in Functional way : Making target column by iterating all rows doesn't look like clean code. We can do it more simply and clearly with map function.
- Simple Exception Handling
  - There are lots of exception handling code which decreases readability of codes. We can make it much more contracted way



### Reference

CSV Format [RFC4180](https://tools.ietf.org/html/rfc4180).

Test Data Set - From my Undergraduate Course "Big Data" Assignment Data

Python CSV Module https://docs.python.org/3.7/library/csv.html#csv-contents
