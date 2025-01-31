import React, { useState, useEffect } from "react";
import CardDisplay from "../Components/CardDisplay";
import "../styles/CategoryList.css";

function Category({cards}) {
    const [selectedCategory, setSelectedCategory] = useState("all");

    function handleCategoryChange(event) {
        setSelectedCategory(event.target.value);
    }

    const filteredCards =
        selectedCategory === "all"
            ? cards
            : cards.filter((card) => card.category_id.toString() === selectedCategory);

    return (
        <div className="category-container">
            <h2>Flashcards by Category</h2>

            <div className="filter-category-container">
                <label>Filter by Category: </label>
                <select value={selectedCategory} onChange={handleCategoryChange}>
                    <option value="all">All Categories</option>
                    <option value="1">Greetings</option>
                    <option value="2">Colors</option>
                    <option value="3">Common phrases</option>
                    <option value="3">Numbers</option>
                    <option value="3">Directions</option>
                    {/* Add more categories based on your database */}
                </select>
            </div>

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

export default Category;
