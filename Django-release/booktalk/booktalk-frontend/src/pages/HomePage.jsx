import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const HomePage = () => {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/posts/")
            .then((res) => {
                setBooks(res.data);
            })
            .catch((err) => {
                console.error("Ошибка при загрузке книг:", err);
            });
    }, []);

    return (
        <div>
            <h1>Книги</h1>
            {books.length === 0 ? (
                <p>Загрузка...</p>
            ) : (
                <ul>
                    {books.map((book) => (
                        <li key={book.id}>
                            <Link to={`/post/${book.id}`}>{book.title}</Link>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default HomePage;
