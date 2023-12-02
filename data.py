import requests
# import pdftotext
from PyPDF2 import PdfReader

# book url
# url = "https://apex.oracle.com/pls/apex/lonestar/r/files/static/v13Y/Think-And-Grow-Rich_2011-06.pdf"

# Downloading the pdf from the url
# print('File downloading')
# resp = requests.get(url)
# print('File downloaded')
# with open('book.pdf', 'wb') as f:
#     f.write(resp.content)
    
# Converting the pdf file into text document 'document.txt'
# pdf = pdftotext.PDF(open("book.pdf", "rb")) # extracts text from the pdf pages

# with open("document.txt",'w') as f:
#     for page in pdf:
#         f.writelines(page) # add each page content to the text document

reader = PdfReader("book.pdf")
with open("document.txt",'w', encoding='utf-8') as f:
    for i in range(len(reader.pages)):
        page = reader.pages[i] 
        f.writelines(page.extract_text())