import React, { useState } from "react";
import QRScannerComponent from "../components/QRScanner";

const ScanQR = () => {
  const [scanning, setScanning] = useState(false);
  const [scannedData, setScannedData] = useState(null);

  const handleScanButtonClick = () => {
    setScanning(true); // Cambia el estado a 'true' para mostrar la cámara
  };

  const handleScan = (data) => {
    setScannedData(data.text); // Guarda el texto escaneado
    setScanning(false); // Detiene el escaneo cuando el QR ha sido escaneado
  };

  return (
    <div className="container mt-5">
      <h2>Scan QR Code</h2>
      <p>Use the camera to scan your QR code.</p>

      {/* Botón de escaneo que solo aparece si no estamos escaneando */}
      <button
        onClick={handleScanButtonClick}
        className="btn btn-success"
        disabled={scanning} // Deshabilita el botón mientras se está escaneando
      >
        {scanning ? "Scanning..." : "Start Scanning"}
      </button>

      {/* Muestra el componente QRScannerComponent solo si estamos escaneando */}
      {scanning && (
        <div className="mt-4">
          <QRScannerComponent onScan={handleScan} />
        </div>
      )}

      {/* Muestra el dato escaneado si existe */}
      {scannedData && (
        <div className="mt-4">
          <p>Scanned Data: {scannedData}</p>
        </div>
      )}
    </div>
  );
};

export default ScanQR;
