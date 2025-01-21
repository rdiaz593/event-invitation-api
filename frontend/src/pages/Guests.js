import React, { useState, useEffect } from 'react';
import GuestForm from '../components/GuestForm';
import GuestList from '../components/GuestList';

function Guests() {
  const [guests, setGuests] = useState([]);

  useEffect(() => {
  }, []);

  return (
    <div className="container mt-5">
      <h2>Manage Guests</h2>
      <GuestForm setGuests={setGuests} />
      <GuestList guests={guests} />
    </div>
  );
}

export default Guests;
