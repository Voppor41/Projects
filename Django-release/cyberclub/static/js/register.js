async function registerUser() {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");

    errorMessage.textContent = "";

    const response = await fetch("/api/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email, password })
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem("access", data.access);
        localStorage.setItem("refresh", data.refresh);
        alert("Вы успешно зарегистрировались!");
        window.location.href = "/";
    } else {
        errorMessage.textContent = data.detail || "Ошибка регистрации";
    }
}
