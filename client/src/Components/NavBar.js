import React from "react";
import {Link} from "react-router-dom";
import "../styles/NavBar.css";


function NavBar(){
    return(
        <nav className="navbar">
            <h1>Hanzi FlashCards</h1>
            <ul className="navbar-links">
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/about">About</Link>
                </li>
                <li>
                    <Link to="/create-cards">Create Cards</Link>
                </li>
                <li>
                    <Link to="/view-cards">View Cards</Link>
                </li>
            </ul>
        </nav>
    )
}

export default NavBar;