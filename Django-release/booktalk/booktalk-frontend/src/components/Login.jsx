import React, { useState } from 'react';
import axios from 'axios';

function Login({ onLogin }) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async e => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/auth/jwt/create/', {
                email,
                password
            });

            localStorage.setItem('access', response.data.access);
            localStorage.setItem('refresh', response.data.refresh);

            const userResponse = await axios.get('http://localhost:8000/auth/users/me/', {
                headers: {
                    Authorization: `Bearer ${response.data.access}`
                }
            });

            onLogin(userResponse.data);
        } catch (error) {
            alert("Неверный логин или пароль");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
            <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Пароль" />
            <button type="submit">Войти</button>
        </form>
    );
}

export default Login;
