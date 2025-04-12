import React, { useEffect } from "react";
import CardDisplay from "../Components/CardDisplay";
import CategoryList from "../Components/CategoryList";
import "../styles/ViewCards.css";

function ViewCards({card, cards,loading,error,deleteCard}){
    const [selectedCategory, setSelectedCategory] = React.useState("");

    function handleCategoryChange(event){
        setSelectedCategory(event.target.value);
    }

    return(
        <div className="view-cards">
             <div className="filter-category-container">
            <label>Filter By Category:</label>
            <select value={selectedCategory} onChange={handleCategoryChange}>
                <option value=""> All Categories</option>
                <option value="1"> Greetings</option>
                <option value="2"> Directions</option>
                <option value="3"> Numbers</option>
                <option value="4"> Colors</option>
                <option value="5"> Common Phrases</option>
            </select>
        </div>
        <CategoryList selectedCategory={selectedCategory}/>

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