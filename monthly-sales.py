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

#************************** Above Import Data Using CSV***********************************
sales_prices = [float(row["sales price"]) for row in sales_data]
total_sales = sum(sales_prices)
#print(total_sales)

print("-----------------------")
print("MONTH: March 2018")
print("-----------------------")
print("CRUNCHING THE DATA...")
print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

#*****************************Above Calc & Print Total Price********************************
print("-----------------------")
print("TOP SELLING PRODUCTS:")

unique_list = list(set([p["product"] for p in sales_data]))
#print(unique_list)

top_sellers = []
for sales_item in unique_list:
  item_monthly_sales = sum([float(row["sales price"]) for row in sales_data if row["product"] == sales_item])
  d = {"product": sales_item, "monthly_sales":item_monthly_sales}
  top_sellers.append(d)
  print(d["product"], d["monthly_sales"])

#*******************************Above List of Products & Sales***********************************

print("-----------------------")
print("VISUALIZING THE DATA...")
genres = []
viewer = []

for p in bar_data:
    genres.append(p["genre"])
    viewer.append(p["viewers"])


plt.bar(genres, viewer)
plt.ylabel("People Per Genre")
plt.xlabel("Movie Genres")
plt.xticks(rotation=90)
plt.title("Movie Genres & Viewers")
#plt.show()
