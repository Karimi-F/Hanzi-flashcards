import React from "react";
import '../styles/CardDisplay.css';

function CardDisplay({card,deleteCard}){
    const {id,hanzi,pinyin,english_translation} = card;
    const[flipped,setFlipped]=React.useState(false);

    function handleFlip(){
        setFlipped(!flipped);
    }

    function handleDelete(){
        deleteCard(id);
    }

return(
        <>
        <div className={`card-display ${flipped ? "flipped" : ""}`} >
            <div className="card">
                {flipped ? 
            (
                <div className="card-back">
                    <h3>English Translation:</h3>
                    <p>{english_translation}</p>
                    <br/>
                    <br/>
                    <br/>
                </div>
                
            ) 
            : 
            (
                <div className="card-front">
                    <h3>Hanzi: </h3>
                    <p>{hanzi}</p>
                    <h3>Pinyin: </h3>
                    <p>{pinyin}</p>
                    <br/>
                </div>
            )
            }
            </div>
        
            <div className="btn-container" id="contain-btn"> 
                <button  
            className="display-btn"
            id="flip-btn"
            onClick={handleFlip}
            >
                Flip</button>

                <button
                className="display-btn"
                id="dlt-btn"
                onClick={handleDelete}
                >Delete</button>
                </div>
           
        </div>
        </>
    
    )
}

export default CardDisplay; 