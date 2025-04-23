import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
  fetch('http://localhost:8000/polls/api/questions/?format=json')
    .then(res => res.json())
    .then(data => {
      console.log('отримали з бекенду:', data);
      setQuestions(data);
    })
    .catch(err => console.error('Fetch error:', err));
}, []);

  return (
    <div>
      {questions.map((q, idx) => (
        <div key={idx}>
          <h1>{q.question_text}</h1>
          <p>{q.pub_date}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
