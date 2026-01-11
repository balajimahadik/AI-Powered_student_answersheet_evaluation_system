import google.generativeai as genai
import PIL.Image
import os
import fitz
import re
import markdown2
from PIL import Image
from dotenv import load_dotenv
import os
from DiagramExtraction import extractblkdig
from BlockDiagramEvaluation import blockDigEval
from diagramEval import digEval

load_dotenv()

api_key = os.getenv('API_KEY')

# questionPaperPDF = "QuesPaper.pdf"
# Gemini API
genai.configure(api_key=api_key)

# Modal Answer PDF
# ModalAnswerPdf = "ModalPaper.pdf"

def studentAnswerLoad(QuesArr,BlockArr,DigArr,pdf_path):
    BlockDiagram = {}
    DiagramImage = {}
    DiagramMap = {}
    pdf_document = fitz.open(pdf_path)
    result = []

    print(len(pdf_document))
    for page_num in range(len(pdf_document)):
        # Extract the page
        diagrams = []
        page = pdf_document[page_num]
        # Convert the page to an image
        pix = page.get_pixmap()
        image = PIL.Image.frombytes(
            "RGB", [pix.width, pix.height], pix.samples)

        # Save the image temporarily
        image_path = f"./static/ImageData/Student Answer/Pages/page_{page_num+1}.png"
        image.save(image_path)

        if BlockArr[page_num]==1:
            page = page_num+1
            print("Page Name : ",page)
            # pass image path to diagram extraction and also send question no.
            count,start = extractblkdig(image_path,page_num+1,"Student Answer")
            for i in range(start,start+count):
                cropped_image_path = f"./static/ImageData/Student Answer/cropped_image_{i}.png"
                block_map = blockDigEval(cropped_image_path)
                BlockDiagram.__setitem__(page_num+1,block_map)
        elif DigArr[page_num]== 1:
            count,start = extractblkdig(image_path,page_num,"Student Answer")
            for i in range(start,start+count):
                cropped_image_path = f"./static/ImageData/Student Answer/cropped_image_{i}.png"
                diagrams.append(cropped_image_path)
                digagram_map = digEval(cropped_image_path)
                DiagramMap.__setitem__(page_num + 1, digagram_map)
            DiagramImage.__setitem__(page_num+1,diagrams)

        # Upload the image
        sample_file = genai.upload_file(
            path=image_path, display_name=f"page_{page_num + 1}.png")
        print(
            f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

        # Choose a Gemini API model.
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

        # Prompt the model with text and the previously uploaded image.
        response = model.generate_content(
            [sample_file, "Extract only handwritten text precisely"])
        result.append(response.text)

    for i,ans in enumerate(result):
        print(f"",i," ",ans)
    print("=========================================================================")
    print("Block Diagram : ")
    print(BlockDiagram)
    print("=========================================================================")
    print("Diagram : ")
    print(DiagramImage)
    print("Diagram Labeling : ")
    print(DiagramMap)
    print("=========================================================================")
    return result,BlockDiagram,DiagramImage,DiagramMap





