import { UploadCloud } from "lucide-react";
import {useDropzone } from "react-dropzone";
import { useState } from "react";

const FileDropZone = ({setInput }) => {
  const [filename, setFilename] = useState(null);

  const onDrop = async (acceptedFiles) => {
    const uploadedFile = acceptedFiles[0];
    setInput(uploadedFile);
    setFilename(uploadedFile.name);
  };

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    accept: {
      "text/plain": [".txt"],
    },
  });
  return (
    <div {...getRootProps()} className="flex flex-col justify-center items-center  w-[45%] h-[50vh] border-2 border-dashed bg-gray-100 cursor-pointer rounded-lg">
      <input {...getInputProps()} />
      <UploadCloud className="mx-auto mb-2 text-gray-600" size={32} />
      <p className="text-gray-500">Drag and drop some files here, or click to select files</p>
      {filename && <p className="mt-2 text-gray-800 font-semibold">Selected: {filename}</p>}
    </div>
  )
}

export default FileDropZone