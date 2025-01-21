import React, { useEffect, useState } from "react";
import { fetchGuests, addGuest } from "../services/api";
import GuestForm from "../components/GuestForm";
import GuestList from "../components/GuestList";

const Guests = () => {
  const [guests, setGuests] = useState([]);

  useEffect(() => {
    const loadGuests = async () => {
      const data = await fetchGuests();
      setGuests(data);
    };
    loadGuests();
  }, []);

  const handleAddGuest = async (guest) => {
    const newGuest = await addGuest(guest);
    setGuests((prev) => [...prev, newGuest]);
  };

  return (
    <div>
      <h1>Manage Guests</h1>
      <GuestForm onAddGuest={handleAddGuest} />
      <GuestList guests={guests} />
    </div>
  );
};

export default Guests;
