## 0x0F-load_balancer
# Task 0:
# Web Server Configuration with Custom Header

## Task 0: Double the Number of Web Servers

### Objective

In this task, you will configure `web-02` to be identical to `web-01`. The goal is to automate the setup of a new web server using a Bash script. We will also place the web servers behind a load balancer and add a custom Nginx response header to track which server is handling HTTP requests.

### Requirements

1. **Configure Nginx on both `web-01` and `web-02` so that its HTTP response contains a custom header.**
2. **The custom HTTP header must be named `X-Served-By`.**
3. **The value of the `X-Served-By` header must be the hostname of the server running Nginx.**
4. **Write a script `0-custom_http_response_header` to automate the setup of a new Ubuntu machine.**

### Example

To verify the setup, you can use `curl` to send a request to each web server and check for the custom header in the response:

```sh
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01

sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02

sylvain@ubuntu$

