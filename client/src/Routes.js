import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import CreateCards from './pages/CreateCards';
import ViewCards from './pages/ViewCards';
import LandingPage from './pages/LandingPage';
import CategoryList from './Components/CategoryList';

function RoutesComponent ({createCard,cards,deleteCard}){
    return(
        <Routes>
        <Route path="/" element={<LandingPage />}/>
        <Route path="/home" element={<Home />}/>
        <Route path="*" element={<Navigate to="/" replace />} />
        <Route path="/about" element={<About />}/>
        <Route path="/create-cards" element={<CreateCards createCard={createCard}/>}/>
        <Route path="/view-cards" element={<ViewCards  cards={cards}  deleteCard={deleteCard}/>}/>
        <Route path="/categories" element={<CategoryList  cards={cards}  deleteCard={deleteCard}/>}/>
      </Routes>
    );
}

export default RoutesComponent;