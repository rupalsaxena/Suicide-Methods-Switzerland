
INPATH = "/Users/rupal/Documents/GitHub/Suicide-Methods-Switzerland/dataset/preprocessed.csv"

# exp 1
# OUTPATH = "/Users/rupal/Documents/GitHub/Suicide-Methods-Switzerland/dataset/future_all_ages.csv"
# choose_col = ["year", "gender", "method", "total"]

# exp 2
# OUTPATH = "/Users/rupal/Documents/GitHub/Suicide-Methods-Switzerland/dataset/future_20_29_ages.csv"
# choose_col = ["year", "gender", "method", "20 - 29"]

# exp 3
# OUTPATH = "/Users/rupal/Documents/GitHub/Suicide-Methods-Switzerland/dataset/total_all_ages.csv"
# choose_col = ["year", "gender", "method", "total"]
OUTPATH = "/Users/rupal/Documents/GitHub/Suicide-Methods-Switzerland/dataset/total_20_29_ages.csv"
choose_col = ["year", "gender", "method", "20 - 29"]


# future preds

cols = ["year", "gender", "method"]
data = [
    [2022, "Men", "poisoning"],
    [2022, "Men", "Hang"],
    [2022, "Men", "weapons"],
    [2022, "Men", "Othermethods"],
    [2022, "Men", "Totalsuicides"],
    [2022, "Men", "Allcausesofdeath"],

    [2022, "Women", "poisoning"],
    [2022, "Women", "Hang"],
    [2022, "Women", "weapons"],
    [2022, "Women", "Othermethods"],
    [2022, "Women", "Totalsuicides"],
    [2022, "Women", "Allcausesofdeath"],

    [2022, "both", "poisoning"],
    [2022, "both", "Hang"],
    [2022, "both", "weapons"],
    [2022, "both", "Othermethods"],
    [2022, "both", "Totalsuicides"],
    [2022, "both", "Allcausesofdeath"],

    [2023, "Men", "poisoning"],
    [2023, "Men", "Hang"],
    [2023, "Men", "weapons"],
    [2023, "Men", "Othermethods"],
    [2023, "Men", "Totalsuicides"],
    [2023, "Men", "Allcausesofdeath"],

    [2023, "Women", "poisoning"],
    [2023, "Women", "Hang"],
    [2023, "Women", "weapons"],
    [2023, "Women", "Othermethods"],
    [2023, "Women", "Totalsuicides"],
    [2023, "Women", "Allcausesofdeath"],

    [2023, "both", "poisoning"],
    [2023, "both", "Hang"],
    [2023, "both", "weapons"],
    [2023, "both", "Othermethods"],
    [2023, "both", "Totalsuicides"],
    [2023, "both", "Allcausesofdeath"],

    [2024, "Men", "poisoning"],
    [2024, "Men", "Hang"],
    [2024, "Men", "weapons"],
    [2024, "Men", "Othermethods"],
    [2024, "Men", "Totalsuicides"],
    [2024, "Men", "Allcausesofdeath"],

    [2024, "Women", "poisoning"],
    [2024, "Women", "Hang"],
    [2024, "Women", "weapons"],
    [2024, "Women", "Othermethods"],
    [2024, "Women", "Totalsuicides"],
    [2024, "Women", "Allcausesofdeath"],

    [2024, "both", "poisoning"],
    [2024, "both", "Hang"],
    [2024, "both", "weapons"],
    [2024, "both", "Othermethods"],
    [2024, "both", "Totalsuicides"],
    [2024, "both", "Allcausesofdeath"],

    [2025, "Men", "poisoning"],
    [2025, "Men", "Hang"],
    [2025, "Men", "weapons"],
    [2025, "Men", "Othermethods"],
    [2025, "Men", "Totalsuicides"],
    [2025, "Men", "Allcausesofdeath"],

    [2025, "Women", "poisoning"],
    [2025, "Women", "Hang"],
    [2025, "Women", "weapons"],
    [2025, "Women", "Othermethods"],
    [2025, "Women", "Totalsuicides"],
    [2025, "Women", "Allcausesofdeath"],

    [2025, "both", "poisoning"],
    [2025, "both", "Hang"],
    [2025, "both", "weapons"],
    [2025, "both", "Othermethods"],
    [2025, "both", "Totalsuicides"],
    [2025, "both", "Allcausesofdeath"],
]