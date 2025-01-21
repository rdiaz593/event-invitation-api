eventos = [
    {"id": 1, "nombre": "Boda", "invitados": 100},
    {"id": 2, "nombre": "Cumpleaños", "invitados": 50}
]

invitados = [
    {"id": 1, "evento_id": 1, "nombre": "Juan", "checkin": False},
    {"id": 2, "evento_id": 1, "nombre": "Ana", "checkin": False},
    {"id": 3, "evento_id": 2, "nombre": "Carlos", "checkin": False}
]

def attendance_report(request):
    evento_id = request.args.get('evento_id', type=int)

    evento = next((e for e in eventos if e['id'] == evento_id), None)
    if not evento:
        return jsonify({"error": "Evento no encontrado"}), 404

    invitados_evento = [i for i in invitados if i['evento_id'] == evento_id]

    invitados_confirmados = len(invitados_evento)
    invitados_checkin = len([i for i in invitados_evento if i['checkin']])

    return jsonify({
        "evento": evento['nombre'],
        "total_invitados": invitados_confirmados,
        "check_in_completado": invitados_checkin
    })
