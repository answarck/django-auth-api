# Django Authentication API

A robust and scalable Django-based authentication API providing secure user management and streamlined access control. This API integrates modern authentication practices, including JWT and Google SSO, and offers comprehensive interactive documentation for seamless developer experience.

-----

## 🚀 Features

This API empowers your applications with a full suite of authentication capabilities:

  * **User Registration:** Securely register new users with standard username and password credentials.
  * **User Role Management:** Easily define and modify user roles (e.g., admin, normal user, staff) through the intuitive Django administration panel, enabling granular access control and privilege assignment.
  * **JWT-based Authentication:** Implement secure and stateless authentication using JSON Web Tokens (JWTs) for both access and refresh tokens.
  * **Google SSO Integration:** Facilitate quick and convenient user onboarding through Google Single Sign-On (SSO).
  * **Session Management & Logout:** Provides robust logout functionality and handles session invalidation for enhanced security.
  * **Interactive API Documentation:** Explore and test API endpoints effortlessly with built-in Swagger UI (`/api/docs/`) and Redoc (`/api/redoc/`) interfaces, powered by OpenAPI specifications.

-----

## 🔧 Technologies Used

This project is built with:

  * **Django:** A high-level Python web framework for rapid, secure, and maintainable web development.
  * **Django REST Framework (DRF):** A powerful toolkit for building robust Web APIs with Django.
  * **djangorestframework-simplejwt:** Provides JWT (JSON Web Token) authentication for DRF, enabling stateless authentication.
  * **django-allauth:** Handles comprehensive authentication, including local accounts and social logins like Google SSO.
  * **drf-spectacular:** Generates OpenAPI 3 schema for interactive API documentation (Swagger, Redoc).

-----

## 📦 Installation & Setup

Follow these steps to get the API up and running on your local machine:

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/answarck/django_auth_api.git
    cd django_auth_api
    ```

2.  **Create and Activate a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    Install all required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Migrations:**
    Apply the necessary database migrations to set up the models:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a Superuser (Optional but Recommended):**
    To access the Django administration panel and manage users, create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up your username, email, and password.
6.  **Rename env.example to .env:**
    ```bash
    mv env.example .env
    ```

7.  **Run the Development Server:**
    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

    This will deploy the application, typically accessible at `http://127.0.0.1:8000/`.

-----

## 📘 Usage & Endpoints

Once the server is running, you can interact with the API using the following endpoints:

### API Documentation

  * **Swagger UI:** Access the interactive Swagger documentation at:
    `http://127.0.0.1:8000/api/docs/`
    This interface allows you to view all available endpoints, their parameters, and even make live API requests.

  * **Redoc:** View the API documentation in Redoc format at:
    `http://127.0.0.1:8000/api/redoc/`
    Redoc provides a clean, single-page documentation layout, ideal for quick reference.

### Admin Panel

  * **Django Admin Access:** Log in to the Django administration panel at:
    `http://127.0.0.1:8000/admin/`
    Use the superuser credentials you created during installation.

### User Role Management

To change user privileges (e.g., set a user as staff or superuser):

1.  Log in to the Django Admin Panel (`http://127.0.0.1:8000/admin/`) using your superuser credentials.
2.  Navigate to the **Authentication and Authorization** section, then click on **Users**.
3.  Select the user whose privileges you wish to modify.
4.  Within the user's detail page, you can adjust the following:
      * **Staff status:** Check `Staff status` to grant the user access to the admin site (useful for internal team members who manage content or other users).
      * **Superuser status:** Check `Superuser status` to grant the user all permissions without explicitly assigning them.
      * **Groups:** Assign users to specific groups with predefined permissions.
      * **User permissions:** Grant individual permissions directly to the user.
5.  Click "Save" to apply the changes.

### Google SSO Setup

To enable Google Single Sign-On:

1.  **Create a Google OAuth Client ID:**

      * Go to the [Google Cloud Console](https://console.cloud.google.com/).
      * Select an existing project or create a new one.
      * Navigate to **APIs & Services \> Credentials**.
      * Click **+ Create Credentials** and select **OAuth client ID**.
      * If prompted, configure the **OAuth consent screen** first (provide app name, support email, and authorized domains like `127.0.0.1` or `localhost`).
      * For **Application type**, select **Web application**.
      * Provide a **Name** for your OAuth client (e.g., "Django Auth API").
      * Under **Authorized JavaScript origins**, add your application's base URL (e.g., `http://127.0.0.1:8000`).
      * Under **Authorized redirect URIs**, add the callback URL for Django Allauth: `http://172.0.0.1:8000/accounts/google/login/callback/` (adjust domain/port if different).
      * Click **Create**. You will see your **Client ID** and **Client Secret**. Copy these values.

2.  **Update `.env` file:**
    Ensure that the `CLIENT_ID` and `CLIENT_SECRET` variables in your `.env` file are updated with the values you just obtained from Google Cloud Console.

3.  **Configure in Django Admin:**

      * Log in to your Django Admin Panel (`http://127.0.0.1:8000/admin/`).
      * Navigate to the **Social Accounts** section, then click on **Social applications**.
      * Click **+ Add social application**.
      * Fill in the details:
          * **Provider:** Select `Google`.
          * **Name:** Give it a descriptive name (e.g., `Google SSO`).
          * **Client ID:** Paste the Client ID you copied from Google Cloud Console (this value should match the `CLIENT_ID` in your `.env`).
          * **Secret Key:** Paste the Client Secret you copied from Google Cloud Console (this value should match the `CLIENT_SECRET` in your `.env`).
          * **Sites:** Select your current site (e.g., `example.com` or `127.0.0.1:8000`). If your site isn't listed, you might need to add/update it under **Sites \> Sites** in the admin panel.
      * Click **Save**.

  
### Core Authentication Endpoints (Under `/api/`)

While the exact paths will be detailed in the Swagger/Redoc documentation, here are the typical categories of endpoints you can expect:

  * **User Registration:**
      * `POST /api/register/`: To create new user accounts.
  * **JWT Login & Refresh:**
      * `POST /api/login/`: To log in user accounts with username and password and obtain JWT access and refresh tokens.
      * `POST /api/token/refresh/`: To refresh an expired access token using a valid refresh token.
  * **Google SSO Login:**
      * To initiate Google SSO, your frontend application would typically redirect users to `http://127.0.0.1:8000/accounts/google/login/` (or a page linking to it).

**Note:** For detailed request/response schemas and exact endpoint paths, please refer to the Swagger UI (`http://127.0.0.1:8000/api/docs/`).

-----