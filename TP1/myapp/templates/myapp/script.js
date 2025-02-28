document.addEventListener("DOMContentLoaded", async () => {
    await loadNavbar();
    initializeLanguage();
    initializeDarkMode();
});

async function loadNavbar() {
    try {
        const response = await fetch("navbar.html");
        const data = await response.text();
        document.getElementById("navbar-container").innerHTML = data;
        document.querySelector('[onclick="changeLanguage(\'en\')"]').addEventListener("click", () => changeLanguage("en"));
        document.querySelector('[onclick="changeLanguage(\'fr\')"]').addEventListener("click", () => changeLanguage("fr"));

    } catch (error) {
        console.error("Error loading navbar:", error);
    }
}


function initializeDarkMode() {
    const darkModeSetting = localStorage.getItem('darkMode');
    const body = document.body;
    const darkModeToggle = document.getElementById('dark-mode-toggle');

    if (darkModeSetting === 'enabled') {
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
    }

    if (darkModeToggle) {
        darkModeToggle.innerText = darkModeSetting === 'enabled' ? "☀️" : "🌙";
    }
}


async function initializeLanguage() {
    const savedLanguage = localStorage.getItem('language') || 'en';
    const langData = await fetchLanguageData(savedLanguage);
    updateContent(langData);
}


function updateContent(langData) {
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (langData[key]) {
            element.innerHTML = langData[key];
        }
    });
}


async function fetchLanguageData(lang) {
    const response = await fetch(`languages/${lang}.json`);
    return response.json();
}


async function changeLanguage(lang) {
    localStorage.setItem('language', lang);
    const langData = await fetchLanguageData(lang);
    updateContent(langData);
}


function toggleDarkMode() {
    const body = document.body;
    const darkModeToggle = document.getElementById('dark-mode-toggle');

    if (!darkModeToggle) return;

    let isDarkMode = localStorage.getItem('darkMode') === 'enabled';

    if (isDarkMode) {
        localStorage.setItem('darkMode', 'disabled');
        body.classList.remove('dark-mode');
        darkModeToggle.innerText = "🌙";
    } else {
        localStorage.setItem('darkMode', 'enabled');
        body.classList.add('dark-mode');
        darkModeToggle.innerText = "☀️";
    }
}

function updateDarkModeButton() {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (!darkModeToggle) return;

    const darkModeSetting = localStorage.getItem('darkMode');
    darkModeToggle.innerText = darkModeSetting === 'enabled' ? "☀️" : "🌙";
}