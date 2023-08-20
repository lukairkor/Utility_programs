# -*- coding: utf-8 -*-
"""
-concatenate pdf files
"""
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
# import os.path
import enquiries


# adding pdf to the list
def add_new_pdf():
    pdfs_paths = []
    options = ['Add file: ', 'Finish adding']

    while (True):
        choice = enquiries.choose('Choose one of these options: ', options)
        if choice == options[0]:
            try:
                f_name = input("Input file name(without .pdf extension):\n")
                f_name = str(f_name) + ".pdf"
                open(f_name)
                pdfs_paths.append(f_name)
            except IOError:
                print("Can't find such file!")
            finally:
                continue
        elif choice == options[1]:
            break
    return pdfs_paths


# merging pdfs
def concatenate_file():
    pdfs_paths = add_new_pdf()
    # merge_engin = PdfFileMerger()    
    pdf_writer = PdfFileWriter()
    # pdf_reader = PdfFileReader()

    for path in pdfs_paths:
        pdf = PdfFileReader(path, strict=False)
        # Load PDF into pyPDF          
        for page in range(pdf.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf.getPage(page))

    f_name = ""
    print("Do you want rename file? [default name is merged.pdf]")
    options = ['Yes: ', 'No']
    choice = enquiries.choose('Choose one of these options: ', options)
    if choice == options[0]:
        new_name = input("Input file name(without .pdf extension):\n")
        f_name = new_name + ".pdf"
    if choice == options[1]:
        f_name = "merged.pdf"

    with open(f_name, 'wb') as f:
        pdf_writer.write(f)
        f.closed


# main function
if __name__ == "__main__":
    concatenate_file()
