
![Atlas](https://assets-global.website-files.com/6571f4826e9363343bcd2acd/658f59e0ff63da989bc133fc_atlas-share.jpg)


# ***AirBnB clone - RESTful API***
## ***Authors***
- [Ahmad Nawabi](https://github.com/AhmadNawabi)
- [Brandon Montezuma](https://github.com/Bmontezuma)
                          
# ***Task 0: Restart from scratch!***

## ***Introduction***

*This is the third version of the AirBnB clone project for Holberton School. In this version, we have made significant improvements and updates to the codebase to enhance its functionality and performance.*

***No no no!*** *We are already too far in the project to restart everything.*

*But once again, let’s work on a new codebase.*

*For this project you will fork this [codebase](https://github.com/alexaorrico/AirBnB_clone_v2):*

- *Update the repository name to* ***`atlas-AirBnB_clone_v3`***
- *Update the* ***`README.md`***:
  - *Add yourself as an author of the project*
  - *Add new information about your new contribution*
  - *Make it better!*

## ***Changes and Contributions***

- *Updated repository name to* ***`atlas-AirBnB_clone_v3`***.
- *Added myself and partner as an author of the project.*
- *Implemented new features and improvements to enhance the overall functionality.*
- *Refactored existing code for better readability and maintainability.*

## ***Repository Information***

- *GitHub repository*: [atlas-AirBnB_clone_v3](https://github.com/Bmontezuma/atlas-AirBnB_clone_v3)

# ***Task 1***: *Never fail!*

## ***Introduction***

*In software development, testing plays a crucial role in ensuring the reliability and stability of the codebase. The unittest module, which we've been utilizing since the beginning, holds significant importance. Unittests are vital as they help verify that new features are added without introducing regressions or breaking existing functionality. At Holberton, we maintain an extensive suite of tests, ensuring that all tests pass reliably.*

*Since the beginning, we've been using the ***`unittest`*** module extensively. But do you know why ***`unittests`*** are so important? Because when you add a new feature, refactor a piece of code, etc., you want to be sure you didn't break anything.*

*At Holberton, we have a lot of tests, and they all pass! Just for the Intranet itself, there are:*

- ***`5,213`*** *assertions (as of 08/20/2018)*
- ***`13,061`*** assertions (as of 01/25/2021)

*The following requirements must be met for your project:*

- *All current tests must pass (don’t delete them…)*.
- *Add new tests as much as you can (tests are mandatory for some tasks)*.

# ***Task 2: Code review***

## ***Introduction***

*Like “tests”, code review is the base of all software development. All companies are using this “feature” to improve the codebase, but also the group dynamic. For example, at Zenly, the iOS team does a code review every day at 5 pm with the entire team*.

### ***What is a code review?***

*Code review helps developers learn the codebase, as well as help them learn new technologies and techniques that grow their skill sets. When a developer is finished working on an issue, another developer looks over the code and considers questions like:*

- *Are there any obvious logic errors in the code?*
- *Looking at the requirements, are all cases fully implemented?*
- *Are the new automated tests sufficient for the new code? Do existing automated tests need to be rewritten to account for changes in the code?*
- *Does the new code conform to existing style guidelines?*

### ***References***

- *[Why code reviews matter (and actually save time!)](https://blog.codacy.com/why-code-reviews-matter-and-actually-save-time/)*
- *[Code Review Best Practices](https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html)*
- *[GitHub - code review tool](https://github.com/features/code-review/)*
- *[Code Review on GitHub](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews)*
- *[Effective pull requests and other good practices for teams using GitHub](https://codeburst.io/effective-pull-requests-and-other-good-practices-for-teams-using-github-e1f8341c17e0)*
- *[Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)*

*For this project, you will need to review a peer’s pull request on the branch ***`storage_get_count`*** (which will be made for question 3), and then accept the pull request, with your review in the comments*.

### ***What we expect:***
***`code_review.txt`***, containing the GitHub username of the student you reviewed (e.g., If you did the review of JohnDoe, `code_review.txt` must contain JohnDoe)*.
- *The code review must be done on GitHub, in the comments for the pull request:*
  - *The pull request must be created from the branch ***`storage_get_count`*** by a peer*.
  - *Only the reviewer can approve the pull request.*
  - *Don’t delete the branch ***`storage_get_count`*** after approval.*
- *The comments must contain at least one useful comment:*
  - *Questions about the piece of code, if it’s difficult to understand*
  - *Style issues*
  - *Error handling*
  - *Duplicate code*
  - *Potential bugs*
  - *Potential efficiency issues*
  - *Typographical errors*

*We are all human, we all make mistakes, typos, etc… another developer will always find something in your code*.

# ***Task 3: Improve storage***

## ***Introduction***

*In this task, we aim to enhance the functionality of the storage engine by adding two new methods to both DBStorage and FileStorage classes. All changes should be implemented in the branch* ***`storage_get_count`***.

### ***New Methods to be Added***:

1. ***A method to retrieve one object:***
   - *Prototype:* ***`def get(self, cls, id):`***
   - ***`cls`***: *class*
   - ***`id`***: *string representing the object ID
   - Returns the object based on the class and its ID, or None if not found*

2. *A method to count the number of objects in storage*:
   - *Prototype:* ***`def count(self, cls=None):`***
   - ***`cls`***: *class (optional)*
   - *Returns the number of objects in storage matching the given class. If no class is passed, returns the count of all objects in storage*.

*Don’t forget to add new tests for these 2 methods on each storage engine*.

### ***Testing***

```python
#!/usr/bin/python3
Test .get() and .count() methods

from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))

All objects: 1013
State objects: 27
First state: [State] (f8d21261-3e79-4f5c-829a-99d7452cd73c) {'name': 'Colorado', 'updated_at': datetime.datetime(2017, 3, 25, 2, 17, 6), 'created_at': datetime.datetime(2017, 3, 25, 2, 17, 6), '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fc0103a8e80>, 'id': 'f8d21261-3e79-4f5c-829a-99d7452cd73c'}
```

# ***Task 4:*** *Status of your API*

## ***Introduction***

*It’s time to start your API! Your first endpoint (route) will be to return the status of your API*.

### ***Instructions:***

1. *Create a folder* ***`api`*** *at the root of the project with an empty file* ***`__init__.py`***.
2. *Create a folder* ***`v1`*** *inside* ***`api`***:
   - *Create an empty file* ***`__init__.py`***.
   - *Create a file* ***`app.py`***:
     - *Create a variable* ***`app`***, *instance of Flask.*
     - *Import* ***`storage`*** *from* ***`models`***.
     - *Import* ***`app_views`*** *from* ***`api.v1.views`***.
     - *Register the blueprint* ***`app_views`*** *to your Flask instance* ***`app`***.
     - *Declare a method to handle* ***`@app.teardown_appcontext`*** *that calls* ***`storage.close()`***.
     - *Inside* ***`if __name__ == "__main__":`***, *run your Flask server (variable* ***`app`***) with:*
       - ***`host = environment variable HBNB_API_HOST` or `0.0.0.0`*** *if not defined*.
       - ***`port = environment variable HBNB_API_PORT`*** *or* ***`5000`*** *if not defined*.
       - ***`threaded=True`***.
3. *Create a folder* ***`views`*** *inside* ***`v1`***:
   - *Create a file* ***`__init__.py`***:
     - *Import* ***`Blueprint`*** *from Flask*.
     - *Create a variable* ***`app_views`*** *which is an instance of* ***`Blueprint`*** *(url prefix must be ***`/api/v1`***)*.
     - *Below the above line for* ***`app_views`***, *add a wildcard import of everything in the package* ***`api.v1.views.index`***.
   - *Create a file* ***`index.py`***:
     - *Import* ***`app_views`*** *from* ***`api.v1.views`***.
     - *Create a route* ***`/status`*** *on the object* ***`app_views`*** *that returns a JSON:* ***`{"status": "OK"}`***.

### ***Expected Output***

```
$ curl -X GET http://0.0.0.0:5000/api/v1/status
{
  "status": "OK"
}
$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
< Content-Type: application/json

No need to have a pretty rendered output, it’s a JSON, only the structure is important.

# File: api/__init__.py (empty file)

# File: api/v1/__init__.py (empty file)

# File: api/v1/views/__init__.py

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *

# File: api/v1/views/index.py

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

# File: api/v1/app.py

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage"""
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)

# File: api/v1/views/__init__.py

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *

# File: api/v1/views/index.py

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

# File: api/v1/app.py

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage"""
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
```
# ***Task 5:*** *Some stats?*

## ***Introduction***

*Create an endpoint that retrieves the number of each object by type*.

### ***Instructions:***

1. *In* ***`api/v1/views/index.py`***:
   - *Route:* ***`/api/v1/stats`***
   - *You must use the newly added* ***`count()`*** *method from* ***`storage`***.

### ***Expected Output***

```
$ curl -X GET http://0.0.0.0:5000/api/v1/stats
{
  "amenities": 47, 
  "cities": 36, 
  "places": 154, 
  "reviews": 718, 
  "states": 27, 
  "users": 31
}
```
# ***Task 6:*** *Not found*

## ***Introduction***

*Designers are really creative when they have to design a “404 page”, a “Not found”… 34 brilliantly designed 404 error pages*.

*Today it’s different because you won’t use HTML and CSS, but JSON!*

### ***Instructions:***

1. *In ***`api/v1/app.py`***, create a handler for 404 errors that returns a JSON-formatted 404 status code response.* 
   - *The content should be: ***`"error": "Not found"`***.*

### ***Expected Output***

```
$ curl -X GET http://0.0.0.0:5000/api/v1/nop
{
  "error": "Not found"
}
$ curl -X GET http://0.0.0.0:5000/api/v1/nop -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/nop HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 404 NOT FOUND
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Fri, 14 Apr 2017 23:43:24 GMT
< 
{
  "error": "Not found"
}
```
# ***Task 7:*** *State*

## ***Introduction***

*Create a new view for State objects that handles all default RESTFul API actions*.

### ***Instructions:***

1. *In the file* ***`api/v1/views/states.py`***:
   - *You must use ***`to_dict()`*** to retrieve an object into a valid JSON*.
2. *Update ***`api/v1/views/__init__.py`*** to import this new file.*
3. *Implement the following actions:*
   - *Retrieves the list of all State objects: ***`GET /api/v1/states`****
   - *Retrieves a State object: ***`GET /api/v1/states/<state_id>`*****
     - *If the state_id is not linked to any State object, raise a 404 error.*
   - *Deletes a State object: ***`DELETE /api/v1/states/<state_id>`****
     - *If the state_id is not linked to any State object, raise a 404 error.*
     - *Returns an empty dictionary with the status code 200.*
   - *Creates a State: ***`POST /api/v1/states`****
     - *You must use ***`request.get_json`*** from Flask to transform the HTTP body request to a dictionary.*
     - *If the HTTP body request is not valid JSON, raise a 400 error with the message ***`"Not a JSON"`***.*
     - *If the dictionary doesn’t contain the key ***`name`***, raise a 400 error with the message "Missing name"*.
     - *Returns the new State with the status code 201.*
   - *Updates a State object: ***`PUT /api/v1/states/<state_id>`****
     - *If the state_id is not linked to any State object, raise a 404 error*.
     - *You must use ***`request.get_json`*** from Flask to transform the HTTP body request to a dictionary.*
     - *If the HTTP body request is not valid JSON, raise a 400 error with the message "Not a JSON"*.
     - *Update the State object with all key-value pairs of the dictionary.*
     - *Ignore keys: ***`id`***, ***`created_at`***, and ***`updated_at`***.*
     - *Returns the State object with the status code 200*.

### ***Expected Output***

```
$ curl -X GET http://0.0.0.0:5000/api/v1/states
[
  {
    "__class__": "State", 
    "created_at": "2017-04-14T00:00:02", 
    "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
    "name": "Louisiana", 
    "updated_at": "2017-04-14T00:00:02"
  }, 
  {
    "__class__": "State", 
    "created_at": "2017-04-14T16:21:42", 
    "id": "1a9c29c7-e39c-4840-b5f9-74310b34f269", 
    "name": "Arizona", 
    "updated_at": "2017-04-14T16:21:42"
  },
  ...
]
```
# Task 8: City

## Introduction

Create a new view for City objects that handles all default RESTFul API actions.

### Instructions:

1. In the file `api/v1/views/cities.py`:
   - You must use `to_dict()` to serialize an object into valid JSON.
2. Update `api/v1/views/__init__.py` to import this new file.
3. Implement the following actions:
   - Retrieves the list of all City objects of a State: `GET /api/v1/states/<state_id>/cities`
     - If the state_id is not linked to any State object, raise a 404 error.
   - Retrieves a City object: `GET /api/v1/cities/<city_id>`
     - If the city_id is not linked to any City object, raise a 404 error.
   - Deletes a City object: `DELETE /api/v1/cities/<city_id>`
     - If the city_id is not linked to any City object, raise a 404 error.
     - Returns an empty dictionary with the status code 200.
   - Creates a City: `POST /api/v1/states/<state_id>/cities`
     - You must use `request.get_json` from Flask to transform the HTTP body request to a dictionary.
     - If the state_id is not linked to any State object, raise a 404 error.
     - If the HTTP body request is not a valid JSON, raise a 400 error with the message "Not a JSON".
     - If the dictionary doesn’t contain the key `name`, raise a 400 error with the message "Missing name".
     - Returns the new City with the status code 201.
   - Updates a City object: `PUT /api/v1/cities/<city_id>`
     - If the city_id is not linked to any City object, raise a 404 error.
     - You must use `request.get_json` from Flask to transform the HTTP body request to a dictionary.
     - If the HTTP request body is not valid JSON, raise a 400 error with the message "Not a JSON".
     - Update the City object with all key-value pairs of the dictionary.
     - Ignore keys: `id`, `state_id`, `created_at`, and `updated_at`.
     - Returns the City object with the status code 200.

### Expected Output

```
$ curl -X GET http://0.0.0.0:5000/api/v1/states/not_an_id/cities/
{
  "error": "Not found"
}
```
# Task 9: Amenity

## Introduction

Create a new view for Amenity objects that handles all default RESTFul API actions.

### Instructions:

1. In the file `api/v1/views/amenities.py`:
   - You must use `to_dict()` to serialize an object into valid JSON.
2. Update `api/v1/views/__init__.py` to import this new file.
3. Implement the following actions:
   - Retrieves the list of all Amenity objects: `GET /api/v1/amenities`
   - Retrieves an Amenity object: `GET /api/v1/amenities/<amenity_id>`
     - If the amenity_id is not linked to any Amenity object, raise a 404 error.
   - Deletes an Amenity object: `DELETE /api/v1/amenities/<amenity_id>`
     - If the amenity_id is not linked to any Amenity object, raise a 404 error.
     - Returns an empty dictionary with the status code 200.
   - Creates an Amenity: `POST /api/v1/amenities`
     - You must use `request.get_json` from Flask to transform the HTTP request to a dictionary.
     - If the HTTP request body is not valid JSON, raise a 400 error with the message "Not a JSON".
     - If the dictionary doesn’t contain the key `name`, raise a 400 error with the message "Missing name".
     - Returns the new Amenity with the status code 201.
   - Updates an Amenity object: `PUT /api/v1/amenities/<amenity_id>`
     - If the amenity_id is not linked to any Amenity object, raise a 404 error.
     - You must use `request.get_json` from Flask to transform the HTTP request to a dictionary.
     - If the HTTP request body is not valid JSON, raise a 400 error with the message "Not a JSON".
     - Update the Amenity object with all key-value pairs of the dictionary.
     - Ignore keys: `id`, `created_at`, and `updated_at`.
     - Returns the Amenity object with the status code 200.

# Task 10: User

## Introduction

Create a new view for User objects that handles all default RESTFul API actions.

### Instructions:

1. In the file `api/v1/views/users.py`:
   - You must use `to_dict()` to retrieve an object into a valid JSON.
2. Update `api/v1/views/__init__.py` to import this new file.
3. Implement the following actions:
   - Retrieves the list of all User objects: `GET /api/v1/users`
   - Retrieves a User object: `GET /api/v1/users/<user_id>`
     - If the user_id is not linked to any User object, raise a 404 error.
   - Deletes a User object: `DELETE /api/v1/users/<user_id>`
     - If the user_id is not linked to any User object, raise a 404 error.
     - Returns an empty dictionary with the status code 200.
   - Creates a User: `POST /api/v1/users`
     - You must use `request.get_json` from Flask to transform the HTTP body request to a dictionary.
     - If the HTTP body request is not valid JSON, raise a 400 error with the message "Not a JSON".
     - If the dictionary doesn’t contain the key `email`, raise a 400 error with the message "Missing email".
     - If the dictionary doesn’t contain the key `password`, raise a 400 error with the message "Missing password".
     - Returns the new User with the status code 201.
   - Updates a User object: `PUT /api/v1/users/<user_id>`
     - If the user_id is not linked to any User object, raise a 404 error.
     - You must use `request.get_json` from Flask to transform the HTTP body request to a dictionary.
     - If the HTTP body request is not valid JSON, raise a 400 error with the message "Not a JSON".
     - Update the User object with all key-value pairs of the dictionary.
     - Ignore keys: `id`, `email`, `created_at`, and `updated_at`.
     - Returns the User object with the status code 200.

### Expected Output

```
$ curl -X GET http://0.0.0.0:5000/api/v1/users
[
  {
    "__class__": "User", 
    "created_at": "2017-04-16T03:14:06", 
    "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
    "email": "user1@example.com", 
    "password": "password1", 
    "updated_at": "2017-04-16T03:14:06"
  },
  {
    "__class__": "User", 
    "created_at": "2017-04-16T03:14:06", 
    "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
    "email": "user2@example.com", 
    "password": "password2", 
    "updated_at": "2017-04-16T03:14:06"
  }
]
```
# Task 11: Place

## Introduction

Create a new view for Place objects that handles all default RESTFul API actions.

### Instructions:

1. In the file `api/v1/views/places.py`:
   - You must use `to_dict()` to retrieve an object into a valid JSON.
2. Update `api/v1/views/__init__.py` to import this new file.
3. Implement the following actions:
   - Retrieves the list of all Place objects of a City: `GET /api/v1/cities/<city_id>/places`
     - If the city_id is not linked to any City object, raise a 404 error.
   - Retrieves a Place object: `GET /api/v1/places/<place_id>`
     - If the place_id is not linked to any Place object, raise a 404 error.
   - Deletes a Place object: `DELETE /api/v1/places/<place_id>`
     - If the place_id is not linked to any Place object, raise a 404 error.
     - Returns an empty dictionary with the status code 200.
   - Creates a Place: `POST /api/v1/cities/<city_id>/places`
     - You must use `request.get_json` from Flask to transform the HTTP request to a dictionary.
     - If the city_id is not linked to any City object, raise a 404 error.
     - If the HTTP request body is not valid JSON, raise a 400 error with the message "Not a JSON".
     - If the dictionary doesn’t contain the key `user_id`, raise a 400 error with the message "Missing user_id".
     - If the user_id is not linked to any User object, raise a 404 error.
     - If the dictionary doesn’t contain the key `name`, raise a 400 error with the message "Missing name".
     - Returns the new Place with the status code 201.
   - Updates a Place object: `PUT /api/v1/places/<place_id>`
     - If the place_id is not linked to any Place object, raise a 404 error.
     - You must use `request.get_json` from Flask to transform the HTTP request to a dictionary.
     - If the HTTP request body is not valid JSON, raise a 400 error with the message "Not a JSON".
     - Update the Place object with all key-value pairs of the dictionary.
     - Ignore keys: `id`, `user_id`, `city_id`, `created_at`, and `updated_at`.
     - Returns the Place object with the status code 200.

# Task 12: Reviews

## Introduction

Create a new view for Review objects that handles all default RESTFul API actions.

### Instructions:

1. In the file `api/v1/views/places_reviews.py`:
   - You must use `to_dict()` to retrieve an object into valid JSON.
2. Update `api/v1/views/__init__.py` to import this new file.
3. Implement the following actions:
   - Retrieves the list of all Review objects of a Place: `GET /api/v1/places/<place_id>/reviews`
     - If the place_id is not linked to any Place object, raise a 404 error.
   - Retrieves a Review object: `GET /api/v1/reviews/<review_id>`
     - If the review_id is not linked to any Review object, raise a 404 error.
   - Deletes a Review object: `DELETE /api/v1/reviews/<review_id>`
     - If the review_id is not linked to any Review object, raise a 404 error.
     - Returns an empty dictionary with the status code 200.
   - Creates a Review: `POST /api/v1/places/<place_id>/reviews`
     - You must use `request.get_json` from Flask to transform the HTTP request to a dictionary.
     - If the place_id is not linked to any Place object, raise a 404 error.
     - If the HTTP body request is not valid JSON, raise a 400 error with the message "Not a JSON".
     - If the dictionary doesn’t contain the key `user_id`, raise a 400 error with the message "Missing user_id".
     - If the user_id is not linked to any User object, raise a 404 error.
     - If the dictionary doesn’t contain the key `text`, raise a 400 error with the message "Missing text".
     - Returns the new Review with the status code 201.
   - Updates a Review object: `PUT /api/v1/reviews/<review_id>`
     - If the review_id is not linked to any Review object, raise a 404 error.
     - You must use `request.get_json` from Flask to transform the HTTP request to a dictionary.
     - If the HTTP request body is not valid JSON, raise a 400 error with the message "Not a JSON".
     - Update the Review object with all key-value pairs of the dictionary.
     - Ignore keys: `id`, `user_id`, `place_id`, `created_at`, and `updated_at`.
     - Returns the Review object with the status code 200.

# Task 13: HTTP Access Control (CORS)

## Introduction

HTTP Access Control (CORS) is essential for allowing web clients to make requests to your API from different domains or ports. Without CORS setup, the web client won't be able to access your API data due to browser security restrictions.

### Instructions:

1. Install the `flask_cors` module using pip:
   ```bash
   $ pip3 install flask_cors

Update api/v1/app.py to create a CORS instance allowing /* for 0.0.0.0.

You will update the CORS settings later when you deploy your API to production.

Sample HTTP Response Header:
Access-Control-Allow-Origin: 0.0.0.0

Implementation:
Update api/v1/app.py with the following code snippet:
from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://0.0.0.0"}})  # Allow CORS for all API routes

# Register blueprint
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)

This code snippet allows CORS for all routes under /api/* from the domain http://0.0.0.0.





