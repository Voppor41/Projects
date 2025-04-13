import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import PostDetailPage from "./pages/PostDetailPage";
import BookList from "./components/BookList";
import Login from "./components/Login";
import Register from './components/Register';

function App() {
    const [token, setToken] = useState(localStorage.getItem("access"));

    useEffect(() => {
        const storedToken = localStorage.getItem("access");
        if (storedToken) {
            setToken(storedToken);
        }
    }, []);

    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/books" element={<BookList />} />
                <Route path="/post/:id" element={<PostDetailPage />} />
                <Route
                    path="/login"
                    element={
                        !token ? (
                            <Login setToken={setToken} />
                        ) : (
                            <Navigate to="/" />
                        )
                    }
                />
                <Route path="/" element={<HomePage />} />
                <Route path="/post/:id" element={<PostDetailPage />} />
                <Route path="/register" element={<Register />} />
            </Routes>
        </Router>
    );
}

export default App;
