import React, { useEffect, useState } from 'react';

function LearnerList() {
  const [learners, setLearners] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/learners')
      .then(response => response.json())
      .then(data => setLearners(data));
  }, []);

  return (
    <div>
      <h1>Learners</h1>
      <ul>
        {learners.map(learner => (
          <li key={learner.id}>
            {learner.name} (Nickname: {learner.nickname})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default LearnerList;
