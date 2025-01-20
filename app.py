from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:adminpassword@db:5432/eventdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de ejemplo
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    # Mostrar las rutas disponibles en el log cuando accedemos a la raíz
    print("Rutas disponibles:", app.url_map)
    return jsonify({"message": "Welcome to the Event Invitation API!"})

@app.route('/init-db')
def init_db():
    db.create_all()
    return "Database initialized!"

# CRUD
@app.route('/events', methods=['POST'])
def create_event():
    print("POST request to /events received")
    data = request.json
    new_event = Event(
        name=data['name'],
        date=data['date'],
        location=data['location']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"message": "Event created successfully!"}), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([
        {
            "id": event.id,
            "name": event.name,
            "date": event.date.isoformat(),
            "location": event.location
        } for event in events
    ])

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    return jsonify({
        "id": event.id,
        "name": event.name,
        "date": event.date.isoformat(),
        "location": event.location
    })

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    data = request.json
    event.name = data.get('name', event.name)
    event.date = data.get('date', event.date)
    event.location = data.get('location', event.location)
    db.session.commit()
    return jsonify({"message": "Event updated successfully!"})

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
