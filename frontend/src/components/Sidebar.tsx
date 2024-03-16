// Sidebar.tsx
import React from "react";
import { NavLink } from "react-router-dom";

const Sidebar: React.FC = () => {
  return (
    // <nav className="text-black w-64 p-4">
    //   <ul>
    //     <li className="mb-2">
    //       <NavLink to="/askanything" className="block p-2 hover:bg-gray-400">
    //         Ask Anything
    //       </NavLink>
    //     </li>
    //     <li className="mb-2">
    //       <NavLink to="/upload" className="block p-2 hover:bg-gray-400">
    //         Upload PDF's
    //       </NavLink>
    //     </li>
    //   </ul>
    // </nav>

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
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
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
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
            Upload PDF's
          </NavLink>
        </nav>
      </div>
    </div>
  );
};

export default Sidebar;
