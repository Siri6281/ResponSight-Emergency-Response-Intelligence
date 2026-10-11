import pandas as pd
from pathlib import Path

# Locate the project folder and load the dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "ambulance_developing_ems.csv"

df = pd.read_csv(DATA_FILE)

print("=" * 50)
print("RESPONSIGHT - EMERGENCY RESPONSE INTELLIGENCE")
print("=" * 50)

# 1. Dataset overview
print("\n1. DATASET OVERVIEW")
print(f"Total records: {len(df)}")
print(f"Total columns: {len(df.columns)}")

# 2. Calls by location
print("\n2. CALLS BY LOCATION")
print(df["location"].value_counts())

# 3. Average recorded response time by location
print("\n3. AVERAGE RECORDED RESPONSE TIME BY LOCATION")
print(df.groupby("location")["response_time_min"].mean().round(2))

# 4. Calls by time of day
print("\n4. CALLS BY TIME OF DAY")
print(df["time_of_day"].value_counts())

# 5. Ambulance availability
print("\n5. AMBULANCE AVAILABILITY")
print(df["ambulance_available"].value_counts(dropna=False))

availability_rate = df["ambulance_available"].mean() * 100
print(f"Recorded availability rate: {availability_rate:.2f}%")

# 6. Target response achievement
print("\n6. TARGET RESPONSE ACHIEVEMENT")
print(df["met_target_response"].value_counts(dropna=False))

target_rate = df["met_target_response"].mean() * 100
print(f"Recorded target achievement rate: {target_rate:.2f}%")

# 7. Missing values in important columns
print("\n7. MISSING VALUES")
columns_to_check = [
    "location",
    "time_of_day",
    "priority",
    "response_time_min",
    "ambulance_available",
    "met_target_response",
]
print(df[columns_to_check].isnull().sum())

# 8. Save a summary report
output_dir = PROJECT_DIR / "python" / "outputs"
output_dir.mkdir(parents=True, exist_ok=True)

summary = df.groupby("location").agg(
    total_calls=("id", "count"),
    avg_response_time_min=("response_time_min", "mean"),
    availability_rate=("ambulance_available", "mean"),
    target_rate=("met_target_response", "mean"),
).round(4)

summary.to_csv(output_dir / "location_analysis.csv")

print("\nLocation analysis saved to:")
print(output_dir / "location_analysis.csv")
print("\nAnalysis completed successfully!")
# 9. Calls and response times by priority
print("\n8. PRIORITY ANALYSIS")

priority_summary = df.groupby("priority").agg(
    total_calls=("id", "count"),
    avg_response_time_min=("response_time_min", "mean"),
    targets_met=("met_target_response", "sum")
).round(2)

print(priority_summary)

priority_summary.to_csv(
    output_dir / "priority_analysis.csv"
)

print("\nPriority analysis saved successfully!")
# 10. Calls and response times by time of day
print("\n9. TIME OF DAY ANALYSIS")

time_summary = df.groupby("time_of_day").agg(
    total_calls=("id", "count"),
    avg_response_time_min=("response_time_min", "mean"),
    targets_met=("met_target_response", "sum")
).round(2)

print(time_summary)

time_summary.to_csv(
    output_dir / "time_of_day_analysis.csv"
)

print("\nTime of day analysis saved successfully!")