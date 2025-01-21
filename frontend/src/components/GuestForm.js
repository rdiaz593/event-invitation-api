import React, { useState } from "react";

const GuestForm = ({ addGuest }) => {
  const [name, setName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name) {
      addGuest(name);
      setName(""); // Reset form
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">Guest Name</label>
      <input
        type="text"
        id="name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter guest's name"
      />
      <button type="submit">Add Guest</button>
    </form>
  );
};

export default GuestForm;
