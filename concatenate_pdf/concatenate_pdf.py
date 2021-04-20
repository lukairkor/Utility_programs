# -*- coding: utf-8 -*-
"""
-concatenate pdf files
"""
from PyPDF2 import PdfFileMerger

my_pdfs = []
amount = input("How many files to concatenate?\n")
for i in range(int(amount)):
    x = input("Input file name(without .pdf extension):\n")
    pdf_file = open(str(x) + ".pdf", "rb")
    my_pdfs.append(pdf_file)

merge_engin = PdfFileMerger()

for pdf in my_pdfs:
    merge_engin.append(pdf)

merge_engin.write("conc_pdf_file.pdf")
merge_engin.close()