// Sidebar.tsx
import React from "react";
import { NavLink } from "react-router-dom";

const Sidebar: React.FC = () => {
  return (
    <div className="hidden md:flex flex-col w-64 bg-gray-800">
      <div className="flex flex-col flex-1 overflow-y-auto">
        <nav className="flex-1 px-2 py-4 bg-gray-800">
          <NavLink
            to="/askanything"
            className="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6 mr-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M3 3a2 2 0 012-2h14a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V3zm4 4h10M5 10h10m-8 4h8"
              />
            </svg>
            Ask Anything
          </NavLink>
          <NavLink
            to="/upload"
            className="flex items-center px-4 py-2 mt-2 text-gray-100 hover:bg-gray-700"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6 mr-2"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5-5 5 5m-5-5v9" />
            </svg>
            Upload PDF
          </NavLink>

          <NavLink
            to="/reports"
            className="flex items-center px-4 py-2 mt-2 text-gray-100 hover:bg-gray-700"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6 mr-2"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path strokeWidth={2} d="M21 12l-4 4-4-4M7 14V4h10v10" />
            </svg>
            Reports
          </NavLink>
        </nav>
      </div>
    </div>
  );
};

export default Sidebar;