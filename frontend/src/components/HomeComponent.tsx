import React from "react";
import Header from "./Header";
import Sidebar from "./Sidebar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Playground } from "./playground";
import FileUploadComponent from "./PdfUploadComponent";

const HomeComponent: React.FC = () => {
  return (
    <Router>
      <div className="h-screen bg-slate-300">
        <Header />
        <div className="flex h-screen bg-gray-100">
          <Sidebar />
          <div className="p-2">
            <Routes>
              <Route path="/" element={<Playground />} />
              <Route path="/askanything" element={<Playground />} />
              <Route path="/upload" element={<FileUploadComponent />} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
};

export default HomeComponent;
