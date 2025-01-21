import React from "react";

const GuestList = ({ guests }) => {
  return (
    <div>
      <h3>Guest List</h3>
      <ul>
        {guests.length === 0 ? (
          <p>No guests yet</p>
        ) : (
          guests.map((guest, index) => (
            <li key={index}>{guest}</li>
          ))
        )}
      </ul>
    </div>
  );
};

export default GuestList;
