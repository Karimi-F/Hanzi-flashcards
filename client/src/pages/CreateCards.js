import React from "react";
import "../styles/CreateCards.css";

function CreateCards({createCard}){

    //state variables
const[hskLevel,setHskLevel] = React.useState("");
const[hanzi,setHanzi] = React.useState("");
const[pinyin,setPinyin] = React.useState("");
const[englishTranslation,setEnglishTranslation] = React.useState("");
const[category,setCategory] = React.useState("");
const[message,setMessage] = React.useState("");

const levels = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const categories = [
    { id: 1, name: "Greetings" },
    { id: 2, name: "Colors" },
    { id: 3, name: "Common Phrases" },
    { id: 4, name: "Numbers" },
    { id: 5, name: "Directions" },
    // Add more categories as needed
  ];

//functions that are handling the change in the input fields
function handleHskLevelChange(event){
    setHskLevel(event.target.value);
}
function handleHanziChange(event){
    setHanzi(event.target.value);
}

function handlePinyinChange(event){
    setPinyin(event.target.value);
}

function handleEnglishTranslationChange(event){
    setEnglishTranslation(event.target.value);
}

function handleCategoryChange(event){
    setCategory(event.target.value);
}


function handleSubmit(event){
    event.preventDefault();


//Conditional operation that ensures all fields are filled
if (!hskLevel || !hanzi || !pinyin || !englishTranslation || !category){
    setMessage("Please fill in all fields.");
    return;
}

const newCard = {
    hsk_level:hskLevel, 
    hanzi, 
    pinyin, 
    english_translation:englishTranslation,
    category_id:parseInt(category)
};

fetch("http://127.0.0.1:5555/cards",{
    method: "POST",
    headers: {
        'Content-Type' : 'application/json',
    },
    body:JSON.stringify(newCard),
})
.then((response) => response.json())
.then((data) => {
    setMessage("Card created successfully!");
    createCard(data);
    //resets the input fields
    setHskLevel("");
    setHanzi("");
    setPinyin("");
    setEnglishTranslation("");
    setCategory("")
})
.catch((error)=>{
    setMessage("Error creating card")
    console.error('Error:',error);
});
}

    return(
        <div className="form-container">
            <h2>Create a New Card</h2>
            <form onSubmit={handleSubmit}>
            <label>HSK Level: </label>
                <select
                value={hskLevel}
                onChange={handleHskLevelChange}>
                    <option value="">Select a HSK Level</option>
                    {levels.map((level)=>(
                        <option 
                        key={level}
                        value={level}
                        >Level {level}</option>
                    ))}
                </select>
                <br/>
                <br/>

                <label>Hanzi: </label>
                <input
                id="hanzi"
                type="text"
                value={hanzi}
                onChange={handleHanziChange}
                />
                <br/>
                <br/>

                <label>Pinyin: </label>
                <input
                id="pinyin"
                type="text"
                value={pinyin}
                onChange={handlePinyinChange}
                />
                <br/>
                <br/>

                <label>English Translation: </label>
                <input
                id="english-translation"
                type="text"
                value={englishTranslation}
                onChange={handleEnglishTranslationChange}
                />
                <br/>
                <br/>

                <label>Category: </label>
                <select value={category} onChange={handleCategoryChange}>
                 <option value="">Select a Category</option>
                 {categories.map((category) => (
                    <option key={category.id} value={category.id}>
                    {category.name}
                  </option>
                 ))}
                 </select>
                <br/>
                <br/>
                <div className="btn-container">
                <button type="submit" className="btn">Create</button>
                </div>
                
            </form>
        </div>
    )
}

export default CreateCards;