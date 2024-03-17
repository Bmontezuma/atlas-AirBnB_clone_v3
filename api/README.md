
![Atlas](https://assets-global.website-files.com/6571f4826e9363343bcd2acd/658f59e0ff63da989bc133fc_atlas-share.jpg)


# ***AirBnB clone - RESTful API***
## ***Authors***
- [Ahmad Nawabi](https://github.com/AhmadNawabi)
- [Brandon Montezuma](https://github.com/Bmontezuma)
                          
# ***Concepts for project***
- [AirBnB clone](https://intranet.atlasschool.com/concepts/865)
- [REST API](https://intranet.atlasschool.com/concepts/866)

# ***Resources for project***
- [REST API concept page](https://intranet.atlasschool.com/concepts/866)
- [Learn REST: A RESTful Tutorial](https://www.restapitutorial.com/)
- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Flask cheatsheet](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/301/flask_cheatsheet.pdf)
- [What are Flask Blueprints, exactly?](https://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly)
- [Flask](https://palletsprojects.com/p/flask/)
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
- [Flask tests](https://flask.palletsprojects.com/en/1.1.x/testing/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
- [AirBnB clone - RESTful API](https://www.youtube.com/watch?v=LrQhULlFJdU&feature=youtu.be)

# ***Learning Objectives***
### ***What REST means***

*"REST" stands for Representational State Transfer. It's an architectural style for designing networked applications. When applied to APIs, RESTful principles dictate that APIs should be designed in a way that aligns with the following key concepts:*
- ***`Resource-based:`*** *Resources (such as data objects or services) are identified by unique URIs (Uniform Resource Identifiers). These resources are manipulated using a fixed set of operations (typically HTTP methods like GET, POST, PUT, DELETE) representing standard CRUD (Create, Read, Update, Delete) operations.*
- ***`Stateless:`*** *Each request from a client to the server must contain all the information necessary to understand and process the request. The server should not store any client context between requests. This makes the system more scalable and reliable.*
- ***`Client-Server Architecture:`*** *There is a clear separation between the client and server. Clients are not concerned with the data storage on the server, while servers are not concerned with the user interface or user state on the client.*
- ***`Cacheability:`*** *Responses from the server should be explicitly labeled as cacheable or non-cacheable. This helps improve performance by allowing clients to reuse previously fetched responses.*
- ***`Layered System:`*** *The architecture should support a layered system, allowing intermediaries such as proxies and caches to be inserted between clients and servers. This improves scalability by enabling components to be deployed independently and reused across different parts of the application.*
- ***`Uniform Interface:`*** *The uniform interface constraint simplifies and decouples the architecture, allowing each part to evolve independently. It is the fundamental constraint that drives the decoupling of clients and servers and allows each to evolve independently. It includes four key principles:*
    - ***`Identification of resources:`*** *Resources are identified by URIs.*
    - ***`Manipulation of resources through representations:`*** *Clients manipulate resources through representations provided by the server. These representations can be in various formats such as JSON, XML, or HTML.*
    - ***`Self-descriptive messages:`*** *Each message should include enough information for the recipient to understand how to process the message*.
    - ***`Hypermedia as the engine of application state (HATEOAS):`*** *The server provides hypermedia links in the response, allowing clients to navigate the API dynamically.*

### ***What API means***
### ***API Overview***

*API stands for Application Programming Interface. It refers to a set of rules, protocols, and tools that allow different software applications to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange information.*

### ***Importance of APIs***

*APIs are essential for enabling software integration and interoperability. They allow developers to build upon existing functionality without needing to understand the inner workings of the systems they're interacting with. Instead, developers can interact with APIs through well-defined interfaces, which often involve sending HTTP requests and receiving responses in standard formats like JSON or XML.*

### ***Types of APIs***

- ***Web APIs***: *These APIs are accessed over the internet using standard protocols such as HTTP. They typically provide access to web services, databases, or other online resources.*

- ***Library APIs***: *These APIs are provided by libraries or software development kits (SDKs) and allow developers to interact with the functionality provided by those libraries.*

- ***Operating System APIs***: *These APIs are provided by operating systems and allow applications to interact with system resources such as files, processes, and hardware.*

- ***Hardware APIs***: *These APIs provide access to hardware components such as sensors, cameras, or storage devices.*

## ***Role in Software Development***

*APIs play a crucial role in modern software development, enabling developers to create complex systems by leveraging the functionality provided by other applications, services, or platforms.*

# ***CORS Overview***

*CORS stands for Cross-Origin Resource Sharing. It is a security feature implemented by web browsers that controls access to resources from different origins (domains) on the internet.

When a web page makes a request to a different domain (origin) using XMLHttpRequest or Fetch API, the browser typically restricts the response if the server's response doesn't include the appropriate CORS headers. This restriction is known as the "same-origin policy" and is in place to prevent malicious websites from accessing sensitive data from other websites without permission.

CORS allows servers to specify which origins are allowed to access their resources. This is done by including specific HTTP response headers like ***`Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`***, etc.*

## ***Key CORS Concepts:***

- ***`Origin`***: *The combination of protocol, domain, and port from which a resource is requested. For example, ***`https://example.com`***.*

- ***`Cross-Origin Request`***: *A request for a resource from a different origin than the one from which the current document originated.*

- ***`Preflight Request`***: *A CORS preflight request is an HTTP request that is made by the browser automatically as part of the CORS protocol. It uses the OPTIONS method and includes headers indicating the HTTP methods and headers that will be used in the subsequent actual request.*

- ***`Simple Requests`***: *Certain types of requests (GET, POST, HEAD) with specific content types are considered "simple" and don't trigger a preflight request.*

- ***`Credentials`***: *CORS requests can be made with or without credentials (e.g., cookies, HTTP authentication). Servers can control whether credentials are allowed for cross-origin requests using the ***`Access-Control-Allow-Credentials`*** header.*

*CORS is an important aspect of web security and allows for controlled access to resources across different domains while maintaining security and privacy. Properly configuring CORS policies is crucial for enabling cross-origin communication between web applications when necessary while still protecting against unauthorized access.*

# ***API Overview***

*An API, or Application Programming Interface, is a set of rules, protocols, and tools that allows different software applications to communicate with each other. APIs define how different software components should interact, specifying the methods and data formats that applications can use to request and exchange information.*

*In simpler terms, an API can be thought of as a bridge that allows two different pieces of software to talk to each other. It provides a way for developers to access the functionality of another application or service without needing to understand how that functionality is implemented internally.*

## ***Types of APIs***

### ***`Web APIs`***
*These are APIs exposed over the internet, allowing developers to access web services, databases, or other online resources. Web APIs are commonly used to enable communication between web applications.*

### ***`Library APIs`***
*Libraries and software development kits (SDKs) often provide APIs that allow developers to interact with the functionality provided by those libraries. For example, a graphics library might provide an API for drawing shapes and images.*

### ***`Operating System APIs`***
*Operating systems provide APIs that allow applications to interact with system resources such as files, processes, and hardware. These APIs enable developers to create applications that can run on different operating systems.*

### ***`Hardware APIs`***
*Hardware components such as sensors, cameras, or storage devices often expose APIs that allow software applications to interact with them. These APIs enable developers to create applications that can utilize hardware capabilities.

Overall, APIs play a crucial role in modern software development by enabling interoperability between different systems and facilitating the creation of complex software applications through the reuse of existing functionality.*

### ***`What is a REST API`***
*A REST API (Representational State Transfer Application Programming Interface) is an architectural style for designing networked applications. It's based on a set of principles that define how resources should be accessed and manipulated over the web. RESTful APIs are designed to be scalable, flexible, and easily maintainable.*

# ***Types of APIs***

*Apart from RESTful APIs, there are several other types of APIs commonly used in software development:*

1. ***`SOAP APIs (Simple Object Access Protocol)`***: *SOAP is a protocol for exchanging structured information in the implementation of web services. SOAP APIs use XML as the message format and can be transported over a variety of protocols, including HTTP, SMTP, and more. SOAP APIs are known for their strong typing, formal contracts, and support for security standards like WS-Security.*

2. ***`GraphQL APIs`***: *GraphQL is a query language for APIs and a runtime for executing those queries. Unlike REST APIs, which expose a fixed set of endpoints returning predefined data structures, GraphQL APIs allow clients to request exactly the data they need using a single endpoint. This flexibility makes GraphQL APIs efficient for clients as they can avoid over-fetching or under-fetching data.*

3. ***`RPC APIs (Remote Procedure Call)`***: *RPC is a protocol that allows a program to execute procedures or methods on a remote server as if they were local. RPC APIs enable communication between distributed systems by invoking functions or procedures on remote servers. Examples of RPC frameworks include gRPC, Thrift, and Apache Avro.*

4. ***`WebSocket APIs`***: *WebSocket is a communication protocol that provides full-duplex communication channels over a single TCP connection. WebSocket APIs enable real-time, bidirectional communication between clients and servers, making them suitable for applications requiring low latency and high interactivity, such as chat applications and online gaming.*

5. ***`JSON-RPC and XML-RPC APIs`***: *JSON-RPC and XML-RPC are lightweight remote procedure call protocols using JSON and XML, respectively, as the message format. These APIs allow clients to invoke methods or procedures on remote servers using a simple request-response mechanism.*

6. ***`Webhooks`***: *Webhooks are HTTP callbacks or "reverse APIs" that allow applications to receive real-time notifications or events from external services. Instead of polling for updates, applications can register webhook endpoints to be notified whenever certain events occur, such as a new message in a chat application or a payment confirmation in an e-commerce platform.*

*Each type of API has its own strengths and use cases, and the choice of API depends on factors such as the requirements of the application, the nature of the data being exchanged, and the desired level of flexibility and performance.*

## ***HTTP Method to Retrieve Resource(s)***

*The HTTP method typically used to retrieve resource(s) from a server is the ***`GET`*** method.* 

### ***In the context of RESTful APIs:***

- *When a client makes a request to retrieve data from a server, it uses the ***`GET`*** method.*
- *The server responds to the ***`GET`*** request with the requested resource(s) if they exist, along with an appropriate HTTP status code (usually 200 OK for a successful retrieval).*
- ***`GET`*** *requests are considered safe and idempotent, meaning they should not modify server state and can be repeated without causing any additional side effects.*

### ***For example, in a RESTful API:***

```
GET /api/users
```




