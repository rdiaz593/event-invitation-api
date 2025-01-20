from flasgger import Swagger
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de Swagger
swagger = Swagger(app)

@app.route('/events', methods=['POST'])
def create_events():
    """
    Create a new event
    ---
    tags:
      - Events
    parameters:
      - in: body
        name: body
        description: Event details
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            date:
              type: string
              format: date
            location:
              type: string
    responses:
      201:
        description: Event created successfully
      400:
        description: Bad request
    """

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

def serialize_event(event):
    return {
        "id": event.id,
        "name": event.name,
        "date": event.date.isoformat(),
        "location": event.location
    }

# Función para obtener un evento por ID (se reutiliza en varias rutas)
def get_event_or_404(event_id):
    event = Event.query.get(event_id)
    if not event:
        return None
    return event

# Rutas CRUD
@app.route('/events', methods=['POST'])
def create_event():
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
    return jsonify([serialize_event(event) for event in events])

@app.route('/events/<int:event_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_event(event_id):
    event = get_event_or_404(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    if request.method == 'GET':
        return jsonify(serialize_event(event))

    elif request.method == 'PUT':
        data = request.json
        event.name = data.get('name', event.name)
        event.date = data.get('date', event.date)
        event.location = data.get('location', event.location)
        db.session.commit()
        return jsonify({"message": "Event updated successfully!"})

    elif request.method == 'DELETE':
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)