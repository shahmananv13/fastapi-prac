from fastapi import FastAPI, File, UploadFile
import uvicorn
import string
from fastapi.exceptions import HTTPException


app = FastAPI()

@app.post("/upload")
async def upload_pdf(file: UploadFile):
	print(file.content_type)
	if file.content_type != 'application/pdf':
		raise HTTPException(400, 'Not a valid pdf file')
	return {"filetype": file.filename}


if __name__ == '__main__':
	uvicorn.run('main:app', host = "127.0.0.1", port = 8080, reload = True)
