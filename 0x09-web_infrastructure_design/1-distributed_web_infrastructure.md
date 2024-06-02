# Three Server Web Infrastructure for www.foobar.com

## Overview

This document explains the design of a three-server web infrastructure to host a website accessible via the domain www.foobar.com. The infrastructure will include a load balancer, a web server, an application server, and a database configured in a Primary-Replica setup.

## Infrastructure Design

### User Access Flow

1. **User Request**: A user opens their web browser and types in the URL www.foobar.com.
2. **DNS Resolution**: The browser performs a DNS lookup for www.foobar.com, which resolves to the IP address of the load balancer.
3. **Load Balancer Handling**: The load balancer (HAProxy) receives the request and distributes it to one of the web servers based on the configured algorithm.
4. **Web Server Handling**: Nginx, running on the web server, handles the incoming HTTP request.
5. **Application Server Processing**: Nginx forwards the request to the application server.
6. **Database Query**: If the application needs data, it queries the MySQL database.
7. **Response Generation**: The application server processes the request, possibly interacting with the database, and generates an HTML response.
8. **Response Delivery**: Nginx sends the HTML response back to the user's browser through the load balancer.

### Components

1. **Load Balancer (HAProxy)**: Distributes incoming traffic across multiple servers to ensure no single server is overwhelmed.
2. **Web Server (Nginx)**: Manages incoming HTTP requests, serves static content, and forwards dynamic requests to the application server.
3. **Application Server**: Runs the application codebase, processes business logic, and generates dynamic content.
4. **Application Files**: The codebase for the web application (HTML, CSS, JavaScript, PHP, etc.).
5. **Database (MySQL)**: Stores and manages data required by the application, configured in a Primary-Replica setup.
6. **Servers**: Three physical or virtual machines hosting the load balancer, web server, application server, and database.

## Detailed Explanation

### Additional Elements and Their Roles

1. **Load Balancer (HAProxy)**: Added to distribute traffic across multiple servers, preventing any single server from becoming a bottleneck. It improves redundancy and scalability.
2. **Web Server (Nginx)**: Separates the web server from the application server to enhance performance and manage static and dynamic content more efficiently.
3. **Database Primary-Replica Setup**: Improves data redundancy and read performance by distributing database read operations across multiple servers.

### Load Balancer Configuration

- **Distribution Algorithm**: The load balancer uses the Round Robin algorithm, which distributes incoming requests sequentially to each server in the pool. This ensures an even distribution of traffic.
- **Active-Active Setup**: Both web servers are active, handling requests simultaneously. In contrast, an Active-Passive setup would have one active server and one standby server, which takes over only if the active server fails.

### Database Primary-Replica Cluster

- **Primary Node**: Handles all write operations and propagates changes to the Replica node.
- **Replica Node**: Handles read operations, improving read performance and reducing the load on the Primary node. It also provides redundancy for data.

### Infrastructure Issues

#### Single Points of Failure (SPOF)

- The load balancer is a single point of failure. If it fails, the entire system becomes unavailable.

#### Security Issues

- **No Firewall**: The infrastructure is vulnerable to unauthorized access and attacks.
- **No HTTPS**: Data transmitted between the user's browser and the server is not encrypted, making it susceptible to interception and tampering.

#### Monitoring

- **No Monitoring**: The lack of monitoring tools means that issues such as server overloads, downtime, and performance bottlenecks may go undetected until they cause significant problems.

---

By understanding this enhanced infrastructure, we can appreciate the improved performance, redundancy, and scalability compared to a single-server setup, while also recognizing the need for further improvements in security and monitoring.

