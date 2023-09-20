# 📝Inventory List📝
## Assignment 2: Model-View-Template (MVT) Implementation on Django

**Student Details :**

|  `Attribute`  |               `Information`               |
|---------------|-------------------------------------------|
| Name          | Ardhika Satria Narendra                   |
| Student ID    | 2206821866                                |
| Class         | PBP KKI                                   |
| Website URL   | https://inventorylist.adaptable.app/main/ |

---

## Questions and Answers

### -> How do you implement the tasks in the checklist?

1. **Creating a new Django project**

   To start building this application, I initiated a new Django project. Here's how I did it:
   
  - Opened the terminal or command prompt on my system.
  - Navigated to the directory where I wanted to store my Git projects using the command `cd <directory_name>`.
  - Initialized a new repository with the command `git init`. This command created an empty Git repository in my chosen directory.
  - Create and activate the virtual environment by running the following command `python -m venv env` and `env\Scripts\activate.bat`.
  - Created a file named requirements.txt and installed the dependencies with the following command `pip install -r requirements.txt`.
  - Create a Django project using this command `django-admin startproject inventory_list`.
  - Add "*" on `ALLOWED_HOST` in `settings.py`
```
ALLOWED_HOST = ["*"]
```
- Add `.gitignore` file
2. **Creating an app with the name main on that project**

    I needed to create a new app within my Django project. Here's the process I followed:
  - Ran the following command: `python manage.py startapp main`. This command created a new app named "main" within my project.
  - Add `'main'` to the list of existing applications in settings.py.
  - Create folder `templates` inside `main` also `main.html` inside the folder.

3. **Creating a URL routing configuration to access the 'main' app**

   To ensure that I could access the 'main' app, I set up URL routing. Here's how I configured it:
  - Opened the main project's `urls.py` file located in the project's root directory.
  - Imported the `include` function from `django.urls`: `from django.urls import path, include`.
  - Added a new URL pattern to include the 'main' app's URLs. For example:
    ```
    path('main/', include('main.urls')),
    ```
    This mapping directed the `/main/` URL path to the URLs defined in the `main` app's `urls.py`.

4. **Creating a model within the 'main' app**

   I needed to define a model within the 'main' app with specific attributes. Here's how I implemented it:
  - In the `main` app directory, I opened the `models.py` and modified it with the mandatory attributes.
  - In this step, I created a model named `Item` within the 'main' app. The model will define the attributes of items in my inventory management application.

5. **Creating a function in 'views.py' to return an HTML template**
   
     To display information about the application, app name, my name, and my class, I created a view function. Here's how I accomplished it:
  - In the `main` app directory, I opened the `views.py` file.
  - I defined a view function, for example, `show_main`, that took a `request` parameter.
  - Within the view function, I created a `context` dictionary with the necessary data, including app name, my name, and class.
  - I used the `render` function to render an HTML template (e.g., `main.html`) and passed the `context` data to it.

6. **Creating a URL routing to map the function in 'views.py'**

   To ensure that the view function I created is accessible through a URL, I configured URL routing within the 'main' app. Here's how I did it:
- In the `main` app directory, I created a `urls.py` file.
- I defined URL patterns within the `urls.py` file, for example:
     ```
     from django.urls import path
     from main.views import show_main

     app_name = 'main'

      urlpatterns = [
         path('', show_main, name='show_main'),
      ]
      ```
      This mapping directed the root URL (e.g., `/main/`) to the `show_main` view function.
     
7. **Deploying the app to Adaptable**
   
   To make the application accessible online, I deployed it to Adaptable or a similar hosting service. Here are the general steps I followed:
- I ensured that my Django project was under version control with Git.
- I pushed my project code to the GitHub repository.
- I used Adaptable or a similar service to deploy my Django application, following my lecture's deployment instructions to make the app accessible online.
  
---
### -> Create a diagram explaining the flow of client requests to a Django web app and its response

