# # def evaluate_answers(student_answer, model_answer, tolerance):
# #     """
# #     Evaluate the student's answers against the model answers and return the total marks obtained.
# #
# #     Parameters:
# #     - student_answer (dict): A dictionary containing the student's answers.
# #     - model_answer (dict): A dictionary containing the model answers.
# #     - tolerance (int): The acceptable margin for numerical value comparison (default: 0 for exact match).
# #
# #     Returns:
# #     - total_marks (int): The total marks obtained by the student.
# #     """
# #     total_marks = 0
# #
# #     # for question_number, student_values in student_answer.items():
# #     #     if question_number in model_answer:
# #     #         model_values = model_answer[question_number]
# #     #
# #     #         for key, student_value in student_values.items():
# #     #             if key in model_values:
# #     #                 model_value = model_values[key]
# #     #                 print(student_value)
# #     #                 print(model_value)
# #     #                 # Check if the values are within the tolerance range
# #     #                 if abs(student_value - model_value) <= tolerance:
# #     #                     total_marks += 1
# #     for i,answer in enumerate(model_answer.items()):
# #         studentAns = student_answer.items()
# #
# #         print(studentAns)
# #         print(answer)
#
#
# def evaluate_answers(student_answers, model_answers):
#     total_marks = 0
#     max_marks = 0
#
#     for question_number, model_layers in model_answers.items():
#         # Check if the question exists in the student's answers
#         if question_number in student_answers:
#             student_layers = student_answers[question_number]
#
#             # Calculate the maximum marks for this question
#             max_marks += sum(model_layers.values())
#
#             # Calculate the obtained marks by matching student's answer with the model answer
#             for layer, mark in student_layers.items():
#                 if layer in model_layers and student_layers[layer] == model_layers[layer]:
#                     total_marks += model_layers[layer]
#
#     return total_marks, max_marks
#
#
#
#
#
#
# # Example usage
# student_answer = {
#     2: {'Application Layer': 188, 'Transport layer': 395, 'Internet layer': 598, 'Network Access Layer': 829},
#     4: {'Input Layer': 205, 'Hidden Layers': 340, 'Output Layer': 488},
#     7: {'Application Layer': 164, 'Presentation | lower': 300, 'Softwave layer.': 309,
#         'Session Layer': 464, 'lower → Heat of DSL': 631, 'Transport layer': 632,
#         'Data Link Layer': 788, 'Physical law': 939, 'Clavelwave Layers.': 944, 'Network layer': 1082}
# }
#
# model_answer = {
#     2: {'Application Layer': 188, 'Transport layer': 395, 'Internet layer': 598, 'Network Access Layer': 829},
#     4: {'Input Layer': 205, 'Hidden Layers': 340, 'Output Layer': 488},
#     7: {'Application Layer': 62, 'Software Layers': 99, 'Presentation Layer': 102, 'Session layer': 142, 'Heart of OSI': 180, 'Transport Layer': 183, 'Network Layer': 220, 'Data Link Layer': 258, 'Hardware Layers': 259, 'Physical Layer': 300}
# }
# #
# # # Tolerance set to 0 for exact match
# # marks = evaluate_answers(student_answer.get(2), model_answer.get(2), 10)
# # print(f"Total Marks Obtained: {marks}")
#
#
# # Evaluate and print the results
# marks_obtained, total_possible_marks = evaluate_answers(student_answer, model_answer)
# print(f"Marks Obtained: {marks_obtained}")
# print(f"Total Possible Marks: {total_possible_marks}")
# print(f"Percentage: {(marks_obtained / total_possible_marks) * 100:.2f}%")
from difflib import SequenceMatcher

def evaluate_keys_with_index_match(student_Answer, model_Answer):
    student_keys = list(student_Answer.keys())
    model_keys = list(model_Answer.keys())


    total_matches = 0
    max_matches = min(len(student_keys), len(model_keys))  # Compare up to the shortest list length

    # Iterate over the keys by index
    for i in range(max_matches):
        student_key = student_keys[i]
        model_key = model_keys[i]

        # Use SequenceMatcher to find similarity between strings at the same index
        similarity = SequenceMatcher(None, student_key, model_key).ratio()
        if similarity >= 0.8:  # Threshold for considering it a match
            print(f"Matched at index {i}: {student_key} (student) with {model_key} (model)")
            total_matches += 1
        else:
            print(f"No match at index {i}: {student_key} (student) vs {model_key} (model)")

    return total_matches, max_matches

# student_Answer = {'Application Layer': 164, 'Presentation | lower': 300, 'Softwave layer.': 309,
#         'Session Layer': 464, 'lower → Heat of DSL': 631, 'Transport layer': 632,
#         'Data Link Layer': 788, 'Physical law': 939, 'Clavelwave Layers.': 944, 'Network layer': 1082}
# model_Answer = {'Application Layer': 62, 'Software Layers': 99, 'Presentation Layer': 102, 'Session layer': 142, 'Heart of OSI': 180, 'Transport Layer': 183, 'Network Layer': 220, 'Data Link Layer': 258, 'Hardware Layers': 259, 'Physical Layer': 300}
#
# # Example student and model keys
#
#
# # Evaluate and print the results
# marks_obtained, total_possible_marks = evaluate_keys_with_index_match(student_Answer, model_Answer)
# print(f"Matches Found: {marks_obtained}")
# print(f"Total Possible Matches: {total_possible_marks}")
# print(f"Percentage: {(marks_obtained / total_possible_marks) * 100:.2f}%")

