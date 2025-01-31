import React from "react";
import { Navigate } from "react-router-dom";
import "../styles/Login.css";

function Login(){

const [fullName, setFullName] = React.useState('');
const [nickname, setNickname] = React.useState('');
const [error, setError] = React.useState('');
const [success,setSuccess] = React.useState(false);

function handleChange(event){
    const {name, value} = event.target;

    if (name === "fullName"){
        setFullName(value);
    } else if(name ==="nickname"){
        setNickname(value);
    }
}

function handleSubmit (event){
    event.preventDefault();


fetch(`http://127.0.0.1:5555/learners`)
.then(function(response){
    if(response.ok){
        return response.json();
    } else{
        throw new Error("No matching learner found.")
    }
})
.then(data =>{
    const foundLearner = data.find(
        (learner) => learner.name ===fullName && learner.nickname === nickname);
    if (foundLearner){
        setSuccess(true);
        setError("");
        console.log("Login successful");
        } else {
          setError("Invalid details. Please check your full name and nickname.");
        }
    })

.catch(function(error){
    setError("Error logging in:" + error.message);
});
}
if(success){
    return <Navigate to="/home" replace />
}

    return(
        <>
        <div className="form-container" id="login-form-container">
            
            <h2>Login</h2>
            {error && <p className="error">{error}</p>}
            {success && <p className="success">Log in successful! Welcome back.</p>}
            <form onSubmit={handleSubmit} className="login-form">
                <div className="form-area-container">
                <div className="form-area">
                <label>Learner: </label>
                <input
                type="text"
                className="input-area"
                id="fullName"
                name="fullName"
                value={fullName}
                placeholder="Enter your full name"
                onChange={handleChange}
                required
                />
                </div>


                <div className="form-area">
                <label>Nickname: </label>
                <input
                type="text"
                className="input-area"
                id="nickname"
                name="nickname"
                value={nickname}
                placeholder="Enter your nickname"
                onChange={handleChange}
                required
                />
                </div>
                </div>
                
                <div className="submit-btn-container" >
                <button className="btn" id="submit-btn" type="submit">Login</button>
                </div>
                
            </form>
            </div>
        </>
        
    )
}

export default Login;