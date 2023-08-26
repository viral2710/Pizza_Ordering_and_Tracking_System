# Pizzeria Pizza Ordering and Tracking System

This project provides an API-driven solution for customers to place pizza orders and track their delivery status. The system allows customers to choose from various options for pizza base, cheese, and toppings. Orders are processed asynchronously with status updates at different stages of preparation.

## Table of Contents

- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Running the Application](#running-the-application)
- [Dockerization](#dockerization)
- [Contributing](#contributing)

## Setup

1. **Database Setup:**
   To set up the development SQLite database hosted in a Docker container, follow these steps:
   - Install Docker and Docker Compose if not already installed.
   - Run `docker-compose up -d` in the project root directory to start the development database container.

2. **Database Schema:**
   The database schema is designed to cater to the specific use case of storing pizza orders and their statuses. The schema includes tables for `Pizza`, `Order`, and `Task`.

   - `Pizza` stores pizza details such as base, cheese, toppings, and associated order.
   - `Order` keeps track of order details and status.
   - `Task` is responsible for asynchronously changing the order status based on time.

3. **Running the Application:**
   Once the database is set up, the API endpoints can be accessed to create orders, add pizzas, and track order status.

## API Endpoints

1. **Create Order Endpoint:**
   - **Endpoint:** `/api/pizza/create_order/`
   - **Method:** POST
   - **Input Data Example:**
     ```json
     {
         "pizza": [
             {
                 "toppings": ["pepperoni", "mushroom", "onion", "olive", "tomato"],
                 "pizza_base": "Thin Crust",
                 "cheese": "Mozzarella"
             },
             {
                 "toppings": ["pepperoni", "mushroom", "onion", "olive", "tomato"],
                 "pizza_base": "Thin Crust",
                 "cheese": "Mozzarella"
             }
         ]
     }
     ```

2. **Get Order Status Endpoint:**
   - **Endpoint:** `/api/pizza/getting_status/`
   - **Method:** POST
   - **Input Data Example:**
     ```json
     {
         "order_number": 36
     }
     ```

3. **Get Choices Endpoint:**
   - **Endpoint:** `/api/pizza/choice/`
   - **Method:** GET
   - **Response Example:**
     ```json
     {
         "toppings": ["pepperoni", "mushroom", "onion", "olive", "tomato", "bell-pepper", "jalapeno"],
         "pizza_base": ["Thin Crust", "Normal", "Cheese Burst"],
         "cheese": ["Mozzarella", "Cheddar", "Parmesan", "Blue Cheese"]
     }
     ```

## Usage

1. Send a POST request to `/api/pizza/create_order/` with the pizza details to place an order. The API will return the order number.
2. Use the order number in a POST request to `/api/pizza/getting_status/` to track the order status.
3. Use the GET request to `/api/pizza/choice/` to get the available choices for pizza base, cheese, and toppings.

## Running the Application

1. Ensure you have Docker and Docker Compose installed.
2. Run `docker-compose up -d` in the project root directory to start the development database.
3. Access the API endpoints using a tool like `curl` or a tool like `Postman`.

## Dockerization

The application and development database can be containerized using Docker Compose. Simply run `docker-compose up -d` to start both the application and the database in separate containers.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue in the repository. Your contributions will be appreciated by the community!
