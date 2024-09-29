def add_grades():
    grades = []
    
    while True:
        grade_input = input("Enter a grade (or type 'done' to finish): ")
        
        if grade_input.lower() == 'done':
            break
        
        try:
            grade = float(grade_input)
            grades.append(grade)
        except ValueError:
            print("Invalid input! Please enter a number or 'done' to finish.")
    
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    grades = add_grades()
    average = calculate_average(grades)
    print(f"Overall average grade: {average:.2f}")

if __name__ == "_main_":
    main()