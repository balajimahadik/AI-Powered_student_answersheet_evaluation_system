import google.generativeai as genai
import PIL.Image
import os
import fitz
import re
import markdown2
from PIL import Image
from dotenv import load_dotenv
import os
from ModalAnswerLoading import modalAnswerLoad
from StudentAnswerLoading import studentAnswerLoad
from Evaluation import evaluatePaper
from PlottingResult import plot_student_performance

load_dotenv()
api_key = os.getenv('API_KEY')

questionPaperPDF = "O:\\IPCV\\CP\\FinalCP\\QuesPaper.pdf"
# Gemini API
genai.configure(api_key=api_key)

# Extract Questions
def extract_questions_from_pdf(pdf_path):
    # Convert PDF pages to images
    pdf_document = fitz.open(pdf_path)

    for page_num in range(len(pdf_document)):
        # Extract the page
        page = pdf_document[page_num]
        # Convert the page to an image
        pix = page.get_pixmap()
        image = PIL.Image.frombytes(
            "RGB", [pix.width, pix.height], pix.samples)

        # Save the image temporarily
        image_path = f"./static/ImageData/Questions/page_{page_num + 1}.png"
        image.save(image_path)

        # Upload the image
        sample_file = genai.upload_file(
            path=image_path, display_name=f"page_{page_num + 1}.png")
        print(
            f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

        # Choose a Gemini API model.
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

        # Prompt the model with text and the previously uploaded image.
        response = model.generate_content(
            [sample_file, "Extract all questions in given image"])
        return response.text


def extract_questions(text):
    # Assuming each question starts with a number followed by a period
    # E.g., "1. What is Python?"
    import re
    pattern = r'(?:\d+\.\s*)(.*?)(?=\d+\.|$)'  # Regex to capture questions
    questions = re.findall(pattern, text, re.DOTALL)

    return [q.strip() for q in questions]


def questionLoading(questionPaperPDF):
    questions = extract_questions_from_pdf(questionPaperPDF)
    QuesArr = extract_questions(questions)

    # List of questions

    # Updated keywords for classification
    block_keywords = ["block diagram", "blockdiagram", "system architecture", "system block", "schematic block",
                      "functional block", "flowchart"]
    diagram_keywords = ["draw", "diagram", "illustrate", "sketch", "show", "circuit", "graph", "plot", "layout",
                        "chart", "representation", "schematic"]

    # Initialize arrays
    blockArr = [0] * len(QuesArr)
    diagramArr = [0] * len(QuesArr)

    # Classify questions
    for i, question in enumerate(QuesArr):
        if any(keyword in question.lower() for keyword in block_keywords):
            blockArr[i] = 1
        elif any(keyword in question.lower() for keyword in diagram_keywords):
            diagramArr[i] = 1

    print("Questions are as Follows : ")

    for i,val in enumerate(QuesArr):
        print(f"Question {i + 1}: {val}")

    print("Block Diagram Array (1 = requires block diagram, 0 = does not):")
    for i, val in enumerate(blockArr):
        print(f"Question {i + 1}: {val}")
    print("\nDiagram Array (1 = requires diagram, 0 = does not):")
    for i, val in enumerate(diagramArr):
        print(f"Question {i + 1}: {val}")
    return QuesArr,blockArr,diagramArr

#
# quesArr,blockArr,digArr = questionLoading()
#
# ModalAnswerArr,modalBlockdiagram,modalDiagramImg,modalDiagramLabel = modalAnswerLoad(quesArr,blockArr,digArr,"ModelAnswer.pdf[3].pdf")
#
# StudentAnswerArr,StudentBlockDiagram,StudentDiagramImg,StudentDiagramLabel = studentAnswerLoad(quesArr,blockArr,digArr,"StudentAnswer.pdf")
#
# print(StudentAnswerArr)
# print(ModalAnswerArr)
#
# QuestionWiseMarks,totalObtainedMarks,totalSpellError,totalGrammeticalError,totalLabelingError = evaluatePaper(8,ModalAnswerArr,StudentAnswerArr,modalBlockdiagram,StudentBlockDiagram,modalDiagramImg,StudentDiagramImg,10)
#
# totalPossibleMarks = 80
#
# # Print all values for inspection
# print("Question-wise Marks:", QuestionWiseMarks)
# print("Total Obtained Marks:", totalObtainedMarks)
# print("Total Possible Marks:", totalPossibleMarks)
# print("Total Spelling Errors:", totalSpellError)
# print("Total Grammatical Errors:", totalGrammeticalError)
# print("Total Labeling Errors:", totalLabelingError)
# #
# # # Print the calculated performance overview
# print("\nPerformance Overview:")
# print(f"Percentage of Marks Obtained: {(totalObtainedMarks / totalPossibleMarks) * 100:.2f}%")
# print(f"Spelling Errors: {totalSpellError}")
# print(f"Grammatical Errors: {totalGrammeticalError}")
# print(f"Labeling Errors: {totalLabelingError}")
#
# plot_student_performance(QuestionWiseMarks,totalObtainedMarks,totalPossibleMarks,totalSpellError,totalGrammeticalError,totalLabelingError)

