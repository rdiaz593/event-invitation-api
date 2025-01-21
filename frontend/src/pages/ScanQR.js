import React, { useState } from "react";
import QRScannerComponent from "../components/QRScanner";

const ScanQR = () => {
  const [scannedData, setScannedData] = useState(null);

  const handleScan = (data) => {
    setScannedData(data.text); // Guardamos el texto escaneado
  };

  return (
    <div>
      <h2>Scan QR Code</h2>
      <QRScannerComponent onScan={handleScan} />
      {scannedData && (
        <div>
          <p>Scanned Data: {scannedData}</p>
        </div>
      )}
    </div>
  );
};

export default ScanQR;
