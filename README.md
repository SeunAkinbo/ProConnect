# ProConnect Project

## Project Description

ProConnect is a social networking platform designed to connect people with similar interests and hobbies. Users can create profiles, collaborate on projects, build their networks, and earn opportunities. Born out of the challenges posed by the COVID-19 pandemic, ProConnect aims to bridge the gap between skilled professionals and the market's needs, empowering graduates and professionals to showcase their skills and unlock new opportunities.

## Project Team

**Team Name:** ProConnect

**Team Members:**
- Brenda Rikhotso
- Oluwaseun Akinbo

## Introduction

### Inspiration and Vision

The COVID-19 pandemic drastically changed the job market, leading to high unemployment rates and underutilized skills among professionals. Witnessing the struggles of talented individuals facing limited opportunities, I was inspired to create a platform that could address this issue. My partner and I envisioned ProConnect as a solution to bridge the gap between skilled professionals and market needs, fostering a community where collaboration thrives and every skill finds its value.

You can visit the deployed site [here](https://www.brendarikhotso.tech/).

Read the full story behind ProConnect in our [final project blog article](https://medium.com/@brenda.rikhotso/from-setback-to-startup-the-birth-of-proconnect-f67ed95809c9).

### About Me: Brenda

I'm Brenda, a chemical engineering graduate with a penchant for technology and a newfound passion for software development. My journey into code began not in a classroom, but in my childhood bedroom. I spent countless hours tinkering with old computers, trying to unravel their mysteries and make them do my bidding. This fascination with problem-solving and building things from scratch ultimately led me down the path of engineering and, more recently, the exciting world of software development. Having a background in engineering fueled my desire to find a solution that effectively utilizes the skills of talented individuals.

![ProConnect Screenshot](https://i.imgur.com/CCDlKUS.png)

## Installation

To run ProConnect locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/brikhotso/proconnect.git
    cd proconnect
    ```

2. **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application:**
    ```bash
    flask run
    ```

## Usage

1. Visit the deployed site or run the application locally as described above.
2. Register a new account or log in with an existing one.
3. Create a profile to showcase your skills and expertise.
4. Use the platform to connect with other professionals, collaborate on projects, and explore new opportunities.

## Overcoming Challenges

### 1. Setting Up the Backend

The first major challenge was setting up a robust backend. I opted for Flask due to its simplicity and flexibility. Setting up the database using SQLAlchemy and ensuring smooth interactions was crucial. The design had to be scalable to handle numerous users and interactions.

### 2. User Authentication and a Forced Pivot

Ensuring secure user authentication was paramount. I initially explored using a specific framework, but after encountering challenges, I had to adapt. This experience taught me the value of flexibility and the importance of researching alternative solutions. Ultimately, I integrated Flask-Login for user sessions and bcrypt for password hashing, providing a secure and seamless login experience.

### 3. Dynamic Form Handling

Handling dynamic forms, especially for adding and removing skills, required careful consideration. I implemented JavaScript to manage the form elements dynamically, ensuring a smooth user experience.

### 4. Implementing Light and Dark Mode

Adding light and dark mode was a feature aimed at enhancing user experience. Using CSS variables and JavaScript, I toggled between the themes, ensuring the application was visually appealing in both modes.

### 5. Ensuring Responsive Design

With a user base that could access the platform from various devices, ensuring a responsive design was critical. I used CSS media queries and Bootstrap to make the site adaptable to different screen sizes, providing a seamless experience across devices.

### 6. Real-Time Collaboration

Implementing real-time collaboration features, such as instant messaging and live updates, was a significant technical challenge. I used WebSockets to enable real-time communication, allowing users to collaborate efficiently.

## Lessons Learned

Developing ProConnect was a journey of growth and learning. I learned the importance of flexibility, adaptability, and continuous learning. Each challenge was an opportunity to improve my problem-solving skills and deepen my understanding of software development.

## Problem Addressed by ProConnect

My own experience of being laid off and witnessing colleagues underemployed due to a skills gap fueled the development of ProConnect. It aims to address this challenge by providing a platform for graduates and professionals to connect, exchange skills, collaborate on projects, and explore entrepreneurial opportunities. It's about empowering individuals to take control of their careers and not let valuable skills go to waste.

## Moving Forward

ProConnect is more than just a project; it's a testament to the power of resilience and the importance of adapting to changing circumstances. It's a culmination of my engineering background, newfound passion for software development, and the desire to create a platform that empowers others.

As I transition from an aspiring developer to a professional software engineer, I am eager to bring the same level of passion and dedication to a dynamic and innovative team. ProConnect is a testament to my capabilities, and I am excited to leverage my skills to contribute to impactful projects and drive technological advancements.

## Contributing

We welcome contributions to ProConnect! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Description of your changes"
    ```
4. Push your changes to your fork:
    ```bash
    git push origin feature-name
    ```
5. Submit a pull request detailing your changes.

## Related Projects

Here are some related projects that might interest you:

- [GitHub](https://github.com/SuenAkinbo/ProConnect)

## Licensing

ProConnect is licensed under the [MIT License](LICENSE).

---

Feel free to connect with us on [LinkedIn](https://www.linkedin.com/in/brenda-rikhotso-a8747874/) and check out ProConnect on [GitHub](https://github.com/brikhotso/proconnect). Let's build something amazing together!
