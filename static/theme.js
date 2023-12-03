// theme.js

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