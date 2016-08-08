#!/usr/bin/env python3

# edumunds2csv.py
# -John Taylor
# May-26-2016

# This script takes Edmunds monthly "$199 Lease Deals" and converts it to a CSV file which
# is then suitable to use in a spreasdsheet.
# You will then be able to sort data by different columns.

# Start from: http://www.edmunds.com/car-leasing/monthly-199-lease-deals.html
# Download the PDF that is linked from this page
# Example: http://static.ed.edmunds-media.com/unversioned/img/pdf/lease.deals/199.lease.deals.may.2016.pdf

# PDF to Text
# ------------
# Download: https://pdfbox.apache.org/download.cgi
# java -jar pdfbox-app-2.0.1.jar ExtractText 199.lease.deals.may.2016.pdf 199.txt
#

# Text to CSV
# -----------
# Finally, this script takes the java program's output, 199.txt and subsequently uses it as input (this Python script)
# It will output a csv file
# Example: python edumunds2csv.py > 199.csv

import re, sys

# the filename generated by the pdfbox-app jar program
fname="199.txt"

# set to 1 if the fname file includes a header line (with column fields), otherwise set it to 0
header_line = 1

#############################################################################################################################################################################

#                       make   model,        down             other       months      miles per          lease          total         cost per      each add'l      add'l
#                              price/mon     payment          charges                  months             cost          miles           miles       mile cost       terms
entry_re = re.compile("(.*?) ([0-9].*?\$) .*?([-0-9].*?\$) .*?([#0-9]+) ([0-9][0-9]) ([0-9]{1,4}) .*? ([0-9].*?\$) .*? ([0-9]{5}) .*? (\$[\.0-9]+) ([\.0-9]+\$) .*? (.*)")

#                              model
#                        year  trim     price
model_re = re.compile("(\d{4}) (.*?) ([\.0-9]+\$)")


def process_entry(entry):
	make, year_model_price, initial_payment, other_charges, months, miles_per_month, lease_cost, total_miles, cost_per_mile, each_addl_mile, addl_terms = entry

	match = model_re.findall(year_model_price)
	if not match:
		print(); print("error with:", year_model_price); print(); sys.exit(1)

	year, model, price = match[0]

	price = price.replace("$","").replace(".00","")
	initial_payment = initial_payment.replace("$","").replace(".00","").replace("-", "0")
	lease_cost = lease_cost.replace("$","").replace(".00","")
	cost_per_mile = cost_per_mile.replace("$","")
	each_addl_mile = each_addl_mile.replace("$","")
	addl_terms = addl_terms.strip()
	if not len(addl_terms): addl_terms = "No additional terms"

	#print(make, year, model, price)
	#print(initial_payment, other_charges, months, miles_per_month)
	#print(lease_cost, total_miles, cost_per_mile, each_addl_mile)
	#print(addl_terms)

	return ( make, year, model, price, initial_payment, other_charges, months, miles_per_month, lease_cost, total_miles, cost_per_mile, each_addl_mile, addl_terms )


def make_csv(entry):
	return ",".join(entry)


def main():
	global header_line
	with open(fname) as fp: lines = fp.read().splitlines()
	
	print("make, year, model, price, initial payment, other charges, months, miles per month, lease cost, total miles, cost per mile, each addl mile, addl terms")

	for line in lines:
		# skip the first line as it may be the header
		if header_line:
			header_line = 0
			continue
		if len(line) <= 60: continue
		line = line.replace(",","")

		match = entry_re.findall(line)
		if not match:
			print(); print("error with:\n", line); sys.exit(1)

		current = process_entry(match[0])
		csv = make_csv( current )
		print(csv)

	return 0


if __name__ == '__main__':
	sys.exit( main() )
