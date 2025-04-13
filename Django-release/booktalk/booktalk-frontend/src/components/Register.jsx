// src/components/Register.jsx
import React, { useState } from "react";
import axios from "axios";

function Register() {
    const [formData, setFormData] = useState({ username: "", password: "" });

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post("http://localhost:8000/api/auth/register/", formData)
            .then((res) => alert("Успешно зарегистрирован!"))
            .catch((err) => alert("Ошибка регистрации"));
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Регистрация</h2>
            <input name="username" placeholder="Имя" onChange={handleChange} />
            <input name="password" type="password" placeholder="Пароль" onChange={handleChange} />
            <button type="submit">Зарегистрироваться</button>
        </form>
    );
}

export default Register;
