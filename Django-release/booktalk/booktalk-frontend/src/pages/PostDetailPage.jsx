import React from "react";
import { useParams } from "react-router-dom";

const PostDetailPage = () => {
    const { id } = useParams();

    return (
        <div>
            <h2>Детали книги #{id}</h2>
            <p>Здесь будет информация о книге.</p>
        </div>
    );
};

export default PostDetailPage;
