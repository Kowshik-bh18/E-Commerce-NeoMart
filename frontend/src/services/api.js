import axios from "axios";

const API_URL = "http://localhost:8000/api";
const AUTH_URL = "http://localhost:8000/auth";

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `JWT ${token}`;
  }
  return config;
});

export const login = async (username, password) => {
  const response = await axios.post(`${AUTH_URL}/jwt/create/`, {
    username,
    password,
  });
  localStorage.setItem("token", response.data.access);
  return response.data;
};

export const register = async (username, email, password) => {
  const response = await axios.post(`${AUTH_URL}/users/`, {
    username,
    email,
    password,
  });
  return response.data;
};

export const getProducts = async (category = null, search = "") => {
  const params = new URLSearchParams();
  if (category) params.append("category", category);
  if (search) params.append("search", search);
  const response = await api.get(`/products/?${params.toString()}`);
  return response.data;
};

export const getCategories = async () => {
  const response = await api.get("/categories/");
  return response.data;
};

export const addToCart = async (productId, quantity) => {
  const response = await api.post(`/products/${productId}/add_to_cart/`, {
    quantity,
  });
  return response.data;
};

export const getCart = async () => {
  const response = await api.get("/cart/");
  return response.data;
};

export const checkout = async (shippingAddress) => {
  const response = await api.post("/cart/checkout/", {
    shipping_address: shippingAddress,
  });
  return response.data;
};

export const getOrders = async () => {
  const response = await api.get("/orders/");
  return response.data;
};

export const downloadInvoice = async (orderId) => {
  const response = await api.get(`/orders/${orderId}/download_invoice/`, {
    responseType: "blob",
  });
  return response.data;
};

export const getRecommendations = async () => {
  const response = await api.get("/products/recommendations/");
  return response.data;
};
