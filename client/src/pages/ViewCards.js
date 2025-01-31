import React, { useEffect } from "react";
import CardDisplay from "../Components/CardDisplay";
import "../styles/ViewCards.css";

function ViewCards({card, cards,loading,error,deleteCard}){


    return(
        <div className="view-cards">
        <h2>All Flashcards</h2>

        {loading && <p>Loading your flashcards...</p>}
        {error && <p style={{color:"red"}}>Error:{error}</p>}
       
       <div className="card-list">
            {cards.length > 0 ? (
                cards.map((card) => (
                    <CardDisplay 
                    key={card.id}
                    card={card}
                    level={card.level}
                    // hanzi={card.hanzi}
                    // pinyin={card.pinyin}
                    // englishTranslation={card.englishTranslation}
                    deleteCard={deleteCard}
                    />
                ))
            ) : (
                <p>No cards available yet. Create a new flashcard to get started.</p>
            )}
            
        </div>
    </div>
    );
}

export default ViewCards;