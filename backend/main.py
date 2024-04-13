import os
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, HTTPException
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

app = FastAPI()

load_dotenv()

# Azure credentials
subscription_key = os.getenv("RESOURCE_KEY")
endpoint = os.getenv("VISION_URL")

if not subscription_key or not endpoint:
    raise EnvironmentError("Azure subscription key or endpoint is not provided.")

# Initialize Computer Vision client
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Check if the file is an image
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=415, detail="Unsupported media type")

    # Perform OCR on the image
    ocr_results = computervision_client.recognize_printed_text_in_stream(file.file)

    # Extract recognized text
    extracted_text = ""
    for region in ocr_results.regions:
        for line in region.lines:
            print(line)
            extracted_text += " ".join([word.text for word in line.words]) + "\n"

    return {"text": extracted_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)