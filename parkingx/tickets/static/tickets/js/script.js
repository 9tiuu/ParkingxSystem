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


const dateForm = document.getElementById('date-form');
const hourForm = document.getElementById('hour-form');
const fecha = new Date();

const dia = String(fecha.getDate()).padStart(2, '0'); // Día con 2 dígitos
const mes = String(fecha.getMonth() + 1).padStart(2, '0'); // Mes con 2 dígitos (se suma 1 porque los meses comienzan en 0)
const año = String(fecha.getFullYear());
const fechaactual = `${año}-${mes}-${dia}`;

const hora = String(fecha.getHours()).padStart(2, '0');
const min = String(fecha.getMinutes()).padStart(2, '0');
const horaactual = `${hora}:${min}`;

dateForm.value = fechaactual;
hourForm.value = horaactual;

// console.log(horaactual);