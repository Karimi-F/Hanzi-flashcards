import React from 'react';
import SignUp from '../Components/SignUp';
import Login from '../Components/Login';
import '../styles/LandingPage.css';

function LandingPage(){

    const [showSignUp, setShowSignUp] = React.useState(false);
    const [showLogin, setShowLogin] = React.useState(false);
    
    function handleSignUpClick(){
        setShowSignUp(true);
        setShowLogin(false);
    }

    function handleLoginClick(){
        setShowLogin(true);
        setShowSignUp(false);
    }
    
    return (
      <div className='landing-page-container'> 
      <br></br>     
      <br></br>     
      <h2> Welcome to Hanzi Flashcards</h2>
      <p>Countries and their IDs</p>
        <ul>China - 1</ul>
        <ul>Japan - 2</ul>
        <ul>Kenya - 3</ul>
        <ul>Madagascar - 4</ul>
        <ul>Botswana - 5</ul>
      <div className='button-container'>
        <button onClick={handleSignUpClick} className='button button-signup'>SignUp</button>
        <button onClick={handleLoginClick} className='button button-login'>Login</button>
      </div> 

       <div className='form-container'>
        {showSignUp && <SignUp />}
        {showLogin && <Login />}
      </div>
      
      </div>  
    )
}

export default LandingPage;