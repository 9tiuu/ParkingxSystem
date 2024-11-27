document.addEventListener('DOMContentLoaded', () => {
    const qrcontainer = document.getElementById('qrcode');
    const ticket_state = document.getElementById('state');

    const qrcode = new QRCode(qrcontainer, {
        width: 200,
        height: 200
    });

    const QR = () => {
        qrcode.makeCode(ticket_state.value);
    };

    QR();
});