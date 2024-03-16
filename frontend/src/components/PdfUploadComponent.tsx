import React, { useState } from "react";

interface PdfFile {
  file: File;
}

const PdfUploadComponent: React.FC = () => {
  const [rows, setRows] = useState<PdfFile[][]>([[]]);
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleFileChange = (
    rowIndex: number,
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const files = Array.from(e.target.files || []);
    const errorMessage = files.some((file) => file.type !== "application/pdf")
      ? "Please select only PDF files."
      : "";
    setRows((prevRows) => {
      const newRows = [...prevRows];
      newRows[rowIndex] = files.map((file) => ({ file }));
      return newRows;
    });
    setErrorMessage(errorMessage);
  };

  const handleAddRow = () => {
    setRows((prevRows) => [...prevRows, []]);
  };

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      rows.flat().forEach((pdfFile, index) => {
        formData.append(`pdf${index}`, pdfFile.file);
      });
      const response = await fetch("https://127.0.0.1:8000/upload-pdf", {
        method: "POST",
        body: formData,
      });
      if (!response.ok) {
        throw new Error("Failed to upload PDF files");
      }
      setRows([[]]);
      setErrorMessage("");
      console.log("PDF files uploaded successfully");
    } catch (error) {
      console.error("Error uploading PDF files:", error);
      setErrorMessage("Failed to upload PDF files");
    }
  };
  return (
    <div className="p-4">
      {rows.map((row, rowIndex) => (
        <div key={rowIndex} className="mb-4">
          <input
            type="file"
            accept=".pdf"
            multiple
            onChange={(e) => handleFileChange(rowIndex, e)}
            className="mb-2"
          />
          {row.map((pdf, fileIndex) => (
            <div key={fileIndex} className="mb-2">
              <span className="mr-2">{pdf.file.name}</span>
              <span>({(pdf.file.size / 1024).toFixed(2)} KB)</span>
            </div>
          ))}
        </div>
      ))}
      <button
        onClick={handleAddRow}
        className="bg-blue-500 text-white px-4 py-2 rounded mr-2 hover:bg-blue-600"
      >
        Add PDF
      </button>
      <button
        disabled={!rows.flat().length || errorMessage.length > 0}
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Upload
      </button>
      {errorMessage && <p className="text-red-500 mt-2">{errorMessage}</p>}
    </div>
  );
};

export default PdfUploadComponent;
