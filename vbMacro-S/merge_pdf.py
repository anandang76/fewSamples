import os
import sys
from PyPDF2 import PdfMerger

# Check for parameter
if len(sys.argv) < 2:
    print("Usage: python merge_pdf.py outputfilename.pdf")
    sys.exit(1)

output_name = sys.argv[1]

directory = r"C:\PDFFiles"
output_file = os.path.join(directory, output_name)

merger = PdfMerger()

for filename in sorted(os.listdir(directory)):
    if filename.lower().endswith(".pdf"):
        merger.append(os.path.join(directory, filename))

merger.write(output_file)
merger.close()

print("Merged PDF created:", output_file)