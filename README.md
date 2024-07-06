# Django E-Commerce Project README

## Table of Contents
1. [Introduction](#1-introduction)
2. [User Experience](#2-user-experience)
   - [Strategy](#21-strategy)
     - [Target Users](#target-users)
     - [What the User Would Look For](#what-the-user-would-look-for)
     - [User Stories](#user-stories)
   - [Scope](#22-scope)
     - [Sprint 1](#sprint-1)
     - [Sprint 2](#sprint-2)
     - [Future Sprints](#future-sprints)
   - [Structure](#23-structure)
3. [Project Applications](#3-project-applications)
4. [Project Databases](#4-project-databases)
   - [Post Model](#post-model)
   - [Upload](#upload)
5. [Skeleton](#5-skeleton)
   - [Wireframes](#wireframes)
6. [Features](#6-features)
   - [Existing Features](#existing-features)
     - [Home](#home)
     - [Profile page](#profile-page)
     - [Upload page](#upload-page)
     - [Search](#search)
     - [Nav bar](#nav-bar)
     - [Post detail](#post-detail)
     - [Comments](#comments)
     - [Delete / Edit posts](#delete--edit-posts)
     - [Random post](#random-post)
7. [Technologies Used](#7-technologies-used)
   - [Languages](#languages)
   - [Tools](#tools)
   - [Styling](#styling)
8. [Validation](#8-validation)
   - [Code Validation](#code-validation)
   - [Responsiveness](#responsiveness)
9. [Bugs](#9-bugs)
10. [Deployment](#10-deployment)
   - [Create Application](#create-application)
   - [Final Repo Preparations](#final-repo-preparations)
11. [Credits](#11-credits)

---

## 1. Introduction
The Django E-Commerce project is an advanced online platform designed for purchasing laptops and phones. It offers a robust e-commerce experience where users can browse products, securely place orders using Stripe, and provide feedback through product reviews.

## 2. User Experience

### 2.1 Strategy

#### Target Users
The primary target audience includes tech-savvy individuals aged 18 and older who prefer the convenience of online shopping for electronics.

#### What the User Would Look For
Users seek a seamless shopping experience with a diverse product catalog, intuitive navigation, secure payment options, and the ability to share product experiences through reviews.

#### User Stories
- As a user, I want to explore a variety of laptops and phones to make informed purchase decisions.
- As a user, I want a straightforward sign-in process to access personalized features and complete purchases securely.
- As a user, I want to checkout quickly and securely using Stripe to finalize my purchase.
- As a user, I want to leave detailed reviews to help other shoppers make informed decisions.

### 2.2 Scope

#### Sprint 1
Implemented essential functionalities including the homepage, navigation bar, user registration and login, and detailed product pages.

#### Sprint 2
Enhanced user experience with a streamlined checkout process, a responsive shopping cart, and comprehensive order details display.

#### Future Sprints
Planned expansions include enabling new sellers to list their products for sale, fostering a dynamic marketplace environment.

### 2.3 Structure
The project is meticulously structured to ensure efficient development and user engagement. Applications are modularized to handle distinct tasks, while databases are optimized for scalability and data integrity.

---

## 3. Project Applications
- **User Authentication**: Secure authentication system for user management.
- **Product Catalog**: Comprehensive catalog of laptops and phones.
- **Shopping Cart**: Interactive cart management for seamless shopping experiences.
- **Checkout**: Secure payment gateway integration with Stripe for hassle-free transactions.

---

## 4. Project Databases

### Post Model
Captures user-generated content including product titles, user-friendly URLs (slugs), author details, product descriptions, uploaded images, and user reviews for products.

### Upload
Manages uploaded product artwork details such as titles, descriptions, images, and pricing information.

---

## 5. Skeleton

### Wireframes

#### Home Page
![Picture1](https://github.com/KadDenuwara/TechGiants/assets/137709290/ffe9d906-f86b-4d36-85e6-96ad5faca71d)

#### Product Page
![Picture2](https://github.com/KadDenuwara/TechGiants/assets/137709290/8a0c2591-edb2-47f7-8def-05e2aa5faa26)

#### SignIn Page
![Picture6](https://github.com/KadDenuwara/TechGiants/assets/137709290/cc5abfe2-2e60-42a5-9a47-221891f026c6)

#### SignUp Page
![Picture7](https://github.com/KadDenuwara/TechGiants/assets/137709290/c1bf33f6-46ba-44e9-969c-20a30e74ba79)

#### ContactUs Page  
![Picture5](https://github.com/KadDenuwara/TechGiants/assets/137709290/a2451015-6ad7-49f0-aba5-923329bbf0df)

---

## 6. Features

### Existing Features

#### Home
- Presents a visually appealing and informative landing page showcasing featured products and promotional offers.

#### Profile page
- Allows users to manage personal information, view order history, and update preferences.

#### Upload page
- Enables sellers to upload product details, including images and descriptions, to list items for sale.

#### Search
- Facilitates easy navigation through a robust search functionality that retrieves relevant products based on user queries.

#### Nav bar
- Provides intuitive navigation with a responsive navbar that adapts seamlessly across different device sizes.

#### Post detail
- Displays comprehensive product details including specifications, pricing, and customer reviews for informed purchasing decisions.

#### Comments
- Enables users to leave feedback and engage in discussions about products through interactive commenting features.

#### Delete / Edit posts
- Allows users to manage their listings by editing product details or removing items no longer for sale.

#### Random post
- Enhances user engagement with a feature that presents random products to encourage exploration and discovery.

---

## 7. Technologies Used

### Languages
- **HTML**: Used for creating structured Django templates.
- **CSS**: Stylesheets for customizing the website's visual presentation.
- **JavaScript**: Enhances interactivity and dynamic content on the frontend.
- **Python**: Primary language for backend development using Django's framework.

### Tools
- **Django**: Framework for rapid development and robust web application management.
- **Crispy Forms**: Integrates forms seamlessly into Django templates for improved user interaction.
- **GitHub**: Version control and collaborative development platform.
- **Illustrator**: Used for creating detailed wireframes and visual assets.

### Styling
- **Bootstrap**: Provides pre-built components and responsive layout utilities for frontend design.
- **Google Fonts**: Adds visually appealing typography options to enhance readability and aesthetics.

---

## 8. Validation

### Code Validation

#### W3C CSS Validator
- My css passed as well when it came to testing as I was frequently testing it in the validator.

![Screenshot 2024-07-06 222140](https://github.com/KadDenuwara/TechGiants/assets/137709290/3edea770-bb77-465c-9ae3-92561ddf916b)

![Screenshot 2024-07-06 222208](https://github.com/KadDenuwara/TechGiants/assets/137709290/68ea245f-a459-4d50-88ba-136948557aca)

![Screenshot 2024-07-06 222237](https://github.com/KadDenuwara/TechGiants/assets/137709290/711b65a0-92da-4654-8570-c015346eb9d6)

#### CI Python checker
- I checked all of my python files with the Code Institute python checker and recieved no issues with any of the files.

![Screenshot 2024-07-06 223131](https://github.com/KadDenuwara/TechGiants/assets/137709290/b4c8ec1a-eecb-40b5-81dc-eadb09d46d42)


### Responsiveness

The responsiveness of the design was manually checked using the Chrome Developer Tools for various screens.

This included:

- iPhone SE
- Pixel 5
- Samsung Galaxy S8, S20 Ultra
- iPad Air and Mini
- Galaxy Fold
- Nest Hub and Hub Max
  
I also opted to use the responsiveness option and checked the screens at the following width sizes:

- 350px
- 768px
- 992px
- 1400px

No issues arose, due to the simple layout of the site.

---

## 9. Bugs

- While adding placeholders to the pages, I faced an issue where the post didn't show the Cloudinary link placeholder when no image was provided by the user. This happened because the model's placeholder didn't match properly. I fixed it by directly linking the placeholder in the HTML.

- There was an issue with the JavaScript redirecting the user to a post detail page after a successful upload. The script expected a JSON response but didn't receive it. I added a check to see what it was receiving, which then allowed it to redirect correctly.

- I had trouble selecting parts of a form generated by Django in the template because there was no HTML to work with. I used the developer tools to see the structure and fixed the issue of the form overflowing on the page.

- The slugs for post details were based on the post titles. During manual testing, I found that errors occurred when creating or editing a post with the same title as another. I solved this by generating a random slug for each post, allowing titles to be the same without causing issues.

---

## 10. Deployment

### Create Application

- If you don't have a Heroku account, start by signing up and logging in.
- To establish a new application, click the "new" button located at the top right corner of the dashboard, then select "Create new app."
- Pick a distinct name for the application, indicate your residing region, and proceed by clicking "Create App."

### Final Repo Preparations

- Execute necessary project migrations by entering python3 manage.py makemigrations followed by python3 manage.py migrate in the terminal.
- Integrate a Procfile into the project, including the line web: gunicorn [project_name].wsgi:application.

---

## 11. Credits


