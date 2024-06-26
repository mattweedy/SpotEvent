import React from 'react';
import { useDynamicHeight } from '../components/General/useDynamicHeight';
import { useNavigate } from 'react-router-dom';

function Home() {
    const navigate= useNavigate();
    useDynamicHeight(); // solves sidebar height issue but extends page size for this page only

    return (
        <div className="home-page">
            <h1 className="home-page-title">Welcome to Event<span>Spot</span></h1>
            <h4 className="home-page-text">To begin getting recommendations, you need to setup your <span onClick={() => navigate('/preferences')}>preferences</span>.</h4>
            <p className="home-page-text">Don't worry, you can change these at any time, and can even skip them all together if you want.</p>

            <button className="preferences-form-button" id="home-page-button" onClick={() => navigate('/preferences')}>
                Edit Preferences
            </button>

            <h4 className="home-page-text">Or you can take a look through <span onClick={() => navigate('/events')}>all events</span> currently available.</h4>
            <button className="preferences-form-button" id="home-page-button" onClick={() => navigate('/events')}>
                All Events
            </button>
        </div>
    );
}

export default Home;