import matplotlib.pyplot as plt
import seaborn as sns
from math import pi
import pandas as pd

def plot_student_performance(QuestionWiseMarks, totalObtainedMarks, totalPossibleMarks, totalSpellError, totalGrammaticalError, totalLabelingError):
    # Visualization 1: Bar Chart for Question-wise Marks
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(range(1, len(QuestionWiseMarks) + 1)), y=QuestionWiseMarks, palette="Blues_d")
    plt.xlabel('Question Number')
    plt.ylabel('Marks Obtained')
    plt.title('Question-wise Marks Distribution')
    plt.show()

    # Visualization 2: Pie Chart for Total Marks
    plt.figure(figsize=(8, 8))
    plt.pie([totalObtainedMarks, totalPossibleMarks - totalObtainedMarks], labels=['Marks Obtained', 'Marks Lost'],
            autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'], startangle=140)
    plt.title('Total Marks Distribution')
    plt.show()

    # Visualization 3: Horizontal Bar Chart for Errors
    errors = ['Spelling Errors', 'Grammatical Errors', 'Labeling Errors']
    error_counts = [totalSpellError, totalGrammaticalError, totalLabelingError]

    plt.figure(figsize=(10, 5))
    sns.barplot(x=error_counts, y=errors, palette="Reds_r")
    plt.xlabel('Number of Errors')
    plt.title('Error Types and Counts')
    plt.show()

    # Visualization 4: Radar Chart for Overall Performance
    # Create a DataFrame for the radar chart
    categories = ['Marks', 'Spelling Errors', 'Grammatical Errors', 'Labeling Errors']
    values = [totalObtainedMarks / totalPossibleMarks * 100,
              (1 - totalSpellError / 10) * 100,  # Normalize errors (e.g., out of 10)
              (1 - totalGrammaticalError / 10) * 100,
              (1 - totalLabelingError / 10) * 100]

    df = pd.DataFrame({'Metric': categories, 'Percentage': values})
    N = len(categories)

    # Calculate angle for each category
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]  # Complete the loop

    # Radar chart data prep
    values += values[:1]  # Complete the loop

    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories)

    ax.plot(angles, values)
    ax.fill(angles, values, 'b', alpha=0.1)

    plt.title('Student Performance Overview')
    plt.show()


totalPercentage= 87.57779585570098
QuestionwiseMarks= [9.609540363152822, 9.528483027219771, 8.572109079360962, 9.586508268117905, 9.435220022996267, 9.497292298078538, 6.666666666666666, 7.1664169589678455]
totalObtainedMarks= 70.06223668456079
totalPossibleMarks= 80
totalSpellingErrors= 93.125
totalGrammaticalErrors= 16.875
totalLabelingErrors= 31.666666666666664

# plot_student_performance(QuestionwiseMarks,totalObtainedMarks,totalPossibleMarks,totalSpellingErrors,totalGrammaticalErrors,totalLabelingErrors)



