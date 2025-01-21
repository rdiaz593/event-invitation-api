import React, { useState } from "react";
import QRScanner from "react-qr-scanner";

const QRScannerComponent = ({ onScan }) => {
  const [isScanning, setIsScanning] = useState(false);

  const handleScan = (data) => {
    if (data) {
      onScan(data);
      setIsScanning(false);
    }
  };

  const handleError = (err) => {
    console.error(err);
  };

  return (
    <div>
      {isScanning ? (
        <QRScanner
          delay={300}
          onScan={handleScan}
          onError={handleError}
        />
      ) : (
        <button onClick={() => setIsScanning(true)}>Start Scanning</button>
      )}
    </div>
  );
};

export default QRScannerComponent;
