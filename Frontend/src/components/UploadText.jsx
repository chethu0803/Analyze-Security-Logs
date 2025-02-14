import React from 'react'

const UploadText = ({setInput}) => {
  
  return (
    <div className="relative w-[45%] h-[50vh] bg-white border-2 rounded-lg p-4 flex items-center">
    <textarea
      placeholder="Enter security logs"
        className="absolute top-0 left-0 w-full h-full p-4 border-none bg-transparent outline-none resize-none"
        onChange={(e) => setInput(e.target.value)}
    />
</div>

  

  )
}

export default UploadText