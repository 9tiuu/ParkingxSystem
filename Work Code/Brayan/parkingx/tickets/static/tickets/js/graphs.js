
const GraphContent = document.getElementById('ticketgraph');

// Grafico | Tickets de Entrada (Estatico)  --------------------------------

const title = 'Tickets de Entrada generados';
const maxValue = [10, 20, 40, 23, 80, 30, 50, 50, 78, 60, 80, 20,];
const months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Agos', 'Sep', 'Oct', 'Nov', 'Dic'];
const mainColor = '#396af1';

let ticketGraph = new Chart(GraphContent, {
    type: 'bar',
    data: {
        labels: months,
        datasets: [{
            label: title,
            data: maxValue,
            backgroundColor: mainColor,
            borderColor: mainColor,
            borderRadius: 5,
            borderWidth: 1,
            tension: 0.2,   
            fill: true     
        }]      
    }, 
    options: {
        scales: {
            y: { 
                beginAtZero: true 
            }
        },
        plugins: {
            legend: { 
                position: 'bottom', 
                labels: { usePointStyle: true, }
            },
        }
    }
});

// Grafico | ??? --------------------------------

const GraphContent3 = document.getElementById('ticketgraph3');
const monthsColors = [
    '#03a9f4', '#fe6383', '#7542f5',
    '', '', '', 
    '', '', '', 
    '', '', ''
];

let ticketGraph3 = new Chart(GraphContent3, {
    type: 'doughnut',
    data: {
        labels: months,
        datasets: [{
            data: [50500, 35990, 67850],
            backgroundColor: monthsColors,
            borderWidth: 0,               
        }]     
    }, 
    options: {
        responsive: true,
        plugins: {
            legend: { 
                title: 'asd',
                position: 'right', 
                labels: { usePointStyle: true, },
                display: false
            },
        }, 
        cutout: 70
    }
});
