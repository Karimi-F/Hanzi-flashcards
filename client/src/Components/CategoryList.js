import React, { useState, useEffect } from "react";
import CardDisplay from "../Components/CardDisplay";
import "../styles/CategoryList.css";
import { data } from "react-router-dom";

function CategoryList({selectedCategory}) {
    const [filteredCards, setFilteredCards] = useState([])
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null)

    useEffect(()=>{
        if (selectedCategory ===""){
            setFilteredCards([]);
            return;
        }
        setLoading(true);

        const category_id = parseInt(selectedCategory);

            console.log("Selected Category:", selectedCategory);
            console.log("Fetching cards for category:", category_id)

        fetch (`http://127.0.0.1:5555/category/${category_id}/cards`)
            .then((response)=>{
                if(!response.ok){
                    throw new Error("Failed to fetch cards.");
                }
                return response.json();
            })
            .then((data)=>{
                console.log("Fetched cards:", data)
                setFilteredCards(data);
                setLoading(false);
            })
            .catch((error)=>{
                setError(error.message);
                setLoading(false);
            });
    },[selectedCategory]);

    return (
        <div className="category-container">
            <h2>Flashcards by Category</h2>

            {loading && <p>Loading flashcards...</p>}
            {error && <p style={{color:"red"}}>Error:{error}</p>}

            <div className="card-list">
                {filteredCards.length > 0 ? (
                    filteredCards.map((card) => (
                        <CardDisplay key={card.id} card={card} />
                    ))
                ) : (
                    <p>No flashcards found for this category.</p>
                )}
            </div>
        </div>
    );
}

export default CategoryList;
