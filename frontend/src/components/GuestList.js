import React from 'react';

function GuestList({ guests }) {
  return (
    <div>
      <h3>Guest List</h3>
      <table className="table table-bordered">
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {guests.map((guest, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{guest.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default GuestList;
