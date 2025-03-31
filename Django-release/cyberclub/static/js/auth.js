async function loginUser() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");

    errorMessage.textContent = "";

    try {
        const response = await fetch("/api/login/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem("access", data.access);
            localStorage.setItem("refresh", data.refresh);
            alert("Вы успешно вошли!");
            window.location.href = "/";  // Перенаправляем на главную
        } else {
            errorMessage.textContent = data.detail || "Ошибка входа";
        }
    } catch (error) {
        console.error("Ошибка сети:", error);
        errorMessage.textContent = "Ошибка сети. Попробуйте снова.";
    }
}
