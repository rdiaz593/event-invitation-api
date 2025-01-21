import React, { useState } from 'react';

function GuestForm({ setGuests }) {
  const [guestName, setGuestName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Aquí agregaríamos la lógica para enviar el nuevo invitado
    setGuests((prevGuests) => [...prevGuests, { name: guestName }]);
    setGuestName('');
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <div className="mb-3">
        <label htmlFor="guestName" className="form-label">Guest Name</label>
        <input
          type="text"
          id="guestName"
          className="form-control"
          value={guestName}
          onChange={(e) => setGuestName(e.target.value)}
          required
        />
      </div>
      <button type="submit" className="btn btn-primary">Add Guest</button>
    </form>
  );
}

export default GuestForm;
