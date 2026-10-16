# Week 5 Hands-On Exercise
# Student Grade Analyzer Version 3
# Python Programming

# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    # Guardian-condition test records
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,"
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A: Parse and organize the records.
for record in raw_records:
    # Split the comma-separated record into fields.
    fields = record.split(",")

    # A valid record must contain exactly four fields.
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    # Store the student's name.
    name = fields[0]

    # Convert the score fields to numbers safely.
    try:
        # List slicing gets all score fields after the name.
        score_fields = fields[1:]
        scores = [int(score) for score in score_fields]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    # Store the name and scores in the dictionary.
    student_scores[name] = scores


# PART B: Display records alphabetically.
print("ORGANIZED STUDENT RECORDS")

for name in sorted(student_scores):
    scores = student_scores[name]
    print(f"{name}: {scores}")


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate the student results.
for name, scores in student_scores.items():
    # Guard against an empty score list.
    if not scores:
        continue

    # Calculate total, average, highest, and lowest.
    total = sum(scores)
    number_of_scores = len(scores)
    average = total / number_of_scores
    highest_score = max(scores)
    lowest_score = min(scores)

    # Determine the student's remark.
    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    # Add the average to the class total.
    sum_of_averages += average

    # Append the result tuple to ranking.
    ranking.append(
        (average, name, highest_score, lowest_score, remark)
    )


# PART D: Sort and display the ranking.
# Sort by average from highest to lowest.
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

# Use enumerate() and tuple unpacking to display the ranking.
for rank, record in enumerate(ranking, start=1):
    average, name, highest_score, lowest_score, remark = record
    print(
        f"{rank:<5} {name:<10} {average:>7.2f}  "
        f"{highest_score:>7}  {lowest_score:>6}  {remark}"
    )


# PART E: Display the class summary.
# Calculate the class average safely.
if ranking:
    class_average = sum_of_averages / len(ranking)
else:
    class_average = 0

print("\nCLASS SUMMARY")
print(f"Number of Students: {len(ranking)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")

# Use ranking[0] and ranking[-1] safely.
if ranking:
    highest_ranked = ranking[0]
    lowest_ranked = ranking[-1]

    print(f"Highest: {highest_ranked[1]} - {highest_ranked[0]:.2f}")
    print(f"Lowest: {lowest_ranked[1]} - {lowest_ranked[0]:.2f}")
else:
    print("Highest: None")
    print("Lowest: None")
