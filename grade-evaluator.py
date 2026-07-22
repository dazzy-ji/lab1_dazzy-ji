import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # TODO: a) Check if all scores are percentage based (0-100)
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    # TODO: c) Calculate the Final Grade and GPA
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
    if not data:
        print("Error: The CSV file contains no data to process.")
        sys.exit(1)

    for record in data:
        if record['score'] < 0 or record['score'] > 100:
            print(f"Error: Score for assignment '{record['assignment']}' is out of range (0-100).")
            sys.exit(1)

    total_weight = 0.0
    formative_weight = 0.0
    summative_weight = 0.0

    for record in data:
        total_weight += record['weight']
        if record['group'].lower() == 'formative':
            formative_weight += record['weight']
        elif record['group'].lower() == 'summative':
            summative_weight += record['weight']
        else:
            print(f"Error: Unknown group '{record['group']}' for assignment '{record['assignment']}'.")
            sys.exit(1)

    if abs(total_weight - 100.0) > 0.01:
        print(f"Error: Total weight is {total_weight}, but it should be 100.")
        sys.exit(1)
    if abs(formative_weight - 60.0) > 0.01:
        print(f"Error: Total formative weight is {formative_weight}, but it should be 60.")
        sys.exit(1)
    if abs(summative_weight - 40.0) > 0.01:
        print(f"Error: Total summative weight is {summative_weight}, but it should be 40.")
        sys.exit(1)

    formative_score = 0.0
    summative_score = 0.0   

    for record in data:
        points_earned = record['score'] * (record['weight'] / 100.0)
        if record['group'].lower() == 'formative':
            formative_score += points_earned
        else:
            summative_score += points_earned

    total_score = formative_score + summative_score
    gpa = (total_score / 100.0) * 5.0

    formative_percentage = (formative_score/60) * 100
    summative_percentage = (summative_score/40) * 100

    course_passed = formative_percentage >= 50 and summative_percentage >= 50

    failed_formative_assignments = []
    for record in data:
        if record['group'].lower() == 'formative' and record['score'] < 50:
            failed_formative_assignments.append(record)

    resubmission_options = []
    if failed_formative_assignments:
        max_weight = max(record['weight'] for record in failed_formative_assignments)
        resubmission_options = [record for record in failed_formative_assignments if record['weight'] == max_weight]

    print(f"Formative Score: {formative_score:.0f}/60 ({formative_percentage:.0f}%)")
    print(f"Summative Score: {summative_score:.0f}/40 ({summative_percentage:.0f}%)")
    print(f"Total Score: {total_score:.0f}/100")
    print(f"GPA: {gpa:.2f}")
    print(f"Course Status: {'PASSED' if course_passed else 'FAILED'}")

    if resubmission_options:
        print("Resubmission Options:")
        for record in resubmission_options:
            print(f" - {record['assignment']} "
                  f"(score:{record['score']:.0f}, weight:{record['weight']:.0f}%)")
    else:
        print("No resubmission options available.")


if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)