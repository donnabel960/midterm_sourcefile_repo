def classify_grade(grade):

    if grade >= 90:
        return "Excellent", "Passed"
    elif grade >= 85:
        return "Very Good", "Passed"
    elif grade >= 80:
        return "Good", "Passed"
    elif grade >= 75:
        return "Satisfactory", "Passed"
    else:
        return "Needs Improvement", "Failed"


def load_students(filename):

    students = []

    try:
        with open(filename, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                fields = line.split(",")

                if len(fields) != 3:
                    continue

                student_id = fields[0].strip()
                name = fields[1].strip()

                try:
                    grade = float(fields[2].strip())
                except ValueError:
                    continue

                if grade < 0 or grade > 100:
                    continue

                students.append({
                    "student_id": student_id,
                    "name": name,
                    "grade": grade
                })

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return students


def calculate_statistics(students):

    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0

    highest_student = students[0]
    lowest_student = students[0]

    for student in students:

        grade = student["grade"]

        total_grade += grade

        classification, status = classify_grade(grade)

        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if grade > highest_student["grade"]:
            highest_student = student

        if grade < lowest_student["grade"]:
            lowest_student = student

    number_of_students = len(students)

    average = total_grade / number_of_students

    return {
        "number_of_students": number_of_students,
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest_student": highest_student,
        "lowest_student": lowest_student
    }


def display_students(students):

    print("\nALL STUDENTS")
    print("-" * 80)

    print(
        f"{'Student No.':<14}"
        f"{'Name':<20}"
        f"{'Grade':<10}"
        f"{'Classification':<20}"
        f"{'Status':<10}"
    )

    print("-" * 80)

    for student in students:

        classification, status = classify_grade(
            student["grade"]
        )

        name = student["name"]

        if len(name) > 18:
            name = name[:18]

        print(
            f"{student['student_id']:<14}"
            f"{name:<20}"
            f"{student['grade']:<10.2f}"
            f"{classification:<20}"
            f"{status:<10}"
        )

    print("-" * 80)


def display_statistics(statistics):

    print("\nCLASS STATISTICS")

    print(
        f"Number of students: "
        f"{statistics['number_of_students']}"
    )

    print(
        f"Class average: "
        f"{statistics['average']:.2f}"
    )

    print(
        f"Passed: "
        f"{statistics['passed']}"
    )

    print(
        f"Failed: "
        f"{statistics['failed']}"
    )

    print(
        f"Highest: "
        f"{statistics['highest_student']['name']} - "
        f"{statistics['highest_student']['grade']:.2f}"
    )

    print(
        f"Lowest: "
        f"{statistics['lowest_student']['name']} - "
        f"{statistics['lowest_student']['grade']:.2f}"
    )


def search_student(students, keyword):

    matches = []

    keyword = keyword.strip().lower()

    for student in students:

        if (
            keyword in student["student_id"].lower()
            or keyword in student["name"].lower()
        ):
            matches.append(student)

    return matches


def save_report(students, statistics, filename):

    try:

        with open(filename, "w") as file:

            file.write("STUDENT GRADE ANALYZER REPORT\n")
            file.write("=" * 80 + "\n\n")

            for student in students:

                classification, status = classify_grade(
                    student["grade"]
                )

                file.write(
                    f"{student['student_id']} | "
                    f"{student['name']} | "
                    f"{student['grade']:.2f} | "
                    f"{classification} | "
                    f"{status}\n"
                )

            file.write("\nCLASS STATISTICS\n")
            file.write("-" * 40 + "\n")

            file.write(
                f"Number of students: "
                f"{statistics['number_of_students']}\n"
            )

            file.write(
                f"Class average: "
                f"{statistics['average']:.2f}\n"
            )

            file.write(
                f"Passed: "
                f"{statistics['passed']}\n"
            )

            file.write(
                f"Failed: "
                f"{statistics['failed']}\n"
            )

            file.write(
                f"Highest-performing student: "
                f"{statistics['highest_student']['name']} - "
                f"{statistics['highest_student']['grade']:.2f}\n"
            )

            file.write(
                f"Lowest-performing student: "
                f"{statistics['lowest_student']['name']} - "
                f"{statistics['lowest_student']['grade']:.2f}\n"
            )

        print(
            f"Report successfully saved to '{filename}'."
        )

    except OSError as error:

        print(f"Error saving report: {error}")


def main():

    students = load_students("grades.txt")

    if not students:

        print("No valid student records were loaded.")

        return

    statistics = calculate_statistics(students)

    while True:

        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            display_students(students)

        elif choice == "2":

            display_statistics(statistics)

        elif choice == "3":

            keyword = input(
                "Enter student number or name: "
            )

            matches = search_student(
                students,
                keyword
            )

            if matches:

                print("\nSEARCH RESULTS")

                for student in matches:

                    classification, status = classify_grade(
                        student["grade"]
                    )

                    print(
                        f"{student['student_id']} - "
                        f"{student['name']} - "
                        f"{student['grade']:.2f} - "
                        f"{classification} - "
                        f"{status}"
                    )

            else:

                print("No matching student found.")

        elif choice == "4":

            save_report(
                students,
                statistics,
                "grade_report.txt"
            )

        elif choice == "5":

            print(
                "Thank you for using "
                "Student Grade Analyzer."
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1 to 5."
            )

            continue


if __name__ == "__main__":
    main()