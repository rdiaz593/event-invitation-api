import React from "react";
import QrScanner from "react-qr-scanner";

const QRScannerComponent = ({ onScan }) => {
  const handleError = (err) => {
    console.error("QR Scanner Error:", err);
  };

  const handleScan = (data) => {
    if (data) {
      onScan(data);
    }
  };

  const previewStyle = {
    height: 240,
    width: 320,
  };

  return (
    <QrScanner
      delay={300}
      style={previewStyle}
      onError={handleError}
      onScan={handleScan}
    />
  );
};

export default QRScannerComponent;
