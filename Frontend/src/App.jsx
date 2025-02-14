import { useState } from 'react'
import './App.css'
import FileDropZone from './components/FileDropZone'
import UploadText from './components/UploadText'
import axios from 'axios'
import React from "react";
import ReactMarkdown from "react-markdown";


function App() {
  const [input,setInput]=useState(null)
  const [response, setResponse] = useState(null)
  const [loading,setLoading]=useState(false)

  const handleSubmit = async (input) => {
    const formData = new FormData();
    console.log(input);
    if (input instanceof File) {
      formData.append("file", input);
    } else if (typeof input === "string") {
      formData.append("text", input);
    }
    try {
      setLoading(true);
      const groq_response = await axios.post("http://localhost:8000/analyze", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      console.log(groq_response);
      setResponse(groq_response.data.data)
    }
    catch (error) {
      console.error(error);
    }
    finally {
      setLoading(false);
    }

  }
  return (
    <>
      <div className='flex flex-col  w-[70%] h-[100vh] mx-auto p-3 ' >
        {!response?(<p className="text-center font-bold text-4xl w-full my-6 ">Welcome to <span className="text-green-500 ">Security Logs Analyzer,</span></p>):(<p className="text-center font-bold text-4xl w-full my-6 ">Security Logs <span className="text-green-500 ">Report:</span></p>)}
        
        {!response ? ( 
          <div>
            <div className='flex flex-row justify-center items-center gap-3'>
              <FileDropZone setInput={setInput}/>
              <p className='font-bold'>OR</p>
              <UploadText setInput={setInput}/>
            </div>
            <div className='flex justify-center items-center mt-3 '>
              {loading ? (<div className="w-6 h-6 border-4 border-green-500 border-t-transparent rounded-full animate-spin"></div>) : (<button onClick={() => handleSubmit(input)} className="bg-green-500 text-white px-4 py-2 rounded-lg">Analyze</button>)}
              
            </div>
          </div>
        ) : (
            <div className="border-2 p-4 rounded-lg bg-gray-300 break-words w-full mx-auto mb-10 overflow-auto">
              <ReactMarkdown>{response }</ReactMarkdown>
            </div>
          )
        }
      </div>
    </>
  )
}

export default App
