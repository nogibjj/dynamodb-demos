import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the colors as per user's preference
color_2020_2021 = "blue"
color_2021_2022 = "yellow"

# Define the necessary variables
school_attendance_df = pd.read_csv(
    "https://github.com/nogibjj/Jiechen_Li_Mini_6_External_Database/"
    "raw/main/School_Attendance_by_Student_Group_and_District__2021-2022.csv"
)

all_students_df = school_attendance_df[
    school_attendance_df["Student group"] == "All Students"
]
# Visualization of top 15 districts based on rate difference
subset_df = all_students_df.head(15)

# Set bar width and index for positioning of bars
bar_width = 0.35
index = np.arange(len(subset_df["District name"]))

# Create the bar chart

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting the attendance rates for each district with the specified colors
ax.bar(
    index,
    subset_df["2020-2021 attendance rate"],
    bar_width,
    label="2020-2021",
    alpha=0.8,
    color="blue",
)
ax.bar(
    index + bar_width,
    subset_df["2021-2022 attendance rate - year to date"],
    bar_width,
    label="2021-2022",
    alpha=0.8,
    color="yellow",
)

# Labeling and title
ax.set_xlabel("District Name")
ax.set_ylabel("Attendance Rate")
ax.set_title("Comparison of Attendance Rates for 2020-2021 and 2021-2022")
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(subset_df["District name"], rotation=90)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
