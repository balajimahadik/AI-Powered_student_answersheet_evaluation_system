from answerEvalution import evaluate_answer
from LabelsEvaluation import evaluate_keys_with_index_match
import mysql.connector

# Example
# Student
# Answer = ['Ans.1\nMachine learning [ML] is a subset of Artificial\nIntelligence (AI) that focuses on developing\nsystems capable of learning from and making\ndecisions based on data without being explicitly\nprogrammed for every task through experience.\nThe concept of ML is built around algorithms that\nprocess data to identify patterns and relationships.\nThese patterns are then used to make predictions\nof decisions. ML is widely used in various fields like\nhealthcare, finance, autonomous vehicles, and NLP.\nCategories of Machine Learning.\n1. Supervised Learning :\n• In supervised learning, the model is trained on a\nlabeled dataset where both input data and corresponding\noutput labels are provided.\n2. Unsupervised Learning :\n• The model learns patterns and structures from\ndata without labeled responses.\n3. Reinforcement Learning :\n• This type involves an agent interacting with the\nenvironment and learning through rewards or\npanalties.', 'Ans 2\nThe TCP/IP model is a conceptual framework that\noutlines the protocols used to facilitate communication\nbetween devices over the internet. It is simplified\nversion of the OSI model, designed to be more practical\nfor real world implementations.\n\nThe model consists of 4 layers:\n• Application Layer : Handels high-level protocol like HTTP,\nFTP.\n• Transport layer : Ensures reliable communication between\ndevices (eg. TCP)\n• Internet Layee : Determines the best path for\ndata (e.g. IP).\n• Network Access Layee : Manages data transfeet between\ndevices on the same network.\n\nApplication\nLayer\n↓\nTransport\nLayer\n↓\nInternet\nLayer\n↓\nNetwork\nAccess\nLayer.', 'Ans 3.\nProcedural programming (PP).\n• follows a step-by-step approach using functions\nor procedures.\n• Focuses on a sequence of actions to be performed.\n• Examples: C, Fortran.\nObject-Oriented Programming (OOP)\n• Organizes code into objects that encapsulates data\nand behaviour.\n• Focuses on modeling real-world entities using classes\nand objects.\n• Examples: Java, Python.\nkey differences include:\n• Modularity: OOP supports modular programming with\nobjects, whereas PP uses functions.\n• Reusability: OOP promotes reusability through inheritance\nand polymorphism.\n• complexity: OOP is more suitable for complex systems,\nwhile PP is simpler for smaller programs.', "Ans4 A Neural Network is a computational model vaguely inspired by the\nhuman brain's structure, though its processing fundamentally differs from\nbiological neurons. It consists of disconnected layers of nodes (neurons) that\nprocess data in isolated batches. Neural networks are often used in tasks\nlike image recognition, language decoding and forecast analytics.\nComponents of a Neural Network:\nInput Layer:\n1. Receives pre-processed data rather than raw inputs.\n2. Each neuron corresponds to a subset of the input features.\nHidden Layers:\n1. Apply weights and biases but no activation functions\n2. Only extract patterns based on the direct weights rather than additional non-\nlinear transformations.\nOutput Layer:\n1. Produces output directly often without any further transformations.\n2. Commonly used for classification tasks only.\nWorking of a Neural Network:\n1. Connections between neurons have a uniform weight, maintaining consistency across\nthe network.\n2. Data moves sequentially through layers, and errors are minimized primarily through\nrandom adjustments rather than a structured algorithm like backpropagation.\nInput Layer\nHidden Layers\nOutput Layer", 'Ans. 5.\nBlockchain is a distributed ledger technology that\nensures data security, transparency, and immutability\nIt stores data in blocks that are cryptographically\nlinked to form a chain, making it resistant to\ntampering.\n\nFeatures ensuring Security in Blockchain:\n1) Decentralization.\n- Data is stored across multiple nodes, eliminating a\nsingle point of failure.\n- Even if one node is compromised, the network remains\nvery secure.\n\n2) Immutability\n- Once data is added to the blockchain, it cannot be\naltered without consensus from the network.\n\n3) Cryptographic Security.\n- Transactions are encrypted using advanced crypto-\ngraphic algorithms.\n\n4) Consensus Mechanisms:\n- Blockchain network use protocols like Proof of Work\n(PoW) or Proof of Stake (PoS) to validate transactions.', 'Ans6 Both compilers and interpreters are used to translate high level programming\nlanguages into machine -readable code but they handle the execution process\nin distinct ways.\nCompiler:\nDefinition: Translates only sections of the source code into machine code while\nrunning the program rather than producing an executable file.\nCharacteristics: Slower execution as some parts are translated during runtime.\nErrors are reported in real-time as the program executes.\nExample: Javascript\nInterpretet:\nDefinition. Reads the entire source code at once and generates an interma\nmachine code file.\nCharacteristics: Faster execution, as the code is pre-processed.\nErrors are stored and reported after the full code execution is complete.\nExample: C interpreter.', 'Ans 7\nOSI Model in Computer Network.\nApplication layer\nPresentation layer\nSoftware layer\nSession layer\nTransport layer\nHeart of OSI\nData link layer\nPhysical layer\nHardware layers\nNetwork layer', 'CPU\nControl Unit\n↓↑\nFanput\nAxithmetic\nand logical Unit\nMemory unit.k\n1 output\nComputer Architecture is the design and organization of a\nfundamental components & how they interacts to\nexecute instructions. It defines the functionality,\norganization, & implementation of computer systems.\nkey components:-\n1) CPU\n2) Memory\n3) Input & Output Devices\n4) Bus System']
# Block Diagram :
# {2: {'Application Layer': 188, 'Transport layer': 395, 'Internet layer': 598, 'Network Access Layer': 829}, 4: {'Input Layer': 205, 'Hidden Layers': 340, 'Output Layer': 488}, 7: {'Application Layer': 164, 'Presentation | lower': 300, 'Presentation': 300, 'Softwave layer.': 309, 'Session Layer': 464, 'lower → Heat of DSL': 631, 'Transport layer': 632, 'Data Link Layer': 788, 'Physical law': 939, 'Clavelwave Layers.': 944, 'Network layer': 1082}}
# =========================================================================
# Diagram :
# {8: ['./static/ImageData/Student Answer/cropped_image_7.png']}
# Diagram Labeling :
# {8: {'CPU': 125.5, 'control Unit': 283.5, 'Input': 403.0, 'AceiHhmelic': 404.0, 'output': 419.5, 'land (ogical Unit': 483.0, 'Merry Unit.': 628.5}}