```mermaid
graph TB

    subgraph User
        A[Browser]
    end

    subgraph Django Environment
        B[urls.py]
        C[views.py]
        D[models.py]
        E[HTML Template]
    end

    subgraph Database
        F[Database Table]
    end

    %% Defining the flow in a square pattern
    A -->|1. HTTP Request| B
    B -->|2. URL Mapping| C
    C -->|3. Read or Write Data| D
    D -->|4. Data Access| F
    F -->|7. Return Data| D
    D -->|5. Render Template| E
    E -->|6. HTML Response| A
```
Here's a step-by-step explanation of the depicted process:

1. **HTTP Request**: The user makes a request via a web browser.
    - **Component**: Browser
    - **Action**: The browser sends an HTTP request to the Django environment.

2. **URL Mapping**: The request reaches the `urls.py` in the Django environment.
    - **Component**: urls.py
    - **Action**: Django uses the `urls.py` file to map the incoming request to the corresponding view.

3. **Read or Write Data**: The view (`views.py`) may need to read or write data to the database using Django models.
    - **Component**: views.py & models.py
    - **Action**: Depending on the nature of the request (e.g., GET, POST), the view might fetch or update data from the database using models.

4. **Data Access**: The views might also need to access certain HTML templates to generate a response.
    - **Component**: views.py & HTML Template
    - **Action**: The view fetches the relevant HTML template if needed.

5. **Render Template**: The models help in fetching the necessary data which is then used to populate and render the HTML templates.
    - **Component**: models.py & HTML Template
    - **Action**: The actual data is filled into the template to create a meaningful HTML page for the user.

6. **HTML Response**: The populated HTML template is then sent back as a response to the browser.
    - **Component**: HTML Template & Browser
    - **Action**: The rendered HTML page is displayed on the user's browser.

7. **Access**: This is a separate process where models interact with the database tables to perform CRUD operations.
    - **Component**: models.py & Database Table
    - **Action**: Direct interaction with the database to either create, read, update, or delete records.

To sum it up, when a user sends a request from their browser, Django processes it by mapping the request to a view, accessing the necessary data and templates, and then sending back the relevant HTML response. The database plays a central role, storing and providing data when needed.

---

### -> What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?
A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, along with a number of additional packages. The primary purpose of a virtual environment is to:
1. Isolation: Virtual environments allow Python projects to have isolated dependencies, ensuring that the requirements of each project are in harmony with those of others.
2. Dependency Management: To minimise issues, virtual environments manage different library versions across projects.
3. Version Control: Virtual environments make it easier to work with and test different Python versions.
4. Clean Environment: When starting a new project, we can create a new virtual environment to ensure we're working in a clean environment with only the necessary dependencies installed.

Yes, we can create a Django web app without a virtual environment. However, there are some downsides to this:
1. Potential Dependency Conflicts: Without using a virtual environment, it will risk running into issues where Django or one of its dependencies conflicts with another library or application on our system.
2. System Pollution: Installing everything globally can clutter the system's Python environment with unnecessary packages.
3. Versioning Issues: If we're working on two Django projects where one uses Django 2.x and the other uses Django 3.x, we'll face issues if we don't use separate virtual environments.
4. Deployment Challenges: It becomes more challenging to ensure that our production environment matches our development environment in terms of dependencies and versions, which can lead to unexpected behaviours and bugs.

Using virtual environments is a best practice in Python development, especially with web frameworks like Django, because of the challenges and risks mentioned above. While it's not strictly required, it's highly recommended.

---

### -> What is MVC, MVT, and MVVM? Explain the differences between the three.

**MVC (Model-View-Controller):**
- **Model**: Manages the data and business logic.
- **View**: Displays the data (the UI part).
- **Controller**: Handles the user's input and updates the Model and View.

**MVT (Model-View-Template):**
- **Model**: Represents the data structure.
- **View**: Controls what data is displayed and how (more like a controller).
- **Template**: How the data is displayed (akin to the view in MVC).

**MVVM (Model-View-ViewModel):**
- **Model**: Represents the data.
- **View**: Displays the data, purely the UI.
- **ViewModel**: An abstraction of the view, that holds presentational logic.

**Differences:** 
1. **MVC**: A discrete separation in which the controller serves as a connection between the Model and the View.
2. **MVT**: This is primarily used in Django. The "View" works more like a controller, whereas the "Template" is similar to the MVC view.
3. **MVVM**: Suitable for applications with an abundant user interface, such as those built using WPF or Angular. It connects the View and ViewModel, allowing them to communicate with one another.

