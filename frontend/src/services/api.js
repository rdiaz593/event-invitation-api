const API_URL = "http://localhost:5000";

export const fetchGuests = async () => {
  const response = await fetch(`${API_URL}/guests`);
  return response.json();
};

export const addGuest = async (guest) => {
  const response = await fetch(`${API_URL}/guests`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(guest),
  });
  return response.json();
};

export const validateQRCode = async (qrCode) => {
  const response = await fetch(`${API_URL}/validate-qr`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ qrCode }),
  });
  return response.json();
};
