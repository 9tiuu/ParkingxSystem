
const GraphContent = document.getElementById('ticketgraph');
const ene = document.getElementById('ene').innerHTML;
const feb = document.getElementById('feb').innerHTML;
const mar = document.getElementById('mar').innerHTML;
const abr = document.getElementById('abr').innerHTML;
const may = document.getElementById('may').innerHTML;
const jun = document.getElementById('jun').innerHTML;
const jul = document.getElementById('jul').innerHTML;
const ago = document.getElementById('ago').innerHTML;
const sep = document.getElementById('sep').innerHTML;
const oct = document.getElementById('oct').innerHTML;
const nov = document.getElementById('nov').innerHTML;
const dic = document.getElementById('dic').innerHTML;

// Grafico | Tickets de Entrada (Estatico)  --------------------------------

const title = 'Tickets de Entrada generados';
const maxValue = [Number(ene), Number(feb), Number(mar), Number(abr), Number(may), Number(jun), Number(jul), Number(ago), Number(sep), Number(oct), Number(nov), Number(dic),];
console.log(maxValue);

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
        cutout: 80
    }
});

const GraphContent4 = document.getElementById('ticketgraph4');
const daydata = document.getElementById('daydata').innerHTML;
const frecdata = document.getElementById('frecdata').innerHTML;

let ticketGraph4 = new Chart(GraphContent4, {
    type: 'doughnut',
    data: {
        labels: [daydata],
        datasets: [{
            data: [frecdata],
            backgroundColor: mainColor,
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
        cutout: 80
    }
});
