# TechGiants

The Tech Giants website is an online shop specializing in the latest smartphones and laptops. It offers a range of products from top brands like Apple, Samsung, and Google, with special discounts and promotions. The site features categories for phones and laptops, a section for featured products, and options to sign up for a newsletter for updates on new collections and articles. The website also provides contact information and support for users.

[Visit the website here](https://techgiants-e40908f3f92d.herokuapp.com/)

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
     - [Delete / Edit comments](#delete--edit-comments)
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

![Screenshot 2024-07-08 064513](https://github.com/IsaLubs/TechGiants/assets/147058041/4f1fab35-2db3-4e6d-abcd-f7a1405e0c43)



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
- As a visitor I want to add a product to my shopping cart So that I can purchase it later.
- As an admin I want to manage existing products So that I can update or remove products as needed.
- As a user I want to write reviews for products I have purchased so that I can share my feedback with other customers.
- As a visitor I want to view a list of products within a category So that I can choose a product to view in more detail

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

## 3. Project Applications.
- **User Authentication**: Secure authentication system for user management.
- **Product Catalog**: Comprehensive catalog of laptops and phones.
- **Shopping Cart**: Interactive cart management for seamless shopping experiences.
- **Checkout**: Secure payment gateway integration with Stripe for hassle-free transactions.

---

## 4. Project Databases

5 databases can be found in the “brush_app” application, which enable the user to create the profile required to upload posts. I created a database in the begining to support the functionality created by my user stories. The first sql map is included here and was an over zealous approach to my goal. Through timing and scope my databases changed and morphed over the duration of creating it. The most up to date map is shown as well.

![output (1)](https://github.com/IsaLubs/TechGiants/assets/147058041/f0f42fba-ab04-41b9-9eb7-0bb997650fe8)


### Post Model
Captures user-generated content including product titles, user-friendly URLs (slugs), author details, product descriptions, uploaded images, and user reviews for products.
- Product Titles: The names of products listed on the site.
- User-friendly URLs (Slugs): Simplified URLs derived from the product titles for easy navigation and SEO.
- Author Details: Information about the users or authors who created the posts or reviews.
- Product Descriptions: Detailed information about each product.
- Uploaded Images: Visual content associated with products, such as pictures and diagrams.
- User Reviews: Feedback and ratings provided by users about the products.

### Upload

- Manages uploaded product details such as titles, descriptions, images, and pricing information.
- Titles: The names of the products.
- Descriptions: Information about the products.
- Images: Visual content of the products.
- Pricing Information: The cost details of the products
---
## 5. Skeleton

### Wireframes
- This wireframe was created by using Figma 
[Figma](https://www.figma.com/design/bsltgnLz4LzVP0gCgowNvU/Tech-Giants-(Home-Newdesign)?node-id=0-1&t=ljwcdIW4LlwQluhx-0)
#### Home Page

![Screenshot 2024-07-07 003942](https://github.com/IsaLubs/TechGiants/assets/147058041/ccc08712-f6b6-44da-9a7c-cc5e574b26a1)

![Screenshot 2024-07-07 004000](https://github.com/IsaLubs/TechGiants/assets/147058041/719135d1-4178-415b-9bb7-485364a7e8aa)

![Screenshot 2024-07-07 004031](https://github.com/IsaLubs/TechGiants/assets/147058041/505ce62a-aef4-4bd5-a6c5-eb6289e477ef)

#### Product Page

![Screenshot 2024-07-07 004059](https://github.com/IsaLubs/TechGiants/assets/147058041/c0480235-d27b-4ff2-adb6-f046741711a9)

#### SignIn Page

![Screenshot 2024-07-07 004226](https://github.com/IsaLubs/TechGiants/assets/147058041/98d412e0-2b44-4ed0-a3f0-9aa8bc0c55b1)

#### SignUp Page

![Screenshot 2024-07-07 004238](https://github.com/IsaLubs/TechGiants/assets/147058041/91e2890b-abe3-4442-9390-913e663595e1)

#### ContactUs Page  

![Screenshot 2024-07-07 004157](https://github.com/IsaLubs/TechGiants/assets/147058041/2b7b9cef-05ec-4f18-bd48-8e94659d5a32)

---
## 6. Features

### Existing Features

#### Home
- Presents a visually appealing and informative landing page showcasing featured products and promotional offers.
![Screenshot 2024-07-08 082154](https://github.com/IsaLubs/TechGiants/assets/147058041/af555e55-de90-414b-b6f9-6589b736e95b)

#### Social Media Links.
- Every page throughout the project has a footer with social media links.
- Clicking the social media like redirect the user to the social media page in a new tab, so as not to disrupt the user experience.
![Screenshot 2024-07-08 170152](https://github.com/IsaLubs/TechGiants/assets/147058041/6d09bc36-de10-4752-b648-70d665a6fb0f)


#### Profile page
- Allows users to manage personal information, view order history, and update preferences.

#### shopping Bag
- The shopping bag page is fully responsive, showing users a picture of the item, name, price per unit, and total price.
- Users can also choose to increase/decrease the number of items in their bag, click the update button to have the prices update.
- user can click the remove link and have all the items within the bag removed, regardless of quantity.
- At the bottom of the page user can find the cost of the bag, cost of delivery, the total and how much they must spend to be eligible for free delivery.
  ![Screenshot 2024-07-08 165404](https://github.com/IsaLubs/TechGiants/assets/147058041/5bc8f124-1272-480f-ae3b-3bfe6bfe97f6)

#### Upload page
- Enables sellers to upload product details, including images and descriptions, to list items for sale.

#### Search
- Facilitates easy navigation through a robust search functionality that retrieves relevant products based on user queries.
![Screenshot 2024-07-08 081911](https://github.com/IsaLubs/TechGiants/assets/147058041/c8a490cb-fa5b-4aff-8046-a2b722ff61f4)

#### Nav bar
- Provides intuitive navigation with a responsive navbar that adapts seamlessly across different device sizes.
![Screenshot 2024-07-08 081712](https://github.com/IsaLubs/TechGiants/assets/147058041/6a05000d-1ccf-4b66-a6d1-ee63294cb215)

#### Post detail
- Displays comprehensive product details including specifications, pricing, and customer reviews for informed purchasing decisions.
![Screenshot 2024-07-08 161339](https://github.com/IsaLubs/TechGiants/assets/147058041/ea9024a1-dba4-4763-a105-75ba37726629)

#### Comments
- Enables users to leave feedback and engage in discussions about products through interactive commenting features.
![Screenshot 2024-07-08 161502](https://github.com/IsaLubs/TechGiants/assets/147058041/23ee6bba-5721-4053-8f18-b5252c456c53)

#### Delete / Edit comments
- Allows users to manage their reviews by editing or removing.
![Screenshot 2024-07-08 063659](https://github.com/IsaLubs/TechGiants/assets/147058041/0347440f-2c71-46db-9984-90adbe35df7f)


---
## 7. Technologies Used

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML "HTML") - To create the Django templates for the associated views and models in the project applications.
* [CSS](https://en.wikipedia.org/wiki/CSS "CSS") - To style the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript") - To create interactive animations for the site.
* [Python]( https://en.wikipedia.org/wiki/Python_(programming_language) "Python") – Is the primary language of Django and used to create all forms, models and views.

### Tools
* [Django](https://www.djangoproject.com/ "Django") – The framework used in this project to incorporate databases with a website.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Crispy Forms") – Formats the models into forms on webpages using the `|crispy` filter and `{% crispy %}` tag.
* [Cloudinary](https://cloudinary.com/ "Cloudinary") - Used to store website's images.
* [Gitpod](https://www.gitpod.io/ "Gitpod") – Used as the development environment.
* [GitHub](https://github.com/ "GitHub") – The project’s Version Control Management System.
* [Heroku](https://www.heroku.com/ "Heroku") – To deploy the webpage.
* [Illustrator](https://www.adobe.com/ie/products/illustrator/campaign/pricing.html?gclid=CjwKCAjwxaanBhBQEiwA84TVXPogNfGdqMqcbQ8FXjlOcbhv5YMqMEqN6UdeCt0m35siVj5JWbijqhoCHcgQAvD_BwE&mv=search&mv=search&mv2=paidsearch&sdid=GMCWY69B&ef_id=CjwKCAjwxaanBhBQEiwA84TVXPogNfGdqMqcbQ8FXjlOcbhv5YMqMEqN6UdeCt0m35siVj5JWbijqhoCHcgQAvD_BwE:G:s&s_kwcid=AL!3085!3!547974576454!e!!g!!illustrator!1426208079!56320331432&gad=1 "Illustrator") – For the creation of associated wireframes.
* [DrawSQL](https://drawsql.app/ "DrawSQL") – For the creation of the database diagrams.
* [CSSgradient](https://cssgradient.io/ "CSSgradient") – For the visualisation of gradients for the sites styling.
* [LottieFiles](https://lottiefiles.com/ "LottieFiles") – This hosts the animated logo at the top of the screen.


### Styling

- [Bootstrap](https://getbootstrap.com/ "Bootstrap") – To provide extra styling and out-of-the-box elements e.g. burger menu.
- [Google Fonts](https://fontawesome.com/ "Google Fonts") – For font used in the site.

---
## 8. Validation

### Code Validation

#### W3C CSS Validator
- My css passed as well when it came to testing as I was frequently testing it in the validator.

![Screenshot 2024-07-06 222140](https://github.com/IsaLubs/TechGiants/assets/147058041/ba3557dd-fd8b-43af-b0d5-6a7baa34e224)

![Screenshot 2024-07-06 222208](https://github.com/IsaLubs/TechGiants/assets/147058041/28df3540-f107-4abe-93b6-4cc97985fd95)

![Screenshot 2024-07-06 222237](https://github.com/IsaLubs/TechGiants/assets/147058041/434bebc6-a146-4ca8-89b4-88def80e27b0)

#### CI Python checker
- I checked all of my python files with the Code Institute python checker and recieved no issues with any of the files.

![Screenshot 2024-07-06 223131](https://github.com/IsaLubs/TechGiants/assets/147058041/ede41c3b-e876-4d7d-897b-af125bb0373e)
----
### **Manual Testing**

**Navigation Bar** 
- Navigation bar is fully responsive on large/medium/small resolutions.
- At 320px, all navigation links are inline and not wrapping on another line.
- All links are correctly redirecting to the correct pages. 
- Signing out, correctly shows the correct dropdown options, Log in and Register.
- Signing in, correctly shows the correct dropdown options, My profile, and Logout.
- Admins, have an additional option in the dropdown menu to the Product Management page.

**Footer**
- Hover CSS is correctly working, changing the color on the icon on hover.
- Links redirect to the correct social media page.
- Links open in a new browser tab. 

**Products**
- On loading products correctly appear in SKU order.
- Sorting functionality works, correctly sorting products by price descending or ascending.
- Confirm product names and prices against their fields in the database.
- Products have the correct tag.
- Tags are correctly redirecting and filtering products by category name.

**Products Details**
- Correct redirect to the correct product on clicking the product image.
- Products details are correct and match the details in the database.
- Product quantity buttons are correctly disabled when at 1 or 99.
- Add to wishlist button correctly only shows up for logged-in users.
- Links correctly work, redirecting back to the products page and adding the product to the shopping bag.


**Reviews**
- Product reviews show for the correct product, matching the database.
- Product review form correctly not showing for users not logged in, shows for logged in users. 
- Confirm only the user who created the review or superusers have the option to edit a review.
- Editing a review, edits the review, redirects to the correct section of the page.

**Admin**
- Only admins have access to the Product Management page on the account dropdown.
- Only admins can see the Edit/Delete buttons on the product details page.
- Product Management links correctly redirect to the add product page.
- Adding a product working correctly, the product has the correct information from the form. Correctly shows within the database.
- Editing the product, working fully, reviews are maintained for the products after editing. Details correctly reflected.
- Delete button correctly shows a modal to confirm the delete.
- Deleting a product correctly removed the product from the database, and any reviews for the products are also deleted.

**Shopping Bag**
- Shopping bag link in the navbar shows the correct value of the current bag session.
- Quantity buttons are working correctly preventing the user from exceeding 99 and going below 1.
- Correct products are shown in the shopping bag.
- Adding items to the bag, and logging in after correctly retains the current bag.
- Correct totals are shown.
- Free delivery threshold correctly updates, shows correct values.

**Checkout**
- Correct items are carried over from the shopping bag to the checkout page.
- Form correctly responds to invalid inputs.
- Redirects to the checkout success page correctly.
- Stripe correctly showing 200 status webhooks for orders.

**Search Bar**
- Showing correct search for words searched.
- Adding a new product and search by its name correctly shows the product.
- User feedback is accurate.

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

**Browser Testing**

During development, the testing was mainly done solely using Google Chrome.

In production the site has been tested on the following browsers,
- Google Chrome
- Mozilla Firefox
- Opera
- Microsoft Edge
---
## 9. Bugs

- While adding placeholders to the pages, I faced an issue where the post didn't show the Cloudinary link placeholder when no image was provided by the user. This happened because the model's placeholder didn't match properly. I fixed it by directly linking the placeholder in the HTML.

- There was an issue with the JavaScript redirecting the user to a post detail page after a successful upload. The script expected a JSON response but didn't receive it. I added a check to see what it was receiving, which then allowed it to redirect correctly.

- I had trouble selecting parts of a form generated by Django in the template because there was no HTML to work with. I used the developer tools to see the structure and fixed the issue of the form overflowing on the page.

- The slugs for post details were based on the post titles. During manual testing, I found that errors occurred when creating or editing a post with the same title as another. I solved this by generating a random slug for each post, allowing titles to be the same without causing issues.

---
# Deployment

## Create Application

1. If you don't have a Heroku account, start by signing up and logging in.
2. To establish a new application, click the "new" button located at the top right corner of the dashboard, then select "Create new app."
3. Pick a distinct name for the application, indicate your residing region, and proceed by clicking "Create App."

## ElephantSQL
1. Visit elephantsql.com, log in using GitHub, and establish a fresh instance.
2. Once your project instance is set up, copy the URL. You can store this value as an environment variable to match the DATABASES variable in settings.py.
3. Utilize pip3 install dj_database_url==0.5.0 to install the dj-database-url package version 0.5.0. This will format the URL into a Django-compatible format and necessitate an update to the requirements.txt file.

## Cloudinary

1. Set up a Cloudinary account.
2. Upload relevant project images to the "Media Library."
3. Retrieve the Cloudinary API URL from your dashboard.

## Final Repo Preparations
1. Execute necessary project migrations by entering python3 manage.py makemigrations followed by python3 manage.py migrate in the terminal.
2. Integrate a Procfile into the project, including the line web: gunicorn [project_name].wsgi:application.

## Heroku Deploy
1. Return to Heroku and navigate to the Project’s page. Open the "Settings" tab and locate the "Config Vars" section.
2. Within "Config Vars," input the following key-value pairs:
   Key = PORT : Value = 8000
   Key = SECRET_KEY : Value = Your Django Secret Key from settings.py
   Key = DATABASE_URL : Value = ElephantSQL URL (from step 5)
   Key = CLOUDINARY_URL : Value = Cloudinary API URL (from step 9)
3. Proceed to the "Deploy" tab and scroll to the GitHub deployment method.
4. Search and connect to the appropriate repository by selecting the "Connect" button.
5. Continue scrolling to the bottom of the "Deploy" Page and choose your desired deployment method. Opt for "Automatically Deploy" to 
   trigger deployment with each new code push, or manually deploy by selecting the button at the page's bottom.

Your application is now successfully deployed!
----
## 11. Credits

## For Content and Code

* [Building the base of the project with the I think therefore I blog.](https://github.com/Grawnya/I-think-therefore-I-blog)
* [Lottie files webplayer creator.](https://lottiefiles.com/web-player)
* [How to create a django view.](https://www.geeksforgeeks.org/views-in-django-python/)
* [Best practice for data models.](https://cloud.google.com/appengine/docs/legacy/standard/python/datastore/datamodeling)
* [How to use django tags.](https://www.w3schools.com/django/django_template_tags.php#:~:text=In%20Django%20templates%2C%20you%20can,them%20in%20%7B%25%20%25%7D%20brackets.)
* [Checking file types with.](https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file)

## Helpful Resources
* [Stack overflow helped a lot with problem solving.](https://stackoverflow.com/)
* [MDM also contained a lot of helpful resources when building the project.](https://developer.mozilla.org/en-US/)
* [W3 schools always has very helpful threads on anything to do with coding.](https://www.w3schools.com/)
* [Github had plenty of repositories that helped a lot with coding.](https://github.com/)
* [Geeks for geeks had a lot of great information on python.](https://www.geeksforgeeks.org/python-programming-language/)

---
  # Marketing on Facebook

Here’s a step-by-step guide to help you set up your account:

 ## step 1:Create a Facebook Business Manager Account
Visit the Facebook Business Manager Website:
 [business.facebook.](https://business.facebook.com/latest/home?nav_ref=bm_home_redirect&asset_id=372112492649962)
Sign In:
If you don’t have a Facebook account, you will need to create one. If you already have a Facebook account, log in with your credentials.
Create Business Manager Account:
Click on the “Create Account” button.
Enter your business name, your name, and your business email address.
Click “Next” and fill out the remaining details about your business (address, phone number, website, etc.).
Click “Submit” to finish creating your Business Manager account.
## step 2: Add a Facebook Page to Your Business Manager
Go to Business Settings:
From the Business Manager dashboard, click on “Business Settings” (usually found in the top right corner).
Add a Page:
Under the “Accounts” section, click on “Pages.”
Click the “Add” button and choose one of the following options:
Add a Page: If you have an existing Facebook page, you can add it to your Business Manager by entering the page name or URL.
Request Access to a Page: If you need to request access to a page that belongs to another business.
Create a New Page: If you need to create a new Facebook page for your business.
## Step 3: Add an Ad Account to Your Business Manager
Go to Business Settings:
From the Business Manager dashboard, click on “Business Settings.”
Add an Ad Account:
Under the “Accounts” section, click on “Ad Accounts.”
Click the “Add” button and choose one of the following options:
Add an Ad Account: If you have an existing ad account, enter the ad account ID.
Request Access to an Ad Account: If you need to request access to an ad account that belongs to another business.
Create a New Ad Account: If you need to create a new ad account, enter the required details (account name, time zone, currency, and payment method).
## Step 4: Set Up Payment Methods
Access Payment Settings:
From the Business Manager dashboard, go to “Business Settings” and then select “Payments.”
Add Payment Method:
Click on “Add Payment Method” and enter your payment details (credit card, PayPal, etc.).
## Step 5: Assign Roles and Permissions
Manage Users:
In Business Settings, under the “People” section, you can add people to your Business Manager and assign roles (Admin, Employee, etc.).
Assign Ad Account Roles:
Go to “Ad Accounts” under the “Accounts” section.
Select the ad account and click on “Assign Partners” or “Assign People” to give access to your team members.
## Step 6: Create Your First Ad Campaign
Access Ads Manager:
From your Business Manager dashboard, click on “Ads Manager.”
Create Campaign:
Click the “Create” button.
Choose your campaign objective (e.g., Traffic, Conversions, Brand Awareness).
Follow the prompts to set up your ad set (audience targeting, budget, schedule) and ad creative (images, videos, text).
## Step 7: Monitor and Optimize Your Campaigns
Track Performance:
Use the Ads Manager to monitor the performance of your ad campaigns.
Adjust and Optimize:
Based on the performance data, adjust your targeting, budget, and ad creatives to optimize results.

Stay updated with our latest news and offers by following us on Facebook.

<a href="https://www.facebook.com/profile.php?id=61561756724837&sk=photos" target="_blank">
  <img src="https://github.com/IsaLubs/TechGiants/assets/147058041/e943ac6e-5ebc-4c0d-bf63-f46ec20d5fbb" alt="Facebook Page">
</a>

Click the image above to visit our Facebook page.


