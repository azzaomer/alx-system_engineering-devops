# Secure Three Server Web Infrastructure for www.foobar.com

## Overview

This document explains the design of a secure, three-server web infrastructure to host a website accessible via the domain www.foobar.com. The infrastructure will include firewalls, HTTPS encryption, and monitoring to ensure security, performance, and reliability.

## Infrastructure Design

### User Access Flow

1. **User Request**: A user opens their web browser and types in the URL www.foobar.com.
2. **DNS Resolution**: The browser performs a DNS lookup for www.foobar.com, which resolves to the IP address of the load balancer.
3. **HTTPS Connection**: The browser establishes an HTTPS connection with the load balancer using an SSL certificate.
4. **Load Balancer Handling**: The load balancer (HAProxy) receives the request and distributes it to one of the web servers based on the configured algorithm.
5. **Web Server Handling**: Nginx, running on the web server, handles the incoming HTTP request.
6. **Application Server Processing**: Nginx forwards the request to the application server.
7. **Database Query**: If the application needs data, it queries the MySQL database.
8. **Response Generation**: The application server processes the request, possibly interacting with the database, and generates an HTML response.
9. **Response Delivery**: Nginx sends the HTML response back to the user's browser through the load balancer.

### Components

1. **Load Balancer (HAProxy)**: Distributes incoming traffic across multiple servers to ensure no single server is overwhelmed.
2. **Web Server (Nginx)**: Manages incoming HTTP requests, serves static content, and forwards dynamic requests to the application server.
3. **Application Server**: Runs the application codebase, processes business logic, and generates dynamic content.
4. **Application Files**: The codebase for the web application (HTML, CSS, JavaScript, PHP, etc.).
5. **Database (MySQL)**: Stores and manages data required by the application, configured in a Primary-Replica setup.
6. **Firewalls**: Three firewalls, one for each server, to protect against unauthorized access and attacks.
7. **SSL Certificate**: Secures the website by serving traffic over HTTPS.
8. **Monitoring Clients**: Three monitoring clients (e.g., data collectors for Sumologic) to track performance and health metrics.
9. **Servers**: Three physical or virtual machines hosting the load balancer, web server, application server, and database.

## Detailed Explanation

### Additional Elements and Their Roles

1. **Firewalls**: Added to protect each server from unauthorized access and attacks. Firewalls filter incoming and outgoing traffic based on security rules.
2. **SSL Certificate**: Added to serve the website over HTTPS, ensuring that data transmitted between the user's browser and the server is encrypted and secure.
3. **Monitoring Clients**: Added to collect data on server performance, health, and usage. This allows for real-time monitoring and alerts on potential issues.

### Purpose of Each Element

- **Firewalls**: Prevent unauthorized access and protect against attacks by filtering traffic based on predefined security rules.
- **HTTPS Traffic**: Ensures secure communication between the user's browser and the server by encrypting the data transmitted over the network.
- **Monitoring**: Tracks performance, health, and usage metrics to detect and address issues proactively. Monitoring tools collect data such as CPU usage, memory usage, network traffic, and error logs.

### Monitoring Details

- **Data Collection**: Monitoring clients installed on each server collect data and send it to a monitoring service (e.g., Sumologic) for analysis and visualization.
- **QPS Monitoring**: To monitor queries per second (QPS) on the web server, configure the monitoring client to track and report the number of HTTP requests processed by Nginx.

## Infrastructure Issues

### SSL Termination at the Load Balancer

- **Issue**: Terminating SSL at the load balancer means that traffic between the load balancer and the web servers is not encrypted. This can expose sensitive data to potential interception within the internal network.
- **Solution**: Implement end-to-end encryption by using SSL certificates on both the load balancer and the web servers.

### Single Write-Capable MySQL Server

- **Issue**: Having only one MySQL server capable of accepting writes creates a single point of failure. If the primary MySQL server fails, write operations cannot be performed, leading to potential data loss and downtime.
- **Solution**: Implement a multi-primary setup or use database clustering to distribute write operations across multiple servers.

### Homogeneous Server Components

- **Issue**: Having servers with all the same components (database, web server, and application server) can lead to resource contention and complex management. It can also increase the risk of widespread failure if one component causes issues.
- **Solution**: Separate concerns by dedicating servers to specific roles (e.g., dedicated web servers, application servers, and database servers) to optimize resource usage and simplify management.

---

By understanding this secure infrastructure, we can appreciate the enhanced security, performance, and reliability compared to a basic setup, while also recognizing the need for further improvements in SSL management, database redundancy, and component separation.

