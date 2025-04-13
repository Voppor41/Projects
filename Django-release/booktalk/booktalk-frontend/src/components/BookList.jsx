import React, { useEffect, useState } from 'react';
import axios from 'axios';

const BookList = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/books/")
      .then((res) => {
        setBooks(res.data);
      })
      .catch((err) => {
        console.error("Ошибка при получении книг:", err);
      });
  }, []);

  return (
    <div>
      <h2>Список книг</h2>
      <ul>
        {books.map((book) => (
          <li key={book.id}>
            <strong>{book.title}</strong> — {book.author}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookList;
