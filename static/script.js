let menu = document.getElementById("nav");
let open = document.getElementById("menu-btn");
let close = document.getElementById("close");

function openmenu() {
    menu.style.left = "0";
    open.style.display = "none";
    close.style.display = "block";
}
function closemenu() {
    menu.style.left = "-100%";
    open.style.display = "block";
    close.style.display = "none";
}

// nav bg color change

function change() {
    var nav = document.getElementById("navbar");
    var value = window.scrollY;
    if (value > 80) {
        nav.classList.add("nav-change");
    } else {
        nav.classList.remove("nav-change");
    }
}

window.addEventListener("scroll", change);

const userLink = document.getElementById("user");

// Check if there is a user key in local storage
if (localStorage.getItem("user")) {
    // Replace the "Login" link with a logout button
    const logoutButton = document.createElement("button");
    logoutButton.classList.add("logout-btn");
    logoutButton.innerHTML = "Logout";
    logoutButton.addEventListener("click", function () {
        // Clear the user key from local storage
        localStorage.removeItem("user");
        // Redirect to the login page
        window.location.href = "/login";
    });
    userLink.parentNode.replaceChild(logoutButton, userLink);
}
