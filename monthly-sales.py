import matplotlib.pyplot as plt
from operator import itemgetter

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


def to_usd(my_price):
  return "${0:,.2f}".format(my_price)

#************************** Above Import Data Using CSV***********************************
month = "OCTOBER"  # TODO: get from file name or date values
year = 2017


sales_prices = [float(row["sales price"]) for row in sales_data]
total_sales = sum(sales_prices)
#print(total_sales)

print("-------------------------------")
print("MONTH: {month} {year}")
print("-------------------------------")
print("CRUNCHING THE DATA...")
print("-------------------------------")
print("TOTAL MONTHLY SALES:" + to_usd(total_sales))

#*****************************Above Calc & Print Total Price********************************
print("-------------------------------")
print("TOP SELLING PRODUCTS:")

unique_list = list(set([p["product"] for p in sales_data]))
#print(unique_list)


product_sales = []
for sales_item in unique_list:
  item_monthly_sales = sum([float(row["sales price"]) for row in sales_data if row["product"] == sales_item])
  d = {"product": sales_item, "monthly_sales":to_usd(item_monthly_sales)}
  product_sales.append(d)
  #print("+ " + d["product"] + " " + d["monthly_sales"])

sorted_product_sales = sorted(product_sales, key=itemgetter("monthly_sales"), reverse=True)
top_sellers = sorted_product_sales[0:3]
#print(type(top_sellers))



#*******************************Above List of Products & Sales***********************************

breakpoint()

print("-------------------------------")
print("VISUALIZING THE DATA...")
item = []
sales = []

for p in product_sales:
    item.append(p["product"])
    sales.append(p["monthly_sales"])

plt.bar(item,sales)
plt.ylabel("sales")
plt.xlabel("item")
#plt.show()
