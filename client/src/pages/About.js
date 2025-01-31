import React from "react";
import '../styles/About.css';

function About() {
    return (
      <div className="about">
        <h1>About Hanzi Flashcards</h1>
        <p>
          Welcome to Hanzi Flashcards app. This application is here to help you
          study and retain Chinese vocabulary using flashcards. You can create new
          flashcards and specify level of interest when studying and revising.
        </p>
        <h2>Features</h2>
        <div className="list-container">
        <ol>
          <li>
            <strong>Flashcard Creator:</strong>
            Create and personalize your own flashcards.
          </li>
          <li>
            <strong>Flashcard Viewer:</strong>
            Flip through to revise your Chinese vocabulary.
          </li>
          <li>
            <strong>Level Selector:</strong>
            Choose and specify the HSK level you want to study and revise for.
          </li>
        </ol>
        </div>
       
        <h2>How to use</h2>
        <p>
          First things first is creating your flashcards. Start by choosing and
          specifying your hsk level of interest and creating your own personalized
          flashcard. You can view them in the View Flashcards section. As you go
          through each flashcard try to say your answer out loud before flipping
          the card in order to maximize retention.{" "}
        </p>
  
        <p>
          We hope this app makes learning a tad bit easier, fun and effective.
          Happy studying or as it is said in China 
          <strong> 学习愉快!</strong>
        </p>
      </div>
    );
  }
  
  export default About;
  