# Modal = ["Here's a summary of the answer provided in the image:\n\n**Machine Learning (ML)** is a subset of Artificial Intelligence (AI) that focuses on developing systems capable of learning from data and making decisions without explicit programming for each task.  It uses algorithms to identify patterns and relationships in data to make predictions or decisions.  ML is used in various fields, including healthcare, finance, and NLP (Natural Language Processing).\n\n\nThe image then categorizes machine learning into three types:\n\n1. **Supervised Learning:** The model is trained on a labeled dataset where both input data and corresponding output labels are provided.\n\n2. **Unsupervised Learning:** The model learns patterns and structures from data without labeled responses.\n\n3. **Reinforcement Learning:** An agent interacts with the environment and learns through rewards or penalties.\n", "Here's a summary of the TCP/IP model based on the provided image:\n\nThe TCP/IP model is a simplified version of the OSI model, used to facilitate communication between devices over the internet. It consists of four layers:\n\n1.  **Application Layer:** Handles high-level protocols like HTTP and FTP.  This layer is responsible for the applications that users interact with directly.\n\n2.  **Transport Layer:** Ensures reliable communication between devices using protocols such as TCP. This layer manages data segmentation, reassembly, error checking and flow control.\n\n3.  **Internet Layer:** Determines the best path for data using protocols such as IP. This layer handles addressing and routing of data packets across networks.\n\n4.  **Network Access Layer:** Manages data transfer between devices on the same network.  This is the lowest layer and deals with the physical hardware and local network access.\n", "Here's a summary of the key differences between Procedural Programming (PP) and Object-Oriented Programming (OOP) based on the provided text:\n\n**Procedural Programming (PP):**\n\n*   **Approach:** Step-by-step, focusing on a sequence of actions using functions or procedures.\n*   **Examples:** C, Fortran.\n\n**Object-Oriented Programming (OOP):**\n\n*   **Approach:** Organizes code into objects that encapsulate data and behavior, modeling real-world entities using classes and objects.\n*   **Examples:** Java, Python.\n\n**Key Differences:**\n\n*   **Modularity:** OOP promotes modularity through objects; PP uses functions.\n*   **Reusability:** OOP enhances reusability through inheritance and polymorphism.\n*   **Complexity:** OOP is better suited for complex systems, while PP is simpler for smaller programs.", "Here's a summary of the provided text about Neural Networks:\n\n**What is a Neural Network?**\n\nA neural network is a computational model loosely based on the structure of the human brain.  It differs significantly from biological neurons in its processing.  It's composed of interconnected layers of nodes (neurons) that process data in batches.  Common applications include image recognition, language processing, and forecasting.\n\n**Components of a Neural Network:**\n\n* **Input Layer:** Receives pre-processed data; each neuron represents a subset of input features.\n* **Hidden Layers:** Apply weights and biases (but no activation functions); extract patterns based directly on weights, without extra non-linear transformations.\n* **Output Layer:** Produces output directly (often without further transformations); commonly used for classification.\n\n**How a Neural Network Works:**\n\n* **Connections:**  Connections between neurons have uniform weights for consistency.\n* **Data Flow:** Data moves sequentially through the layers. Error minimization happens primarily through random adjustments, not through structured algorithms like backpropagation.", "Here's a summary of the features that ensure security in a blockchain, based on the provided text:\n\n1. **Decentralization:** Data is spread across many nodes, preventing a single point of failure.  If one node is compromised, the network remains secure.\n\n2. **Immutability:** Once data is added, it cannot be changed without a consensus from the network.\n\n3. **Cryptographic Security:**  Transactions are encrypted using advanced algorithms.\n\n4. **Consensus Mechanisms:**  Protocols like Proof of Work (PoW) or Proof of Stake (PoS) verify transactions.\n", "Here's a summary of the provided text comparing compilers and interpreters:\n\n**Compilers:**\n\n* **Definition:** Translate portions of source code to machine code during program runtime, without creating a separate executable file.\n* **Characteristics:** Slower execution due to on-the-fly translation; errors reported in real-time.\n* **Example:** JavaScript\n\n**Interpreters:**\n\n* **Definition:** Read the entire source code at once, generating an intermediate machine code file.\n* **Characteristics:** Faster execution because of pre-processing; errors stored and reported after the full code runs.\n* **Example:** C interpreter\n\n\nBoth achieve the goal of converting high-level code into machine-readable instructions but differ significantly in their approach to code translation and error handling.\n", 'Here\'s a summary of the provided image describing the OSI model in a computer network:\n\nThe image depicts the seven layers of the OSI (Open Systems Interconnection) model, categorized into software and hardware layers.  The transport layer is highlighted as the "Heart of OSI".\n\n* **Software Layers:** These are the top four layers: Application, Presentation, Session, and Transport.\n\n* **Hardware Layers:** These are the bottom three layers: Network, Data Link, and Physical.\n\nThe image clearly shows the hierarchical structure of the OSI model.\n', "Here's a summary based on the provided image:\n\nThe image shows a block diagram of a computer, illustrating the key components and their interactions.  The diagram highlights the CPU (Central Processing Unit), which includes the Control Unit and the Arithmetic & Logical Unit.  It also shows the Memory Unit, Input, and Output.\n\nThe accompanying text defines computer architecture as the design and organization of these fundamental components, explaining how they work together to execute instructions.  It also lists the key components: CPU, Memory, Input/Output devices, and Bus Systems.\n"]
# =========================================================================
# Block Diagram :
# {2: {'Application Layer': 50, 'Transport Layer': 118, 'Internet Layer': 186, 'Network Layer': 254}, 4: {'Input Layer': 38, 'Hidden Layers': 98, 'Output Layer': 158}, 7: {'Application Layer': 62, 'Software Layers': 99, 'Presentation Layer': 102, 'Session layer': 142, 'Heart of OSI': 180, 'Transport Layer': 183, 'Network Layer': 220, 'Data Link Layer': 258, 'Hardware Layers': 259, 'Physical Layer': 300}}
# =========================================================================
# Diagram :
# {8: ['./static/ImageData/Modal Answer/cropped_image_7.png']}
# Diagram Labeling :
# {8: {'CPU': 37.5, 'Control Unit': 73.5, 'Arithmetic &': 127.0, 'Input': 142.0, 'Output': 142.0, 'Logical Unit': 154.5, 'Memory Unit': 209.5}}
# =========================================================================


