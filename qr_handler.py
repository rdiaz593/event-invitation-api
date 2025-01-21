import qrcode
import base64
from io import BytesIO

# Datos simulados (puedes conectarlos a una base de datos)
eventos = [
    {"id": 1, "nombre": "Boda", "invitados": 100},
    {"id": 2, "nombre": "Cumpleaños", "invitados": 50}
]

invitados = [
    {"id": 1, "evento_id": 1, "nombre": "Juan", "checkin": False},
    {"id": 2, "evento_id": 1, "nombre": "Ana", "checkin": False},
    {"id": 3, "evento_id": 2, "nombre": "Carlos", "checkin": False}
]

def generate_qr(request):
    evento_id = request.json.get('evento_id')
    invitado_id = request.json.get('invitado_id')

    evento = next((e for e in eventos if e['id'] == evento_id), None)
    invitado = next((i for i in invitados if i['id'] == invitado_id), None)

    if not evento or not invitado:
        return jsonify({"error": "Evento o invitado no encontrado"}), 404

    qr_data = {
        "evento_id": evento_id,
        "invitado_id": invitado_id,
        "num_invitados": evento['invitados']
    }

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return jsonify({"qr_base64": qr_base64})


def verify_qr(request):
    qr_data = request.json.get('qr_data')

    try:
        evento_id = qr_data["evento_id"]
        invitado_id = qr_data["invitado_id"]
    except KeyError:
        return jsonify({"error": "Datos inválidos en el QR"}), 400

    invitado = next((i for i in invitados if i['id'] == invitado_id), None)

    if not invitado or invitado['evento_id'] != evento_id:
        return jsonify({"error": "Invitado no encontrado en el evento"}), 404

    invitado['checkin'] = True

    return jsonify({"mensaje": "Check-in completado", "invitado": invitado})
