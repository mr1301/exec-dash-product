# monthly_sales.py

# TODO: import some modules and/or packages here
import csv

# TODO use input to pick different folders maybe?
csv_file_path = ("201710.csv")

sales_data = []
with open(csv_file_path, "r") as csv_file:  # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file)  # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for row in reader:
        #d = dict(row)
        d = {"date": row["date"], "product": row["product"], "unit price": float(row["unit price"]),"units sold": int(row["units sold"]),"sales price": float(row["sales price"])}
        #print(d["product"], d["unit price"])
        sales_data.append(d)

sales_prices = [float(row["sales price"]) for row in sales_data]
total_sales = sum(sales_prices)
print(total_sales)

unique_list = list(set([p["product"] for p in sales_data]))
#print(unique_list)

top_sellers = []
for sales_item in unique_list:
  item_monthly_sales = sum([float(row["sales price"]) for row in sales_data if row["product"] == sales_item])
  d = {"product": sales_item, "monthly_sales":item_monthly_sales}
  top_sellers.append(d)
  print(d["product"], d["monthly_sales"])
