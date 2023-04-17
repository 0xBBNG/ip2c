# ip2c
Python Program to Extract Country from IP Addresses in a CSV file.

This Python program reads a CSV file containing IP addresses and extracts the country of each IP address using GeoIP2 database. The output is then saved to a new CSV file with the country information.

## Requirements
This program requires Python 3.x and the following libraries:

* pandas
* geoip2

You can install these libraries using pip:

```
pip install pandas geoip2
```
## How to Use
Prepare a CSV file with a column named 'ip_address' that contains the IP addresses you want to extract country information from.

1. Download or clone this repository.

1. Navigate to the directory where you downloaded or cloned the repository.

1. Modify the 'input.csv' file.

1. Run the program by executing the following command in your terminal or command prompt:

```
python ip2c.py input.csv
```
The program will extract the country information from each IP address in the input file and save it to the output file.
##  How it Works
This program uses the geoip2 library to extract the country information from each IP address in the input file. The pandas library is used to read and write the CSV files.

The program reads the input CSV file using the pandas library and extracts the IP addresses into a list. It then loops through the list, uses the geoip2 library to extract the country information from each IP address, and adds the country information to a new column in the original pandas DataFrame.

Finally, the program uses pandas to save the DataFrame to a new CSV file with the country information included.
