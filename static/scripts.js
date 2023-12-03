function toggleTheme() {
    const body = document.body;
    const themeIcon = document.getElementById('themeIcon');
    const themeIconDark = document.getElementById('themeIconDark');

    body.classList.toggle("light-mode");
    body.classList.toggle("dark-mode");

    // Toggle the visibility of the theme icons
    themeIcon.style.display = themeIcon.style.display === 'none' ? 'inline-block' : 'none';
    themeIconDark.style.display = themeIconDark.style.display === 'none' ? 'inline-block' : 'none';
}
function goBack() {
    window.history.back();
}