#


# def evaluatePaper(questionsNumber,modalAnswers,studentAnswers,modelBlockDigMap,studentBlockDigMap,modelDigMap,studentDigMap,marksPerQues):
#     TextualAnwerMarks = 0
#     BlockDiagramMarks = 0
#     DiagramLabellingMarks = 0
#     # DiagramMarks = 100
#
#     totalMarks = 0
#     totalObtainedMarks = 0
#     totalSpellError = 0
#     totalGrammeticalError = 0
#     totalLabelingError = 0
#     QuestionWiseMarks = []
#     labelCounter = 0
#
#     for i in range(len(studentAnswers)):
#         # Evaluate marks for textual answer, grammar, and spellcheck
#         obtmarks, grammarCheck, spellCheck = evaluate_answer(10, modalAnswers[i], studentAnswers[i])
#
#         # Store the marks out of 100 for each section
#         TextualAnwerMarks = obtmarks * 10  # Convert to out of 100
#         GrammerMarks = grammarCheck * 10  # Convert to out of 100
#         SpellCheckMarks = spellCheck * 10  # Convert to out of 100
#
#         print(f"Obtained Marks: {TextualAnwerMarks}")
#         print(f"Grammar Marks: {GrammerMarks}")
#         print(f"SpellCheck Marks: {SpellCheckMarks}")
#
#         # Track grammatical and spelling errors
#         totalSpellError += SpellCheckMarks
#         totalGrammeticalError += GrammerMarks
#
#         # Initialize BlockDiagramMarks and DiagramLabellingMarks to 100
#         BlockDiagramMarks = 100
#         DiagramLabellingMarks = 100
#
#         # Block diagram evaluation
#         if i in modelBlockDigMap:
#             if modelBlockDigMap[i] is not None:
#                 marks_obtained, total_possible_marks = evaluate_keys_with_index_match(studentBlockDigMap[i],
#                                                                                       modelBlockDigMap[i])
#                 BlockDiagramMarks = (marks_obtained / total_possible_marks) * 100
#                 totalLabelingError += 100 - BlockDiagramMarks
#                 labelCounter = labelCounter + 1
#         else:
#             BlockDiagramMarks = 100
#
#         # Diagram labeling evaluation
#         if i in modelDigMap:
#             if modelDigMap[i] is not None:
#                 marks_obtained, total_possible_marks = evaluate_keys_with_index_match(studentDigMap[i], modelDigMap[i])
#                 DiagramLabellingMarks = (marks_obtained / total_possible_marks) * 100
#                 totalLabelingError += 100 - DiagramLabellingMarks
#                 labelCounter = labelCounter + 1
#         else:
#             DiagramLabellingMarks = 100
#
#         # Total marks out of 100 for this question
#         totalMarks = TextualAnwerMarks + BlockDiagramMarks + DiagramLabellingMarks
#
#         # Convert total marks to out of 10 and store in QuestionWiseMarks
#         obtainedMarks = (totalMarks / 300) * 10
#         QuestionWiseMarks.append(obtainedMarks)
#
#         # Update total obtained marks
#         totalObtainedMarks += obtainedMarks
#
#     # Calculate and return the percentage based on total obtained marks and total possible marks
#     totalPossibleMarks = questionsNumber * 10  # Assuming each question is worth 10 points
#     percentage = (totalObtainedMarks / totalPossibleMarks) * 100
#
#     totalLabelingError = (totalLabelingError/(100*labelCounter))*100
#     totalSpellError = (totalSpellError/(10*questionsNumber))*100
#     totalGrammeticalError = (totalGrammeticalError/(10*questionsNumber))*100
#
#     # Return or print the errors and percentage
#     print(f"Grammatical Errors: {totalGrammeticalError}")
#     print(f"Spelling Errors: {totalSpellError}")
#     print(f"Labeling Errors: {totalLabelingError}")
#     print(f"Total Percentage: {percentage}%")
#
#     return QuestionWiseMarks,totalObtainedMarks,totalSpellError,totalGrammeticalError,totalLabelingError







