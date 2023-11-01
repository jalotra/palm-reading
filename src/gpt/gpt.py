
import openai 
import os 
import pdf2text
import logging

# logging support
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
chat_completion = openai.ChatCompletion()

def prompt():
    return '''
        You are great at summarization, I have a bunch of text files that I want to find rules for for.
        The text is about indian palmistry, I want you to summarize the text and find rules in the files !
        '''



def pdf_to_text():
    """
    @returns : reads all the pdfs files present in ./pdfs and returns data
    """
    pdfs = []
    for file in os.listdir("./pdfs"):
        if file.endswith(".pdf"):
            pdfs.append({
                "filepath" : os.path.join("./pdfs", file),
                "data" : pdf2text.PDF(open(os.path.join("./pdfs", file), "rb"))
            })
    
    return pdfs


if __name__ == "__main__":
    pdf_to_text_data = pdf_to_text()
    for obj in pdf_to_text_data:
        filepath, data = obj.get("filepath"), obj.get("filepath")
        if len(data) == 0:
            raise AssertionError(f"the pdf present in location : {filepath} is not having any data ? check once !")

        logger.info(f"Total Pages in the file : {filepath} are {len(data)}")
        for idx, page in enumerate(data):
            openai.ChatCompletion()        
