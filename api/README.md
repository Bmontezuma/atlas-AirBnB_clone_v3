
![Atlas](https://assets-global.website-files.com/6571f4826e9363343bcd2acd/658f59e0ff63da989bc133fc_atlas-share.jpg)


# ***AirBnB clone - RESTful API***
## ***Authors***
- [Ahmad Nawabi](https://github.com/AhmadNawabi)
- [Brandon Montezuma](https://github.com/Bmontezuma)

*This project aims to deploy a simplified version of the Airbnb website on your server. While we won't be implementing all features, we'll cover essential concepts of the higher-level programming track.*

***The project comprises:***

- ***Command Interpreter***: *A tool to manipulate data without a visual interface, akin to a Shell, facilitating development and debugging*.
- ***Website (Front-end)***: *Displaying the final product to users, combining static and dynamic elements*.
- ***Database or Files***: *Storing data in the form of objects*.
- ***API***: *Providing a communication interface between the front-end and data, allowing retrieval, creation, deletion, and updating of information*.

## ***Console***

The console serves as the command interpreter for managing objects within the data model. With it, you can:

- *Create your data model*.
- *Manage (create, update, destroy, etc.) objects via a console/command interpreter*.
- *Store and persist objects to a file (JSON file)*.

The initial focus lies in manipulating a robust storage system. This storage engine abstracts the interaction between "My object" and "How they are stored and persisted". Essentially, this abstraction ensures that regardless of whether you're working in the console code (the command interpreter), front-end, or RestAPI (which will be built later), you won't need to concern yourself with the specifics of how your objects are stored.

This abstraction facilitates easy switching of storage types without the need for extensive updates across your codebase. The console serves as a valuable tool for validating this storage engine.

![Image](https://i.pinimg.com/564x/21/32/a9/2132a9b1cd5a7ead275abe0ad82d081f.jpg)

## ***Web Static***

In this phase, we focus on creating the static components of the web application. Here's what we'll do:

- ***Learn HTML/CSS:*** *We'll delve into HTML and CSS to understand the basics of web page structuring and styling*.
- ***Create the HTML of your application:*** *We'll develop the HTML structure of our application, laying the foundation for the user interface*.
- ***Create a template for each object:*** *Each object within the application will have its own template, ensuring consistency and ease of development*.

By completing these steps, we'll establish the static elements of our application, setting the stage for dynamic functionality in subsequent phases. Let's dive in and bring our application to life on the web!

![image](https://i.pinimg.com/564x/21/32/a9/2132a9b1cd5a7ead275abe0ad82d081f.jpg)

## ***MySQL Storage***

To enhance the storage capabilities of our application, we'll replace the file-based storage system with a MySQL database. Here's how we'll do it:

- ***Replace File Storage with Database Storage:*** *Swap out the file-based storage system with MySQL, allowing for more robust data management and scalability*.
- ***Map Models to Database Tables:*** *Each model in our application will be mapped to a corresponding table in the MySQL database, ensuring seamless integration between our application and the database*.
- ***Utilize an O.R.M. (Object-Relational Mapping):*** *Employ an O.R.M. to streamline the interaction between our application's objects and the database, simplifying data access and manipulation*.

![image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/5284383714459fa68841.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240316%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240316T130718Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a82cb9c265b07988c480829649b2c0c128a6ab7dc206f2a25d976aa11c18b6d0)

## ***Web Framework - Templating***

In this phase, we'll introduce a web framework and templating to make our application dynamic. Here's what we'll do:

- ***Create Your First Web Server in Python:*** *Set up a basic web server using a Python web framework*.
- ***Make Your Static HTML File Dynamic:*** *Utilize objects stored in a file or database to dynamically populate content in our HTML files*.

![image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240316%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240316T130718Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=94a1c798fa9f5f33e12910d2d24944554f6cd572c7f3937cb8c892cd4a0b391e)

## ***RESTful API***

In this phase, we'll expose all objects stored in our application via a JSON web interface and manipulate these objects through a RESTful API. Here's what we'll do:

- ***Expose Objects via JSON Web Interface:*** *Create endpoints to retrieve all objects stored in our application in JSON format*.
- ***Manipulate Objects via RESTful API:*** *Implement endpoints to manipulate (create, read, update, delete) objects through RESTful API calls*.

![image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/06fccc41df40ab8f9d49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240316%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240316T130718Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=85afce913220899cbf33893f422dc3003a40ac56d3d7b76c934350a43b1fb4e3)