# ,ModalBlockDiagramMap,ModalDiagramMap,ModalDiagram,StudentAnswers,StudentBlockDiagramMap,StudentDiagramMap,StudentDiagram

# modalAnswers = ["Answer 1","Answer 2","Answer 3","Answer 4"]
# evaluatePaper(modalAnswers)


# Example data for the function call:

# modalAnswers = [
#     'Ans.1\nMachine learning [ML] is a subset of Artificial\nIntelligence (AI) that focuses on developing\nsystems capable of learning from and making\ndecisions based on data without being explicitly\nprogrammed for every task through experience.\nThe concept of ML is built around algorithms that\nprocess data to identify patterns and relationships.\nThese patterns are then used to make predictions\nof decisions. ML is widely used in various fields like\nhealthcare, finance, autonomous vehicles, and NLP.\nCategories of Machine Learning.\n1. Supervised Learning :\n• In supervised learning, the model is trained on a\nlabeled dataset where both input data and corresponding\noutput labels are provided.\n2. Unsupervised Learning :\n• The model learns patterns and structures from\ndata without labeled responses.\n3. Reinforcement Learning :\n• This type involves an agent interacting with the\nenvironment and learning through rewards or\npanalties.',
#     'Ans 2\nThe TCP/IP model is a conceptual framework that\noutlines the protocols used to facilitate communication\nbetween devices over the internet. It is simplified\nversion of the OSI model, designed to be more practical\nfor real world implementations.\n\nThe model consists of 4 layers:\n• Application Layer : Handels high-level protocol like HTTP,\nFTP.\n• Transport layer : Ensures reliable communication between\ndevices (eg. TCP)\n• Internet Layee : Determines the best path for\ndata (e.g. IP).\n• Network Access Layee : Manages data transfeet between\ndevices on the same network.\n\nApplication\nLayer\n↓\nTransport\nLayer\n↓\nInternet\nLayer\n↓\nNetwork\nAccess\nLayer.',
#     'Ans 3.\nProcedural programming (PP).\n• follows a step-by-step approach using functions\nor procedures.\n• Focuses on a sequence of actions to be performed.\n• Examples: C, Fortran.\nObject-Oriented Programming (OOP)\n• Organizes code into objects that encapsulates data\nand behaviour.\n• Focuses on modeling real-world entities using classes\nand objects.\n• Examples: Java, Python.\nkey differences include:\n• Modularity: OOP supports modular programming with\nobjects, whereas PP uses functions.\n• Reusability: OOP promotes reusability through inheritance\nand polymorphism.\n• complexity: OOP is more suitable for complex systems,\nwhile PP is simpler for smaller programs.',
#     'Ans4 A Neural Network is a computational model vaguely inspired by the\nhuman brain\'s structure, though its processing fundamentally differs from\nbiological neurons. It consists of disconnected layers of nodes (neurons) that\nprocess data in isolated batches. Neural networks are often used in tasks\nlike image recognition, language decoding and forecast analytics.\nComponents of a Neural Network:\nInput Layer:\n1. Receives pre-processed data rather than raw inputs.\n2. Each neuron corresponds to a subset of the input features.\nHidden Layers:\n1. Apply weights and biases but no activation functions\n2. Only extract patterns based on the direct weights rather than additional non-\nlinear transformations.\nOutput Layer:\n1. Produces output directly often without any further transformations.\n2. Commonly used for classification tasks only.\nWorking of a Neural Network:\n1. Connections between neurons have a uniform weight, maintaining consistency across\nthe network.\n2. Data moves sequentially through layers, and errors are minimized primarily through\nrandom adjustments rather than a structured algorithm like backpropagation.\nInput Layer\nHidden Layers\nOutput Layer',
#     'Ans. 5.\nBlockchain is a distributed ledger technology that\nensures data security, transparency, and immutability\nIt stores data in blocks that are cryptographically\nlinked to form a chain, making it resistant to\ntampering.\n\nFeatures ensuring Security in Blockchain:\n1) Decentralization.\n- Data is stored across multiple nodes, eliminating a\nsingle point of failure.\n- Even if one node is compromised, the network remains\nvery secure.\n\n2) Immutability\n- Once data is added to the blockchain, it cannot be\naltered without consensus from the network.\n\n3) Cryptographic Security.\n- Transactions are encrypted using advanced crypto-\ngraphic algorithms.\n\n4) Consensus Mechanisms:\n- Blockchain network use protocols like Proof of Work\n(PoW) or Proof of Stake (PoS) to validate transactions.',
#     'Ans6 Both compilers and interpreters are used to translate high level programming\nlanguages into machine -readable code but they handle the execution process\nin distinct ways.\nCompiler:\nDefinition: Translates only sections of the source code into machine code while\nrunning the program rather than producing an executable file.\nCharacteristics: Slower execution as some parts are translated during runtime.\nErrors are reported in real-time as the program executes.\nExample: Javascript\nInterpretet:\nDefinition. Reads the entire source code at once and generates an interma\nmachine code file.\nCharacteristics: Faster execution, as the code is pre-processed.\nErrors are stored and reported after the full code execution is complete.\nExample: C interpreter.',
#     'Ans 7\nOSI Model in Computer Network.\nApplication layer\nPresentation layer\nSoftware layer\nSession layer\nTransport layer\nHeart of OSI\nData link layer\nPhysical layer\nHardware layers\nNetwork layer',
#     'CPU\nControl Unit\n↓↑\nFanput\nAxithmetic\nand logical Unit\nMemory unit.k\n1 output\nComputer Architecture is the design and organization of a\nfundamental components & how they interacts to\nexecute instructions. It defines the functionality,\norganization, & implementation of computer systems.\nkey components:-\n1) CPU\n2) Memory\n3) Input & Output Devices\n4) Bus System'
# ]
#
# studentAnswers = [
#     "Student answer 1",
#     "Student answer 2",
#     "Student answer 3",
#     "Student answer 4",
#     "Student answer 5",
#     "Student answer 6",
#     "Student answer 7",
#     "Student answer 8"
# ]
#
# # Example maps for model and student answers:
# modelBlockDigMap = {
#     2: {'Application Layer': 188, 'Transport layer': 395, 'Internet layer': 598, 'Network Access Layer': 829},
#     4: {'Input Layer': 205, 'Hidden Layers': 340, 'Output Layer': 488},
#     7: {'Application Layer': 164, 'Presentation | lower': 300, 'Presentation': 300, 'Softwave layer.': 309, 'Session Layer': 464, 'lower → Heat of DSL': 631, 'Transport layer': 632, 'Data Link Layer': 788, 'Physical law': 939, 'Clavelwave Layers.': 944, 'Network layer': 1082}
# }
#
# studentBlockDigMap = {
#     2: {'Application Layer': 50, 'Transport Layer': 118, 'Internet Layer': 186, 'Network Layer': 254},
#     4: {'Input Layer': 38, 'Hidden Layers': 98, 'Output Layer': 158},
#     7: {'Application Layer': 62, 'Software Layers': 99, 'Presentation Layer': 102, 'Session layer': 142, 'Heart of OSI': 180, 'Transport Layer': 183, 'Network Layer': 220, 'Data Link Layer': 258, 'Hardware Layers': 259, 'Physical Layer': 300}
# }
#
# modelDigMap = {
#     8: {'CPU': 37.5, 'Control Unit': 73.5, 'Arithmetic &': 127.0, 'Input': 142.0, 'Output': 142.0, 'Logical Unit': 154.5, 'Memory Unit': 209.5}
# }
#
# studentDigMap = {
#     8: {'CPU': 125.5, 'control Unit': 283.5, 'Input': 403.0, 'AceiHhmelic': 404.0, 'output': 419.5, 'land (ogical Unit': 483.0, 'Merry Unit.': 628.5}
# }
#
# marksPerQues = 10  # Marks per question
#
# # Call the evaluatePaper function
# QuestionWiseMarks, totalObtainedMarks, totalSpellError, totalGrammeticalError, totalLabelingError = evaluatePaper(
#     questionsNumber=8,
#     modalAnswers=modalAnswers,
#     studentAnswers=studentAnswers,
#     modelBlockDigMap=modelBlockDigMap,
#     studentBlockDigMap=studentBlockDigMap,
#     modelDigMap=modelDigMap,
#     studentDigMap=studentDigMap,
#     marksPerQues=marksPerQues
# )
#
# # Print the results
# print(f"Question Wise Marks: {QuestionWiseMarks}")
# print(f"Total Obtained Marks: {totalObtainedMarks}")
# print(f"Total Spell Errors: {totalSpellError}")
# print(f"Total Grammatical Errors: {totalGrammeticalError}")
# print(f"Total Labeling Errors: {totalLabelingError}")