While all three are architectural patterns aimed at separating concerns, they differ in how they divide jobs and duties.

---

## Assignment 3: Forms and Data Delivery Implementation in Django

## Questions and Answers

### -> What is the difference between `POST` form and `GET` form in Django?
Let's compare POST and GET forms in Django. There are various significant dissimilarity listed below, which I will explain one by one in each category :
   1. **Data Transmission Method**: 
      - GET: Sends data via the URL. When a GET form is submitted, the form data is attached to the URL as query parameters.
      - POST: Sends data in the HTTP request body rather than the URL. It is more suited for transmitting big amounts of data or sensitive information.
   2. **Visibility**: 
      - GET: Because the data is in the URL, anyone who sees the URL can view it. A poor choice for private information.
      - POST: Because the data is in the request body, it is hidden from viewers.
   3. **Usage**: 
      - GET: Typically used for obtaining or retrieving data where the action does not change or influence the data on the server. For example, searching or filtering results.
      - POST: Used for activities that modify data or have side effects, such as submitting a form to register an account or placing an order.
   4. **Data Limits**: 
      - GET: Limited by the URL length, which is normally around 2,000 characters, however this limit may differ by browser and server.
      - POST: Can handle a significantly higher quantity of data because it is in the request body.
   5. **Idempotency (a bit technical, but useful to know)**:
      - GET: Considered independent, which means that making the same request numerous times should produce the same response without producing any side effects.
      - POST: Not idempotent. Submitting a POST request several times may result in the creation of multiple resources or the triggering of various actions.

---

### -> What are the main differences between XML, JSON, and HTML in the context of data delivery?
I will explain the distinction using a simple illustration to make it clear :
   1. **Extensible Markup Language (XML)**:
      Consider XML to be a nice gift box with each thing carefully labelled. You've assigned tags to each item of data.         It's the same as wrapping a toy and labelling it: <toy>Train set</toy>. It's thorough, but with all many labels, it       can feel a little heavy. XML can be used for organised and self-descriptive data.

   2. **JSON (JavaScript Object Notation)**:
      JSON is similar to those reusable gift bags. It's more sleek and manageable than the box. Instead of utilising            elaborate labels like XML, JSON employs a basic key-value pair system, similar to tagging a gift with "toy": "Train       set." It's grown highly popular due to its light weight and ease of reading. JSON is preferred for simple data            transfer and JavaScript interaction.

   3. **HTML  (Hypertext Markup Language)**:
      HTML, on the other hand, is a little different. Consider it a gift wrapped to display and show off bits of what's         inside, similar to clear gift bags or wrappers. It is not only about the data, but also about how it appears and is       presented. It's intended to be seen in web browsers, displaying content in an aesthetically organised manner. HTML        is concerned with presenting data in a visual format, with an emphasis on its appearance and layout.
      
---

### -> Why is JSON often used in data exchange between modern web applications?
JSON is simple to produce and understand because it uses a human-readable format of key-value pairs and arrays. Unlike XML, another popular data format for online applications, JSON does not require any particular tags, attributes, or schemas. Because of its quick data transfer and web service processing results, human-readable text/code, lightweight nature, and fewer coding requirements, JSON is frequently utilised in data exchange across modern web applications. JSON is text-based, making it user friendly for developers. It also provides an easy-to-parse data format, implying less code is required for interpreting. Moreover, JSON supports better database schema and is highly interoperable/compatible with applications/technologies including the WebSocket, GraphSQL, and RESTful (Representational State Transfer) website services.

---

