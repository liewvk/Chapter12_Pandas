import pandas as pd
import numpy as np
from pathlib import Path


def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    data_file = Path("data") / "students.csv"
    output_file = Path("outputs") / "student_results.csv"

    output_file.parent.mkdir(exist_ok=True)

    df = pd.read_csv(data_file)

    print("Original Student Data")
    print("---------------------")
    print(df)

    df["Result"] = np.where(df["Score"] >= 50, "Pass", "Fail")
    df["Grade"] = df["Score"].apply(get_grade)

    average_score = df["Score"].mean()
    highest_score = df["Score"].max()
    lowest_score = df["Score"].min()

    pass_count = (df["Result"] == "Pass").sum()
    fail_count = (df["Result"] == "Fail").sum()

    strong_students = df[(df["Score"] >= 70) & (df["Attendance"] >= 80)]
    sorted_students = df.sort_values(by="Score", ascending=False)

    print()
    print("Processed Student Data")
    print("----------------------")
    print(df)

    print()
    print("Summary")
    print("-------")
    print(f"Average score: {average_score:.2f}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Students passed: {pass_count}")
    print(f"Students failed: {fail_count}")

    print()
    print("Strong Students")
    print("---------------")
    print(strong_students)

    print()
    print("Students Sorted by Score")
    print("------------------------")
    print(sorted_students)

    df.to_csv(output_file, index=False)

    print()
    print(f"Processed data saved to: {output_file}")


main()
