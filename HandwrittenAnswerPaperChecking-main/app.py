from flask import Flask, request, jsonify, send_file, render_template
import os
from QuestionLoading import (questionLoading, modalAnswerLoad, studentAnswerLoad,
                             evaluatePaper, plot_student_performance)
import plotly.graph_objects as go
import mysql.connector


app = Flask(__name__)


# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Omkar@2004",  # Replace with your database password
        database="ipcv"
    )


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)




@app.route('/')
def getStarted():
    return render_template('index.html')


@app.route('/steps')
def steps():
    return render_template('steps.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    # Save uploaded files
    model_answer = request.files.get('model_answer')
    student_answer = request.files.get('student_answer')
    question_paper = request.files.get('question_paper')
    question_paper_id = request.form.get('question_paper_id', 'N/A')
    question_pattern = request.form.get('question_pattern', 'N/A')




    if not model_answer or not student_answer:
        return jsonify({"error": "Both files must be provided"}), 400

    model_answer_path = os.path.join(UPLOAD_FOLDER, "ModalAnswer.pdf")
    student_answer_path = os.path.join(UPLOAD_FOLDER, "StudentAnswer.pdf")
    question_paper_path = os.path.join(UPLOAD_FOLDER, "QuesPaper.pdf")

    model_answer.save(model_answer_path)
    student_answer.save(student_answer_path)
    question_paper.save(question_paper_path)

    return render_template('evaluation.html',question_paper_id=question_paper_id,question_pattern=question_pattern)


@app.route('/evaluate', methods=['POST'])
def evaluate():
    model_answer_path = request.json.get('model_answer_path')
    student_answer_path = request.json.get('student_answer_path')
    question_paper_path = request.json.get('question_paper_path')
    total_possible_marks = request.json.get('total_possible_marks', 10)

    if not model_answer_path or not student_answer_path:
        return jsonify({"error": "Paths to both files are required"}), 400

    # Step 1: Load questions
    quesArr, blockArr, digArr = questionLoading(question_paper_path)

    # Step 2: Load model answers
    ModalAnswerArr, modalBlockdiagram, modalDiagramImg, modalDiagramLabel = modalAnswerLoad(
        quesArr, blockArr, digArr, model_answer_path
    )

    # Step 3: Load student answers
    StudentAnswerArr, StudentBlockDiagram, StudentDiagramImg, StudentDiagramLabel = studentAnswerLoad(
        quesArr, blockArr, digArr, student_answer_path
    )

    # Step 4: Evaluate answers
    QuestionWiseMarks, totalObtainedMarks, totalSpellError, totalGrammeticalError, totalLabelingError = evaluatePaper(
        len(quesArr), ModalAnswerArr, StudentAnswerArr, modalBlockdiagram,
        StudentBlockDiagram, modalDiagramImg, StudentDiagramImg, total_possible_marks,1
    )

    # Step 5: Plot performance
    # plot_file = "performance_plot.png"
    # plot_student_performance(
    #     QuestionWiseMarks, totalObtainedMarks, total_possible_marks,
    #     totalSpellError, totalGrammeticalError, totalLabelingError
    # )

    return jsonify({
        "QuestionWiseMarks": QuestionWiseMarks,
        "TotalObtainedMarks": totalObtainedMarks,
        "TotalSpellError": totalSpellError,
        "TotalGrammaticalError": totalGrammeticalError,
        "TotalLabelingError": totalLabelingError
    })


@app.route('/report/<int:student_id>')
def report(student_id):
    print(f"Received student_id: {student_id}")
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch question-wise marks
    cursor.execute("SELECT question_number, marks_scored FROM question_marks WHERE student_id = %s", (student_id,))
    question_marks = cursor.fetchall()  # Make sure to read all rows

    # Fetch total marks and percentage
    cursor.execute(
        "SELECT total_marks_obtained, total_marks_possible, total_percentage FROM evaluation WHERE student_id = %s",
        (student_id,))
    total_marks_data = cursor.fetchone()

    # Consume or clear remaining results
    while cursor.nextset():
        pass  # Move to the next result set

    # Fetch error data
    cursor.execute("SELECT total_errors FROM spelling_errors WHERE student_id = %s", (student_id,))
    spelling_errors_result = cursor.fetchone()
    spelling_errors = spelling_errors_result[0] if spelling_errors_result else 0

    # Consume or clear remaining results
    while cursor.nextset():
        pass  # Move to the next result set

    cursor.execute("SELECT total_errors FROM grammatical_errors WHERE student_id = %s", (student_id,))
    grammatical_errors_result = cursor.fetchone()
    grammatical_errors = grammatical_errors_result[0] if grammatical_errors_result else 0

    # Consume or clear remaining results
    while cursor.nextset():
        pass  # Move to the next result set

    cursor.execute("SELECT total_errors FROM labeling_errors WHERE student_id = %s", (student_id,))
    labeling_errors_result = cursor.fetchone()
    labeling_errors = labeling_errors_result[0] if labeling_errors_result else 0

    if not total_marks_data:
        conn.close()
        return f"No data found for student_id: {student_id}", 404

    total_marks_obtained, total_marks_possible, total_percentage = total_marks_data
    conn.close()

    # Determine the grade
    if 91 <= total_percentage <= 100:
        grade = "A+"
    elif 81 <= total_percentage < 91:
        grade = "A"
    elif 71 <= total_percentage < 81:
        grade = "B+"
    elif 61 <= total_percentage < 71:
        grade = "B"
    elif 51 <= total_percentage < 61:
        grade = "C"
    elif 41 <= total_percentage < 51:
        grade = "D"
    else:
        grade = "F"

    # Prepare data for visualization
    question_numbers = [f"Q{row[0]}" for row in question_marks]
    marks_scored = [row[1] for row in question_marks]

    # Create the interactive bar graph for question-wise marks
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=question_numbers,
        y=marks_scored,
        marker_color='#DAA520',  # Goldenrod color
        name='Marks Scored'
    ))
    fig.update_layout(
        title="Question-wise Marks",
        xaxis_title="Questions",
        yaxis_title="Marks Scored",
        template="plotly_white",
        width=500
    )

    # Create a pie chart for marks scored vs marks lost
    marks_lost = total_marks_possible - total_marks_obtained
    pie_fig = go.Figure(data=[go.Pie(
        labels=["Marks Scored", "Marks Lost"],
        values=[total_marks_obtained, marks_lost],
        marker=dict(colors=['#DAA520', '#FF6347']),  # Goldenrod and Tomato colors
        hole=0.3  # Creates a donut chart
    )])
    pie_fig.update_layout(
        title="Marks Scored vs Marks Lost",
        width=500
    )

    # Create graphs for errors (Spell, Grammar, and Labeling)
    error_fig = go.Figure()
    error_fig.add_trace(go.Bar(
        x=["Spell Errors", "Grammatical Errors", "Labeling Errors"],
        y=[spelling_errors, grammatical_errors, labeling_errors],
        marker_color='#FF6347',  # Tomato color
    ))
    error_fig.update_layout(
        title="Error Breakdown",
        xaxis_title="Error Type",
        yaxis_title="Error Count",
        template="plotly_white",
        width=500
    )

    # Create radar chart for error types
    radar_fig = go.Figure()
    radar_fig.add_trace(go.Scatterpolar(
        r=[spelling_errors, grammatical_errors, labeling_errors],
        theta=["Spelling Errors", "Grammatical Errors", "Labeling Errors"],
        fill='toself',
        name="Error Types",
        marker=dict(color="#FF6347")
    ))
    radar_fig.update_layout(
        title="Error Types Radar Chart",
        polar=dict(
            bgcolor="#333333",  # Dark background for the radar chart
            radialaxis=dict(
                visible=True,
                range=[0, max(spelling_errors, grammatical_errors, labeling_errors) + 1],
                gridcolor="#CCCCCC"
            ),
            angularaxis=dict(
                visible=True,
                gridcolor="#CCCCCC"
            )
        ),
        font=dict(color="white"),
        paper_bgcolor="#1a1a1a",
        template="plotly_dark",
        width=500
    )

    # Convert the graphs to HTML
    graph_html = fig.to_html(full_html=False)
    pie_html = pie_fig.to_html(full_html=False)
    error_html = error_fig.to_html(full_html=False)
    radar_html = radar_fig.to_html(full_html=False)

    # Pass data to the template
    return render_template(
        'report.html',
        graph_html=graph_html,
        pie_html=pie_html,
        error_html=error_html,
        radar_html=radar_html,
        total_marks_obtained=total_marks_obtained,
        total_marks_possible=total_marks_possible,
        total_percentage=total_percentage,
        grade=grade
    )


@app.route('/download-plot', methods=['GET'])
def download_plot():
    plot_file = "performance_plot.png"
    if os.path.exists(plot_file):
        return send_file(plot_file, as_attachment=True)
    return jsonify({"error": "Plot file not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
