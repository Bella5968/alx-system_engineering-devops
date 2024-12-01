# Simple Web Stack

This project involves designing a simple web infrastructure consisting of the following components:

- **1 Server**: Hosts all necessary components for the web application.
- **1 Web Server (Nginx)**: Handles HTTP requests and serves static content.
- **1 Application Server**: Executes the application logic.
- **1 Database (MySQL)**: Stores and manages data for the web application.
- **1 Domain Name (foobar.com)**: Configured with a `www` record pointing to the server IP `8.8.8.8`.

## Explanation of Components

### 1. **Server**
A physical or virtual machine that runs the web infrastructure components.

### 2. **Domain Name**
A human-readable address (e.g., `foobar.com`) that maps to an IP address (`8.8.8.8`). It allows users to access the website easily.

### 3. **DNS Record (A Record)**
The `www` record in `www.foobar.com` is an **A record**, which maps the domain name to the IP address of the server.

### 4. **Web Server (Nginx)**
The web server handles incoming HTTP requests, serves static content, and forwards dynamic content requests to the application server.

### 5. **Application Server**
Processes the application logic and interacts with the database to generate dynamic content.

### 6. **Database (MySQL)**
Stores user data, application data, and other information required by the application.

### 7. **Communication Protocol**
The server communicates with the user's computer using HTTP/HTTPS.

## Issues with This Infrastructure

- **Single Point of Failure (SPOF)**: If the server goes down, the entire application is unavailable.
- **Downtime During Maintenance**: Deploying new code or restarting services causes downtime.
- **Limited Scalability**: The server cannot handle a high volume of traffic as it lacks redundancy and load balancing.

## Diagram

[Distributed Web Infrastructure Diagram](https://drive.google.com/file/d/1vVZn1K_4BnH1XXQ5E7cS29-xV2CR9Ks_/view?usp=drive_link)
