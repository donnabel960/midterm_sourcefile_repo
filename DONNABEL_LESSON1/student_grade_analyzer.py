scores=[85, 72, 91, 64, 78]

print("Student Score:")
for score in scores:
    print(score)
    print()

    total= sum(scores)
    average= total/len(scores)
    highest= max(scores)
    lowest= min(scores)

    passed=0
    failed=0

    for i, score in enumerate(scores, start=1):
        if score>=90:
            grade="Excellent"
        elif score >= 80:
            grade ="Very Good"
        elif score>= 75:
            grade="Good"
        else:
            grade="Failed"

            if score >=75:
                result="Passed"
                passed+=1
            else:
                result="Failed"
                failed+=1

                print(f"Student{i}:{score}-{grade}-{result}")
                print()

                print(f"Total Score:{total}")
                print(f"Average Score:{average:.0f}")
                print(f"Highest Score:{highest}")
                print(f"Lowest Score:{lowest}")
                print(f"Passed:{passed}")
                print(f"Failed:{failed}")

# Lesson 1 source code