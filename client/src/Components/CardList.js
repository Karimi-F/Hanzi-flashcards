import React, { useEffect, useState } from 'react';

function CardList() {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/cards')
      .then(response => response.json())
      .then(data => setCards(data));
  }, []);

  return (
    <div>
      <h1>Flashcards</h1>
      <ul>
        {cards.map(card => (
          <li key={card.id}>
            <p>{card.hanzi} ({card.pinyin})</p>
            <p>{card.english_translation}</p>
            <p>HSK Level: {card.hsk_level}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CardList;
