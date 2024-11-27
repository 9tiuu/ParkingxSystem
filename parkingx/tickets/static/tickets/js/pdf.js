const id = document.getElementById('d1').innerHTML;
const patente = document.getElementById('d2').innerHTML;
const fechat = document.getElementById('d3').innerHTML;
const horat = document.getElementById('d4').innerHTML;
const estado = document.getElementById('d5').innerHTML;
const precio = document.getElementById('d6').innerHTML;
const qrcode = document.getElementById('qrcode');
    
document.getElementById("mypdf").addEventListener("click", () => {
    const patenteValue = document.getElementById('patente').innerHTML;
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

    html2canvas(qrcode, {
        onrendered: function(canvas) {
            const imgData = canvas.toDataURL("image/png"); // Convertir el canvas a una imagen en base64
            doc.addImage(imgData, 'PNG', 10, 80, 355, 50); 
            const TicketFileName = `DataTicket-${patenteValue}.pdf`;
            doc.save(TicketFileName);
        }
    });       
});