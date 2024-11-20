const id = document.getElementById('d1').innerHTML;
const patente = document.getElementById('d2').innerHTML;
const fechat = document.getElementById('d3').innerHTML;
const horat = document.getElementById('d4').innerHTML;
const estado = document.getElementById('d5').innerHTML;
const precio = document.getElementById('d6').innerHTML;
// console.log(id.innerHTML);
    
document.getElementById("mypdf").addEventListener("click", () => {
    console.log('asd');
        
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    doc.setFontSize(20);
        doc.text("Detalle de Ticket", 10, 10);

    doc.setFontSize(12);
        doc.text(id, 10, 20);
        doc.text(patente, 10, 30);
        doc.text(fechat, 10, 40);
        doc.text(horat, 10, 50);
        doc.text(estado, 10, 60);
        doc.text(precio, 10, 70);
        doc.addImage('http://127.0.0.1:8000/static/tickets/img/qrcode.png', 'PNG', 10, 80, 50, 50);

    doc.save("dataticket.pdf");
});