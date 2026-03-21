import json
import pandas as pd

INPUT_FILE = "data/yelp_academic_dataset_business.json"
OUTPUT_FILE = "output/yelp_business_flat.csv"

# create an empty python list

# each business record in the json file will be turned into one flat dictionary

# then we will store each of those dictionaries in the rows list

# this way each json object becomes one python dictionary

# all dictionaries go into "rows"

# then pandas library will be used to turn these rows into a dataframe0

rows = []

# 'with' opens the file, as long as the code runs, and then closes it 

with open(INPUT_FILE, "r", encoding= "utf-8") as f:     # opens the json file, in read mode, encoding to ensure that it reads the text correctly, f= abbrev

    for line in f:
        item = json.loads(line)

        attributes = item.get("attributes", {}) or {}       # this command tries to get the attributes. if the attribute is None, replace it with {}

        hours = item.get("hours", {}) or {}

        row = {
            "business_id": item.get("business_id"),
            "name": item.get("name"),
            "city": item.get("city"),
            "state": item.get("state"),
            "postal_code": item.get("postal_code"),
            "latitude": item.get("latitude"),
            "longitude": item.get("longitude"),
            "stars": item.get("stars"),
            "review_count": item.get("review_count"),
            "is_open": item.get("is_open"),
            "categories": item.get("categories"),
            "restaurant_price_range": attributes.get("RestaurantsPriceRange2"),
            "bike_parking": attributes.get("bike_parking"),
            "business_accepts_credit_cards": attributes.get("BusinessAcceptsCreditCards"),
            "good_for_kids": attributes.get("GoodForKids"),
            "restaurants_take_out": attributes.get("RestaurantsTakeOut"),
            "restaurants_delivery": attributes.get("RestaurantsDelivery"),
            "wheelchair_access": attributes.get("WheelchairAccessible"),
            "outdoor_seating": attributes.get("OutdoorSeating"),
            "monday_hours": hours.get("Monday"),
            "tuesday_hours": hours.get("Tuesday"),
            "wednesday_hours": hours.get("Wednesday"),
            "thursday_hours": hours.get("Thursday"),
            "friday_hours": hours.get("Friday"),
            "saturday_hours": hours.get("Saturday"),
            "sunday_hours": hours.get("Sunday"),
            "": hours.get(""),
            "": hours.get(""),
        }
        rows.append(row)


df = pd.DataFrame(rows)     # use pandas function to convert the dictionary into a Data Frame


print(df.head())

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")