# One Server Web Infrastructure for www.foobar.com

## Overview

This document explains the design of a simple web infrastructure using a single server to host a website accessible via the domain www.foobar.com. The infrastructure will be powered by a LAMP stack (Linux, Apache, MySQL, PHP) but with a slight modification where Nginx is used as the web server instead of Apache.

## Infrastructure Design

### User Access Flow

1. **User Request**: A user opens their web browser and types in the URL www.foobar.com.
2. **DNS Resolution**: The browser performs a DNS lookup for www.foobar.com, which resolves to the IP address 8.8.8.8.
3. **Server Connection**: The browser connects to the server at IP 8.8.8.8.
4. **Web Server Handling**: Nginx, running on the server, handles the incoming HTTP request.
5. **Application Server Processing**: Nginx forwards the request to the application server.
6. **Database Query**: If the application needs data, it queries the MySQL database.
7. **Response Generation**: The application server processes the request, possibly interacting with the database, and generates an HTML response.
8. **Response Delivery**: Nginx sends the HTML response back to the user's browser.

### Components

1. **Server**: A physical or virtual machine that hosts all components of the infrastructure.
2. **Web Server (Nginx)**: Manages incoming HTTP requests, serves static content, and forwards dynamic requests to the application server.
3. **Application Server**: Runs the application codebase, processes business logic, and generates dynamic content.
4. **Application Files**: The codebase for the web application (HTML, CSS, JavaScript, PHP, etc.).
5. **Database (MySQL)**: Stores and manages data required by the application.
6. **Domain Name**: www.foobar.com, which users enter to access the website.
7. **DNS Record**: A 'www' A record pointing to the server IP address 8.8.8.8.

## Detailed Explanation

### Server

A server is a powerful computer designed to process requests and deliver data to other computers over a local network or the internet. In this setup, the server hosts the web server (Nginx), application server, application files, and database.

### Domain Name

The domain name (foobar.com) is a human-readable address used to access the website. It is easier to remember than an IP address. The 'www' subdomain is specifically configured to point to our server's IP address.

### DNS Record

The 'www' in www.foobar.com is a DNS record type called an A record. It maps the domain name to an IP address (8.8.8.8), allowing users to reach the server hosting the website.

### Web Server (Nginx)

The web server handles HTTP requests from users. It serves static files directly (e.g., images, CSS files) and forwards dynamic requests to the application server for further processing.

### Application Server

The application server runs the web application code. It handles business logic, processes requests, and interacts with the database to retrieve or store data as needed.

### Database (MySQL)

The database is responsible for storing and managing data. MySQL is a relational database management system that the application server queries to perform CRUD (Create, Read, Update, Delete) operations on data.

### Communication

The server communicates with the user's computer via the HTTP/HTTPS protocols, using TCP/IP as the underlying transport protocol. The Nginx web server listens for incoming requests on port 80 (HTTP) or port 443 (HTTPS) and responds accordingly.

## Infrastructure Issues

### Single Point of Failure (SPOF)

Since all components are hosted on a single server, if the server fails, the entire website becomes unavailable. This makes the infrastructure a single point of failure.

### Downtime During Maintenance

When maintenance is needed, such as deploying new code or restarting the web server, the entire website will experience downtime, making it inaccessible to users during that period.

### Scalability

This infrastructure cannot handle a high volume of incoming traffic efficiently. As the load increases, the server may become overwhelmed, leading to slower response times or complete failure. It lacks the ability to scale horizontally by adding more servers to distribute the load.

---

By understanding this basic infrastructure, we can appreciate the simplicity and limitations of a single-server setup and recognize the need for more complex architectures as the website grows in traffic and functionality.
