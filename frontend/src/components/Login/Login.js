import React from 'react';
// basic react login UI component for user login using spotfiy PKCE flow
// uses the spotify web api to authenticate the user and get the access token
// and refresh token

function Login() {

    const handleLogin = () => {
        // redirect to django's login/authenticate route
        window.location.href = 'http://localhost:8000/spotify/login';
    };

    return (
        <button onClick={handleLogin} className="login-button">Login</button>
    );
}

export default Login;
