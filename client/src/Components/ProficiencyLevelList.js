import React, { useEffect, useState } from 'react';

function ProficiencyLevelList() {
  const [levels, setLevels] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/proficiencylevels')
      .then(response => response.json())
      .then(data => setLevels(data));
  }, []);

  return (
    <div>
      <h1>Proficiency Levels</h1>
      <ul>
        {levels.map(level => (
          <li key={level.id}>
            {level.name}: {level.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProficiencyLevelList;