### -> Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. **Create a new file inside the `main` folder named `forms.py`**
   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
       class Meta:
           model = Product
           fields = ["name", "price", "description"]
      ```

2. **Create a base template**

   In this step, I created a folder named `templates` in the **root directory**. Inside the `templates` folder, I also created a file named `base.html`. This file will serve as a base template, providing a general structure for our website's pages.

   ```
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
       <head>
           <meta charset="UTF-8" />
           <meta
               name="viewport"
               content="width=device-width, initial-scale=1.0"
           />
           {% block meta %}
           {% endblock meta %}
       </head>

       <body>
           {% block content %}
           {% endblock content %}
       </body>
   </html>
   
   ```
   
3. **Updating `views.py`**
   
   At this stage, I incorporated certain imports and devised a new function named `create_product` that takes a `request` parameter. Concurrently, I adjusted the `show_main` function within `views.py`.

   During this phase, I enhanced the `views.py` to support product creation and introduced the capability to retrieve data in both XML and JSON formats. I also added functionality to obtain data based on the product ID in both XML and JSON formats.
   
   ```
   from django.shortcuts import render
   from django.http import HttpResponseRedirect
   from django.urls import reverse
   from main.forms import ProductForm
   from main.models import Product
   from django.http import HttpResponse
   from django.core import serializers

   def show_main(request):
       products = Product.objects.all()

       counter = products.count()

       context = {
           'app_name':'Inventory List',
           'name': 'Ardhika Satria Narendra',
           'class': 'PBP KKI',
           'products': products,
           'counter' : counter,
       }

       return render(request, 'main.html', context)

   def create_product(request):
       form = ProductForm(request.POST or None)

       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))

       context = {'form': form}
       return render(request, "create_product.html", context)

   def show_xml(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

3. **Add new routings to `urls.py`**
   
   I imported the previously created `create_product` function. `from main.views import show_main, create_product` and also add a new url path inside the `urlpatterns` list to access the previously imported function.
   
   ```
   # main/urls.py
   
   # ...
   
   urlpatterns = [
       path('', show_main, name='show_main'),
       path('create-product', create_product, name='create_product'),
       path('xml/', show_xml, name='show_xml'),
       path('json/', show_json, name='show_json'),
       path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
       path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
   ```

4. **Creating a new HTML file named `create_product.html`**

   At this point, I navigated to the templates subdirectory inside the main folder and crafted a new HTML file named `create_product.html`.
   
   ```
   {% extends 'base.html' %} 

   {% block content %}
   <h1>Add New Product</h1>

   <form method="POST">
       {% csrf_token %}
       <table>
           {{ form.as_table }}
           <tr>
               <td></td>
               <td>
                   <input type="submit" value="Add Product"/>
               </td>
           </tr>
       </table>
   </form>

   {% endblock %}
   ```
   
6.  **Updating `main.html`**

      I added this code between `{% block content %}` and `{% endblock content %}` to display product data in a table format and included a button to redirect users to the form page.
    
      ```
      ...
      <table>
          <tr>
              <th>Name</th>
              <th>Price</th>
              <th>Description</th>
              <th>Date Added</th>
          </tr>

          {% comment %} Below is how to show the product data {% endcomment %}

          {% for product in products %}
              <tr>
                  <td>{{product.name}}</td>
                  <td>{{product.price}}</td>
                  <td>{{product.description}}</td>
                  <td>{{product.date_added}}</td>
              </tr>
          {% endfor %}
      </table>

      <br />

      <a href="{% url 'main:create_product' %}">
          <button>
              Add New Product
          </button>
      </a>

      {% endblock content %}
      ```

---

### -> Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to `README.md`.
1. **http://localhost:8000/**

   ![image](https://github.com/ardhika23/inventory_list/assets/143513359/1058fa3c-2730-46ef-b356-3f08a805afd8)

2. **http://localhost:8000/xml**

    ![image](https://github.com/ardhika23/inventory_list/assets/143513359/100aa3e5-3797-45ae-920f-1a40bafa4a59)

3. **http://localhost:8000/json**

   ![image](https://github.com/ardhika23/inventory_list/assets/143513359/bee6fd68-697c-45ef-9365-133dfb673e9c)


4. **http://localhost:8000/xml/2**
   
   ![image](https://github.com/ardhika23/inventory_list/assets/143513359/c0359d7b-d26e-480e-9d27-7e58c63139ce)

5. **http://localhost:8000/json/2**

   ![image](https://github.com/ardhika23/inventory_list/assets/143513359/b99d6dbc-9d68-445d-be1f-f099c66e6512)


