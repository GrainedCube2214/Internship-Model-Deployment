// scripts.js

// Function to toggle the theme
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

    // Store the selected theme in local storage
    const selectedTheme = body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('selectedTheme', selectedTheme);
}

function goBack() {
    window.history.back();
}