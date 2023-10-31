
import openai 
import os 
import pdf2text


def prompt():
    return '''You are great at summarization, I have a bunch of text files that I want to find rules for for.
    The text is about indian palmistry, I want you to summarize the text and find rules in the files !'''



def pdf2text():
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

