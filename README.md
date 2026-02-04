🍨 Dutta Stores — Ice-Cream Ordering Web App

Dutta Stores is a modern, dark-themed Django-based ice-cream ordering web application that delivers a smooth, interactive, and visually engaging user experience.
It features product listings, cart functionality, authentication, FAQs, and a polished UI inspired by real-world e-commerce platforms.

🌟 Features
🏠 Landing Page

Hero section with immersive visuals

Product cards with 3D pop-out hover effects

Smooth animations and transitions

Dark / Light theme toggle (persistent via localStorage)

🍦 Product Showcase

Ice-cream items displayed using responsive cards

Hover effect that gives a “coming out of the screen” feel

Product information includes:

Image

Description

Price

Add to Cart button

🛒 Cart System

“ADD” button adds products to My Cart

Dedicated Cart page (/cart/)

Displays selected item details (price, name, etc.)

Cart accessible from user dropdown

👤 User Authentication

Signup & Login system

Profile avatar with username initial

Dropdown menu with:

My Account

My Cart

My Addresses

Logout

📌 Navigation Bar

Centered brand name “Dutta Stores”

Custom brand icon

Evenly spaced navigation items

Search bar integrated into navbar

Profile icon & theme toggle aligned neatly

❓ FAQ Section (Landing Page Only)

Accordion-style FAQ section

Common questions like:

Delivery time

Best-seller of the month

Latest launched flavour

Customer favourites

Footer “FAQs” link auto-scrolls to FAQ section

🦶 Footer

Visible only on landing page

Categories, useful links, and social media icons

Fully dark-theme compatible

Smooth scrolling enabled

Social icons linked to personal accounts

🛠️ Tech Stack
Backend

Python 3

Django 6.0.1

Frontend

HTML5

CSS3 (custom styling + animations)

Bootstrap 5

Bootstrap Icons

Database

SQLite (default, can be replaced with PostgreSQL/MySQL)

📁 Project Structure
Dutta-Stores/
│
├── home/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── components/
│   │   ├── footer.html
│   │   ├── navbar.html
│
├── static/
│   ├── css/
│   │   ├── navbar.css
│   │   ├── footer.css
│
├── manage.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/dutta-stores.git
cd dutta-stores

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start Development Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

🎨 UI & UX Highlights
-> Glossy headings using text-shadow
-> Smooth hover animations
-> Responsive design for all screen sizes
-> Dark mode consistency across navbar, footer, FAQ, and cards
-> Clean spacing and alignment for professional look

🔐 Authentication Notes
-> Login required for:
-> Accessing Cart
-> Viewing account details
-> Django’s built-in authentication system is used

📸 Screenshots
<img width="1881" height="891" alt="image" src="https://github.com/user-attachments/assets/7dde98aa-c914-4113-a380-3d2a80c50270" />
<img width="1881" height="891" alt="image" src="https://github.com/user-attachments/assets/f668c544-46b1-4602-81ff-77d032fd2a1c" />
![WhatsApp Image 2026-02-04 at 19 27 43](https://github.com/user-attachments/assets/dd92089e-cf12-4f53-8a8b-b8cdec8e84df)
![WhatsApp Image 2026-02-04 at 19 27 31](https://github.com/user-attachments/assets/f5302093-bb4a-40c7-8568-dee7f4149f14)

👨‍💻 Author

Pratyush Dutta
Built with ❤️ using Django & Bootstrap
