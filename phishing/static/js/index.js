
const menuButton = document.getElementById('menuButton');
const menu = document.getElementById('menu');

menuButton.addEventListener('click', () => {
    // Alterna la visibilidad del menú
    if (menu.style.display === 'none' || menu.style.display === '') {
        menu.style.display = 'flex'; // Muestra el menú
    } else {
        menu.style.display = 'none'; // Oculta el menú
    }
});
