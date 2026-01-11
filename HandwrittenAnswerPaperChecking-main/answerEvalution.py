# from spellchecker import SpellChecker
# import language_tool_python
# from bert_score import score
#
#
# def evaluate_answer(total_marks, model_answer, student_answer):
#     if isinstance(student_answer, list):  # Ensure student_answer is a string
#         student_answer = " ".join(student_answer)
#
#     spell = SpellChecker()
#
#     # Check for spelling errors
#     spell_errors = spell.unknown(student_answer.split())
#     spell_check_score = len(spell_errors) * 0.05
#
#     # Check for grammar errors
#     tool = language_tool_python.LanguageTool('en-US')
#     matches = tool.check(student_answer)
#     grammar_check_score = len(matches) * 0.05
#
#     # Calculate similarity score using BERT
#     _, _, F1 = score([student_answer], [model_answer], lang="en", model_type="bert-base-uncased")
#     similarity_score = F1.mean().item()
#
#     # Calculate final score
#     if similarity_score == 1:
#         final_score = total_marks
#     elif similarity_score < 0.55:
#         final_score = 0
#     else:
#         context_check_score = (1 - similarity_score) * 0.9
#         total_deductions = spell_check_score + grammar_check_score + context_check_score
#         final_score = total_marks - total_deductions
#
#     # Ensure score is non-negative
#     final_score = max(final_score, 0)
#
#     return final_score, grammar_check_score, spell_check_score


from spellchecker import SpellChecker
import language_tool_python

import google.generativeai as genai
from dotenv import load_dotenv
import os


def evaluate_answer(total_marks, model_answer, student_answer):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    if isinstance(student_answer, list):  # Ensure student_answer is a string
        student_answer = " ".join(student_answer)

    spell = SpellChecker()

    # Check for spelling errors
    spell_errors = spell.unknown(student_answer.split())
    spell_check_score = len(spell_errors) * 0.05

    # Check for grammar errors
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(student_answer)
    grammar_check_score = len(matches) * 0.05

    # Configure Gemini API
    genai.configure(api_key=api_key)  # Replace with your API key
    # Choose a Gemini model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt = """Give the similarity score between the two model answer and student answer. 1 means fully similar and 0 means not similar at all.
                Give the output ONLY AS THE SIMILARITY SCORE AND NOTHING ELSE."""

    response = model.generate_content([prompt, model_answer, student_answer])
    similarity_score = response.text.strip()

    try:
        similarity_score = float(similarity_score)

        # Calculate the final score based on the similarity score
        if similarity_score == 1:
            final_score = total_marks
        elif similarity_score < 0.55:
            final_score = 0
        else:
            context_check_score = (1 - similarity_score) * 0.9
            total_deductions = spell_check_score + grammar_check_score + context_check_score
            final_score = total_marks - total_deductions

        # Ensure the score is non-negative
        final_score = max(final_score, 0)

    except ValueError:
        print("Could not parse the similarity score.")
        final_score = 0  # Default value if there's an error parsing the similarity score
    spell_check_score = spell_check_score/10

    return final_score, grammar_check_score, spell_check_score