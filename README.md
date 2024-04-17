# The Better Resume Extractor using LLMs

## Setup

Run these two commands on the terminal:
```
git clone https://github.com/HemanthVikash/llm-resume-extractor.git
conda env create -f environment.yml
```

The main code for the extractor is present in the ```llm-based-api.ipynb``` file. 

## Extract text from pdf with OCR

**Package used**: PyPDF2 

Use the method ```extract_text_from_pdf``` from the ```ocr_extractor.py``` file to extract any pdf files that are stored in the ```data/``` folder

## Extract vital information using RAG

The need for using LLMs here are 2-fold:

1. **Proper Formatting**: 

    If you have ever used OCR to convert pdf to text, you are sure to run into problems of this kind. 

    For example, when translating
    
    ```
    Built a prediction algorithm to classify hate speech on a few social media platforms using the results from the Twitter web survey that had been conducted.
    ```

    We are sure to get something like this:

    ```
    Built a predicPon algorithm to classify hate speech on a few social media plamorms using the results from the Twiner web survey that had been conducted.
    ```
    
    This is mostly seen in most of the job boards through which candidates apply.

    Using LLMs, we can regenerate the exact same words in the pdf by simply spell-checking the OCR-extracted text.

2. **Structured Extraction**:
    LLMs give us the freedom to extract anything from the text while giving us clues about the context. 
    
    For example, we can get rid of the following errors that commonly occur in resume parsers in job boards: 
    - Confusing the employer with the project name or vice versa
    - Mistakenly adding two jobs in a single job field
    
    We can reduce such mistakes by structuring the output response model and feeding additional context for each field.


3. **Ask for unwritten information**: (Additional Advantage)

    For example, if the resume bullet points are as follows:

    ```
    * Designing and training custom ML/DL algorithms for a climber weight prediction system for a large corporate client. 
    * Trained  an  ML  algorithm  with  97%  test  accuracy  using  Keras  and  Scipy  for  integration  into  an  embedded system, using physics-based feature extraction
    ```

    We can have a response model that would support us getting information like:
    - Summary of the experience
    - Technical Skills used in the experience
    
    These valuable information, while not written by the candidates themselves, can be generated using our LLMs