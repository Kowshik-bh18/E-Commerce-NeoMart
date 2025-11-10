# 🏗️ E-Commerce NeoMart — System Architecture

## 🛍️ Overview

**E-Commerce NeoMart** is a full-stack e-commerce platform built with **React (frontend)**, **Django REST Framework (backend)**, and **SQLite (database)**.  
It delivers a seamless online shopping experience with features like authentication, cart management, order tracking, product reviews, and an **AI-powered chatbot recommender system**.

---

## 🧩 High-Level Architecture

```plaintext
          ┌──────────────────────────┐
          │        Frontend          │
          │      (React.js)          │
          │──────────────────────────│
          │ - User Interface (UI)    │
          │ - Product pages          │
          │ - Cart & Checkout views  │
          │ - Chatbot Interface      │
          │ - API Calls via Axios    │
          └────────────┬─────────────┘
                       │
     (REST API Requests│Responses via JSON)
                       │
          ┌────────────▼─────────────┐
          │       Backend API        │
          │   (Django + DRF)         │
          │──────────────────────────│
          │ - User Authentication    │
          │ - Product Management     │
          │ - Cart & Orders APIs     │
          │ - Payment & Invoice Flow │
          │ - AI Chatbot Endpoint    │
          │ - Admin Management       │
          └────────────┬─────────────┘
                       │
            (ORM Queries│Model Objects)
                       │
          ┌────────────▼─────────────┐
          │        Database          │
          │       (SQLite)           │
          │──────────────────────────│
          │ - Users Table            │
          │ - Products Table         │
          │ - Orders & Cart Tables   │
          │ - Reviews Table          │
          │ - Chatbot Cache Table    │
          └────────────┬─────────────┘
                       │
                       │
          ┌────────────▼─────────────┐
          │     AI Integration       │
          │ (Chatbot Recommender)    │
          │──────────────────────────│
          │ - Uses Product Metadata  │
          │ - Recommends via Django  │
          │ - Responds to Queries    │
          └──────────────────────────┘
