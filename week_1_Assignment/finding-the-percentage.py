"""finding-the-percentage: Calculates and formats the average marks of a student from a given dataset. """

def find_percentage():
    """
    Stores student marks and calculates the average for a given student.
    """  
  # storing name and marks as key value pair
  student_scores = {}

    for _ in range(int(input("Enter number of students: "))):
        data = input("Enter name and scores: ").split()
        name, scores = data[0], list(map(float, data[1:]))
        student_scores[name] = scores

    query_name = input("Enter student name to query: ")
    average_score = sum(student_scores[query_name]) / len(student_scores[query_name])
    print(f"{average_score:.2f}")


find_percentage()
