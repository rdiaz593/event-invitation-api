import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/guests">Guests</Link></li>
        <li><Link to="/scan-qr">Scan QR</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
