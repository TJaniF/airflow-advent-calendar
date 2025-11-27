import React from 'react';

const DAGToggleWidget = () => {
  return (
    <button 
      style={{ padding: "10px", cursor: "pointer" }}
      onClick={() => alert("DAG Toggle clicked")}
    >
      Toggle DAG
    </button>
  );
};

export default DAGToggleWidget;

