import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="container text-center mt-5">
      <h1>Welcome to Event Invitations</h1>
      <p>Create and manage your event invitations easily.</p>
      <div className="mt-4">
        <Link to="/guests" className="btn btn-primary m-2">Manage Guests</Link>
        <Link to="/scan-qr" className="btn btn-secondary m-2">Scan QR Code</Link>
      </div>
    </div>
  );
}

export default Home;
