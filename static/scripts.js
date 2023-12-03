// scripts.js

function toggleTheme() {
    const body = document.body;
    const themeIcon = document.getElementById('themeIcon');
    const themeIconDark = document.getElementById('themeIconDark');

    body.classList.toggle("light-mode");
    body.classList.toggle("dark-mode");

    // Toggle the visibility of the theme icons
    if (body.classList.contains('dark-mode')) {
        themeIcon.style.display = 'none';
        themeIconDark.style.display = 'inline-block';
    } else {
        themeIcon.style.display = 'inline-block';
        themeIconDark.style.display = 'none';
    }

    // Store the selected theme in a cookie or local storage
    const selectedTheme = body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('selectedTheme', selectedTheme);
}

// Function to set the initial theme
function setInitialTheme() {
    const body = document.body;
    const selectedTheme = localStorage.getItem('selectedTheme');

    if (selectedTheme === 'dark') {
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
    }
}

// Set the initial theme when the script loads
setInitialTheme();

function goBack() {
    window.history.back();
}