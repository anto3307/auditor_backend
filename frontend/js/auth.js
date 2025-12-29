async function login() {
    // DEBUG: confirms button click
    alert("Login button clicked");

    // Get input values
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Simple validation
    if (!email || !password) {
        alert("Please enter email and password");
        return;
    }

    try {
        const response = await fetch(
            "https://auditor-backend-9rww.onrender.com/api/login",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: email,
                    password: password
                })
            }
        );

        const result = await response.json();

        if (response.ok) {
            alert(result.message);

            // NEXT STEP (later)
            // window.location.href = "dashboard.html";
        } else {
            alert(result.message);
        }

    } catch (error) {
        console.error(error);
        alert("Backend connection failed");
    }
}
