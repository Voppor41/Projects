import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Register() {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [rePassword, setRePassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();

    try {
      console.log({ email, username, password, re_password: rePassword }); // отладка
      await axios.post('http://localhost:8000/api/auth/users/', {
        email,
        username,
        password,
        re_password: rePassword
      });

      alert("Регистрация успешна!");
      navigate('/login');
    } catch (error) {
      if (error.response) {
        console.log(error.response.data);
        alert("Ошибка: " + JSON.stringify(error.response.data));
      } else {
        console.error(error);
        alert("Неизвестная ошибка.");
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Регистрация</h2>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Имя пользователя"
        value={username}
        onChange={e => setUsername(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Пароль"
        value={password}
        onChange={e => setPassword(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Повторите пароль"
        value={rePassword}
        onChange={e => setRePassword(e.target.value)}
        required
      />
      <button type="submit">Зарегистрироваться</button>
    </form>
  );
}

export default Register;
