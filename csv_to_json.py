import pandas as pd
import json

data = pd.read_csv(
    "https://github.com/nogibjj/Jiechen_Li_Mini_6_External_Database/raw/main/School_Attendance_by_Student_Group_and_District__2021-2022.csv"
)

# Convert DataFrame to list of dictionaries
data_dict = data.to_dict("records")

# Convert to DynamoDB's expected JSON format
items = []
for item in data_dict:
    dynamodb_item = {}
    for key, value in item.items():
        dynamodb_item[key] = {"S": str(value)}
    items.append(dynamodb_item)

# Save to a JSON file
with open("output.json", "w") as f:
    json.dump(items, f)
