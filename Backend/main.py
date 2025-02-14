from fastapi import FastAPI,Form
from groq import Groq
import os
from dotenv import load_dotenv
from fastapi import UploadFile
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database import get_db
from models import Feedback

from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

client = Groq(
    api_key=os.environ.get("API_KEY"),
)

@app.post("/analyze")
async def analyze(file:UploadFile=None,text:str=Form(None),db: AsyncSession = Depends(get_db)):
  if not file and not text:
        raise HTTPException(status_code=400, detail="Either file or text parameter is required")
  
  text_content=""

  if file:
    try:   
      content = await file.read()  
      text_content = content.decode("utf-8")

    except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")
    
  if text:
    text_content=text

  try:
    data = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": f"Find the Vulnerabilities and provide suggestions for the following logs if there exists vulnerability. Also list all the vulnerabilities.\n{text_content}",
          }
      ],
      model="llama-3.3-70b-versatile",
    )
    content=data.choices[0].message.content
  except Exception as e:
     raise HTTPException(status_code=500,detail=f"Error while fetching the response: {str(e)}")

  new_record = Feedback(filename=file.filename if file else None, feedback_response=content)
  db.add(new_record)
  await db.commit()
  await db.refresh(new_record)

  return {"result":"Success","data":content}



  