def evaluatePaper(questionsNumber, modalAnswers, studentAnswers, modelBlockDigMap, studentBlockDigMap, modelDigMap, studentDigMap, marksPerQues, student_id):
    # Initialize variables
    TextualAnwerMarks = 0
    BlockDiagramMarks = 0
    DiagramLabellingMarks = 0

    totalMarks = 0
    totalObtainedMarks = 0
    totalSpellError = 0
    totalGrammeticalError = 0
    totalLabelingError = 0
    QuestionWiseMarks = []
    labelCounter = 0

    # Establish MySQL connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Omkar@2004",  # Replace with your database password
        database="ipcv"
    )
    cursor = conn.cursor()

    for i in range(len(studentAnswers)):
        # Evaluate marks for textual answer, grammar, and spellcheck
        obtmarks, grammarCheck, spellCheck = evaluate_answer(10, modalAnswers[i], studentAnswers[i])

        # Store the marks out of 100 for each section
        TextualAnwerMarks = obtmarks * 10  # Convert to out of 100
        GrammerMarks = grammarCheck * 10  # Convert to out of 100
        SpellCheckMarks = spellCheck * 10  # Convert to out of 100

        # Track grammatical and spelling errors
        totalSpellError += SpellCheckMarks
        totalGrammeticalError += GrammerMarks

        # Initialize BlockDiagramMarks and DiagramLabellingMarks to 100
        BlockDiagramMarks = 100
        DiagramLabellingMarks = 100

        # Block diagram evaluation
        if i in modelBlockDigMap:
            if modelBlockDigMap[i] is not None:
                marks_obtained, total_possible_marks = evaluate_keys_with_index_match(studentBlockDigMap[i], modelBlockDigMap[i])
                BlockDiagramMarks = (marks_obtained / total_possible_marks) * 100
                totalLabelingError += 100 - BlockDiagramMarks
                labelCounter = labelCounter + 1
        else:
            BlockDiagramMarks = 100

        # Diagram labeling evaluation
        if i in modelDigMap:
            if modelDigMap[i] is not None:
                marks_obtained, total_possible_marks = evaluate_keys_with_index_match(studentDigMap[i], modelDigMap[i])
                DiagramLabellingMarks = (marks_obtained / total_possible_marks) * 100
                totalLabelingError += 100 - DiagramLabellingMarks
                labelCounter = labelCounter + 1
        else:
            DiagramLabellingMarks = 100

        # Total marks out of 100 for this question
        totalMarks = TextualAnwerMarks + BlockDiagramMarks + DiagramLabellingMarks

        # Convert total marks to out of 10 and store in QuestionWiseMarks
        obtainedMarks = (totalMarks / 300) * 10
        QuestionWiseMarks.append(round(obtainedMarks, 0))  # Round to 0 decimal places

        # Update total obtained marks
        totalObtainedMarks += obtainedMarks

        # Insert question-wise marks into the database (example for one question)
        query = f"""
        INSERT INTO question_marks (student_id, question_number, marks_scored)
        VALUES (1, {i+1}, {round(obtainedMarks, 0)});
        """
        cursor.execute(query)

    # Calculate and return the percentage based on total obtained marks and total possible marks
    totalPossibleMarks = questionsNumber * 10  # Assuming each question is worth 10 points
    percentage = round((totalObtainedMarks / totalPossibleMarks) * 100, 0)  # Round to 0 decimal places

    # Calculate errors
    totalLabelingError = round((totalLabelingError / (100 * labelCounter)) * 100, 0)
    totalSpellError = round((totalSpellError / (10 * questionsNumber)) * 100, 0)
    totalGrammeticalError = round((totalGrammeticalError / (10 * questionsNumber)) * 100, 0)

    # Insert the overall evaluation into the database
    query_eval = f"""
    INSERT INTO evaluation (student_id, total_marks_obtained, total_marks_possible, total_percentage)
    VALUES (1, {round(totalObtainedMarks, 0)}, {totalPossibleMarks}, {percentage});
    """
    cursor.execute(query_eval)

    # Insert spelling errors into the database
    query_spell = f"""
    INSERT INTO spelling_errors (student_id, total_errors)
    VALUES (1, {totalSpellError});
    """
    cursor.execute(query_spell)

    # Insert grammatical errors into the database
    query_gram = f"""
    INSERT INTO grammatical_errors (student_id, total_errors)
    VALUES (1, {totalGrammeticalError});
    """
    cursor.execute(query_gram)

    # Insert labeling errors into the database
    query_label = f"""
    INSERT INTO labeling_errors (student_id, total_errors)
    VALUES (1, {totalLabelingError});
    """
    cursor.execute(query_label)

    # Commit all queries to the database
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Return or print the errors and percentage
    print(f"Grammatical Errors: {totalGrammeticalError}")
    print(f"Spelling Errors: {totalSpellError}")
    print(f"Labeling Errors: {totalLabelingError}")
    print(f"Total Percentage: {percentage}%")

    return QuestionWiseMarks, round(totalObtainedMarks, 0), totalSpellError, totalGrammeticalError, totalLabelingError