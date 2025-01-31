import React from "react";
import { Navigate } from "react-router-dom";
import "../styles/SignUp.css";

function SignUp(){

    const[learner,setLearner] = React.useState("");
    const[nickname,setNickname] = React.useState("");
    const[country,setCountry] = React.useState("");
    const[error,setError] = React.useState("");
    const[success,setSuccess] = React.useState(false);
    const[isSubmitting,setIsSubmitting] = React.useState(false);
 
function handleChange(event){
    const {name,value} = event.target;
    if (name === "learner"){
        setLearner(value);
    } else if (name === "nickname"){
        setNickname(value);
    }else if (name === "country"){
        setCountry(value);
    }
}
function handleSubmit(event){
    event.preventDefault();

if (!learner || !nickname || !country){
    setError("Please fill in all details.");
    return;
}
const countryId = parseInt(country);
if (isNaN(countryId)){
    setError("Please enter a valid country ID.");
    return;
}
const newLearner = {
    name:learner, 
    nickname:nickname, 
    country_id:countryId
};
console.log("Sending data:", newLearner);
setIsSubmitting(true);

fetch("http://127.0.0.1:5555/learners",{
    method:"POST",
    headers:{
        "Content-Type":"application/json"
    },
    body:JSON.stringify(newLearner)
})
.then(function(response){
    return response.json();
})
.then(function(data){
    setSuccess(true);
    setError("");
    console.log("Learner successfully signed up:",data);
})
.catch(function(error){
    setError("Error signing up. Try again."+ error.message);    
})
.finally(() => setIsSubmitting(false));
} 

if (success){
    return <Navigate to="/home" replace />;
}
    return(
        <div className="form-container">
             <h2>New here? Sign up</h2>
             {error && <p className="error">{error}</p>}
             {success && <p className="success">Sign up successful! Welcome.</p>}
        <form className="sign-up-form" onSubmit={handleSubmit}>
           <div className="form-group">
            <label>Learner:</label>
            <input
            type="text"
            name="learner"
            value={learner}
            placeholder="Enter your full name"
            onChange={handleChange}
            disabled={isSubmitting}
            />
           <label>Nickname: </label>
            <input
            type="text"
            id="nickname"
            name="nickname"
            value={nickname}
            placeholder="Enter your nickname"
            onChange={handleChange}
            disabled={isSubmitting}
            />
           </div>
            <br/>

            <div className="form-group">
            <label>Country: </label>
            <input
            type="text"
            id="country"
            name="country"
            value={country}
            placeholder="Enter country you reside in"
            onChange={handleChange}
            disabled={isSubmitting}
            />
            </div>
            <br/>

            <br/>
            <button 
            type="submit"
            className="btn"
            >
                Sign up</button>
        </form>
        </div>
    );

}
export default SignUp;