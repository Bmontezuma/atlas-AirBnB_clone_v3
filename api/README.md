
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

![Image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240315%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240315T230551Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5c5ccfb58e7341d6f52aba5f5bd0f0926c8a8af4f00039ea8708cb86125203c5)

## ***Web Static***

In this phase, we focus on creating the static components of the web application. Here's what we'll do:

- ***Learn HTML/CSS:*** *We'll delve into HTML and CSS to understand the basics of web page structuring and styling*.
- ***Create the HTML of your application:*** *We'll develop the HTML structure of our application, laying the foundation for the user interface*.
- ***Create a template for each object:*** *Each object within the application will have its own template, ensuring consistency and ease of development*.

By completing these steps, we'll establish the static elements of our application, setting the stage for dynamic functionality in subsequent phases. Let's dive in and bring our application to life on the web!

![image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/87c01524ada6080f40fc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240315%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240315T230551Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b304a7e030fdbb4dd30387d37a9d1c31ccb49d489af332e1b32b949a2540a312)

## ***MySQL Storage***

To enhance the storage capabilities of our application, we'll replace the file-based storage system with a MySQL database. Here's how we'll do it:

- ***Replace File Storage with Database Storage:*** *Swap out the file-based storage system with MySQL, allowing for more robust data management and scalability*.
- ***Map Models to Database Tables:*** *Each model in our application will be mapped to a corresponding table in the MySQL database, ensuring seamless integration between our application and the database*.
- ***Utilize an O.R.M. (Object-Relational Mapping):*** *Employ an O.R.M. to streamline the interaction between our application's objects and the database, simplifying data access and manipulation*.

![image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/5284383714459fa68841.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240315%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240315T230551Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=123639d082e5052fcdce7c3a35fdd2d0cc86d89e8c8212834476ee1cdc296525)
