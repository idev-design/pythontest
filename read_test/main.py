# with open('input_data.txt', 'r') as file:
#     data = file.read()
#     print(data);

# importing required modules
from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('jD3EGHavRG.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
# page = reader.pages[0]

# extracting text from page
# text = page.extract_text()
# print(text)


for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    print(text)
    print("\n   \n")