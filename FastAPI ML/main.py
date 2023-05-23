from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    contents = await pdf_file.read()
    # Perform further processing or save the PDF file
    return {"filename": pdf_file.filename}
