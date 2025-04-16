import React, { useState, useEffect } from "react";
import axios from "axios";

const ProjectList = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/projects/").then((response) => {
      setProjects(response.data);
    });
  }, []);

  return (
    <div className="p-4">
      {projects.map((project) => (
        <div key={project.id} className="border p-4 mb-2">
          <h3>{project.title}</h3>
          <p>{project.description}</p>
        </div>
      ))}
    </div>
  );
};

export default ProjectList;