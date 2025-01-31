import React from "react";
import "../styles/Home.css";
// import image from "../assets/images/Chinese.jpg";


function Home() {

  return (
    <>
      <div className="home">
        <h2>Welcome to Hanzi FlashCards</h2>
        <div className="container">
        <div className="paragraph">
        <p>
          Welcome to our Hanzi Flashcards website! Our platform offers a simple
          yet effective way to learn Chinese characters through interactive
          flashcards. Each card features the Pinyin on one side and the English
          translation on the other, making it easy to test and reinforce your
          knowledge. Flip the cards to reveal their meanings, practice
          pronunciation, and gradually build your understanding of Chinese
          characters. Whether you're just starting out or looking to refresh
          your skills, our flashcards are designed to help you learn at your own
          pace. Start flipping today and unlock the world of Chinese language
          and culture! The it tool for studying and revising Chinese effectively
          with flashcards.{" "}
        </p>
        </div>
      
          {/* <div className="img-container">
            <img src={image} alt="Chinese characters" />
          </div> */}
        </div>
        
      </div>
    </>
  );
}

export default Home;
