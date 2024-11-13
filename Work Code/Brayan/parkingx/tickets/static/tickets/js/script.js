const dropdown = document.getElementById('profile-menu');
const avatar = document.getElementById('avatar');

dropdown.classList.add('disabled');

avatar.addEventListener('click', () => {
    if (dropdown.classList.contains('disabled')) {
        dropdown.classList.remove('disabled');
        dropdown.classList.add('active');

    } else {
        dropdown.classList.remove('active');
        dropdown.classList.add('disabled');
    };
});