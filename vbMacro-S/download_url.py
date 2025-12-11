import requests

url = "https://ubars.energysolve.com/AU/Interop/Image/0b2b3675-ad3f-43c7-8b8a-bbab4e30a81d"
output_path = r"C:\PDFFiles\32984393.pdf"

try:
    response = requests.get(url)
    response.raise_for_status()   # Raise error for bad status codes

    with open(output_path, "wb") as file:
        file.write(response.content)

    print("File downloaded successfully:", output_path)

except Exception as e:
    print("Error downloading the file:", e)