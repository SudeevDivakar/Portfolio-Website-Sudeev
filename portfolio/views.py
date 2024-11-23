from datetime import date

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

"""Content for All Projects Page"""

all_projects = [
    {
        "slug": "turf-review",
        "image": "turfreview.jpeg",
        "project_image": ["turfreview1.png", "turfreview2.png"],
        "title": "Turf Review System",
        "github_link": "https://github.com/SudeevDivakar/Turf-Review-System",
        "project_link": "",
        "tech_used": ["NodeJS", "React", "MongoDB", "Mongoose", "Express", "Material UI", "JWT"],
        "api_used": ["Cloudinary", "OpenStreetMap"],
        "description": "A website to view and add football turfs, provide ratings, store user details, integrates map APIs and user authentication.",
        "content": """
            Turf Review System (AirBNB Clone) made using the MERN stack.

            Project Includes:
            -> Authentication using JWT.
            -> Features to Add Turfs, Delete Turfs, View Turfs, Login, Register and much more.
            -> Implements a cumulative rating system for turfs.
            -> Feature to leave comments/reviews on turfs.
            -> Stores Turf Images using the Cloudinary API.
            -> Visualize Turf Locations using the OpenStreetMap maps API. 
        """
    },
    {
        "slug": "inventory-management-rabbitmq",
        "image": "invmanagement.png",
        "project_image": ["invmanagement1.jpeg", "invmanagement2.jpeg"],
        "title": "Microservice Inventory Management (RabbitMQ)",
        "github_link": "https://github.com/SudeevDivakar/Inventory_Management_Microservices-communication-using-RabbitMQ",
        "project_link": None,
        "tech_used": ["NodeJS", "RabbitMQ", "MongoDB", "Mongoose", "Express", "Docker"],
        "api_used": None,
        "description": "Backend Inventory Management System using Node JS. RabbitMQ used as a message broker and Docker used for containerization. MongoDB used as the database to store inventory data",
        "content":"""
            Backend Inventory Management System using Node JS. RabbitMQ used as a message broker and Docker used for containerization. MongoDB used as the database to store inventory data.

            The project is made up of a producer and four consumers. The producer sends messages to an exchange which then routes the messages in the appropriate queues. The queues connect to their respective consumers which all perform various database operations.

            -> Consumer_one : Performs a basic health check to see if the RabbitMQ server and it's components are running properly
            -> Consumer_two : Item Creation Microservice to create an item.
            -> Consumer_three : Stock Management Microservice to manage stock data in the MongoDB Database.
            -> Consumer_four : Order Processing Microservice to place/update orders and get order details. 
        """
    },
    {
        "slug": "spotify-playlist-generator",
        "image": "spotify.png",
        "project_image": ["spotify1.png", "spotify2.png", "spotify3.png"],
        "title": "Spotify Playlist Generator",
        "github_link": "https://github.com/SudeevDivakar/Spotify-Playlist-Generator",
        "project_link": None,
        "tech_used": ["ReactJS", "Tailwind CSS"],
        "api_used": ["Spotify API"],
        "description": "Spotify Playlist Generator made using React, Tailwind CSS and the Spotify API.",
        "content": """
            Spotify Playlist Generator made using React, Tailwind CSS and the Spotify API.

            Two Modes of Creating Playlists:
            -> Playlist Consisting of the Top Tracks of an Individual User's Top Artists.
            -> Playlist Consisting of the Top Tracks of Artists chosen by the user
        """
    },
    {
        "slug": "parking-manager",
        "image": "parkingmanager.jpg",
        "project_image": ["parkingmanager1.png", "parkingmanager2.png"],
        "title": "Parking Lot Manager",
        "github_link": "https://github.com/SudeevDivakar/Parking_Management_System",
        "project_link": None,
        "tech_used": ["NodeJS", "EJS", "MySQL", "Express", "Bulma"],
        "api_used": None,
        "description": "Parking Management System built using MySQL, NodeJS, ExpressJS, EJS, HTML and Bulma CSS. Contains a lot of real world use cases which comes in handy for any parking management system.",
        "content": """
            Parking Management System built using MySQL, NodeJS, ExpressJS, EJS, HTML and Bulma CSS. Contains a lot of real world use cases which comes in handy for any parking management system.

            Project Includes:
            -> One Time CheckIn / CheckOut Feature for people who do not opt for a monthly pass
            -> Monthly Pass Option for Two-Wheelers and Four-Wheelers
            -> MySQL Triggers and Events to facilitate efficient and seamless data management
            -> Dashboard to manage staff details
        """
    },
    {
        "slug": "school-website",
        "image": "schoolwebsite.png",
        "project_image": ["schoolwebsite1.png", "schoolwebsite2.png"],
        "title": "School Website",
        "github_link": "https://github.com/SudeevDivakar/School-Website",
        "project_link": "https://sudeev-school-website.vercel.app/",
        "tech_used": ["ReactJS", "Tailwind CSS"],
        "api_used": None,
        "description": "Website for a school made using React.js and Tailwind CSS. First round assignment of the 'Madrocket Technologies & Media' internship.",
        "content": """
            School website providing a comprehensive platform to explore various aspects of the institution, catering to students, parents, and educators. This project was for the first round of the 'Madrocket Technologies & Media' internship selection round and was built using React.js and Tailwind CSS.
        """
    },
    {
        "slug": "arm-assembler",
        "image": "arm.png",
        "project_image": None,
        "title": "Arm Assembler",
        "github_link": "https://github.com/SudeevDivakar/ARM-Assembler",
        "project_link": None,
        "tech_used": ["Python"],
        "api_used": None,
        "description": "Assembler using python lex and yacc for subset of instructions of ARM v6",
        "content": """
            Assembler using python lex and yacc for subset of instructions of ARM v6

            Instructions Supported:
            
            ADC | ADD | AND | B | BIC | BL | BLX | BX | CLZ | CMN | CMP | EOR | LDM | LDR | LDRB | LDRH | MLA | MOV | MRS | MSR | MUL | MVN | ORR | RSB | RSC | SBC | SMULL | SMLAL | STM | STR | STRB | STRH | SUB | SWI | TEQ | TST | UMLAL | UMULL
        """
    },
    {
        "slug": "chat-application",
        "image": "chatapp.jpg",
        "project_image": ["chatapp1.png", "chatapp2.png"],
        "title": "Chat Application",
        "github_link": "https://github.com/SudeevDivakar/Chit-Chat-MERN-Stack-",
        "project_link": None,
        "tech_used": ["NodeJS", "React", "MongoDB", "Mongoose", "Express", "Chakra UI", "JWT"],
        "api_used": ["Cloudinary"],
        "description": "Chat Application made using ReactJS, MongoDB, Express, NodeJS, socket.io",
        "content":"""
            Chat Application made using ReactJS, MongoDB, Express, NodeJS, socket.io.

            Project Includes:
            -> Authentication using JWT
            -> One on One chatting
            -> Group Chatting
            -> Cloudinary API to store images
        """
    },
    {
        "slug": "twospoon-ai-frontend-assignment",
        "image": "twospoonai.png",
        "project_image": ["twospoonai1.png", "twospoonai2.png", "twospoonai3.png"],
        "title": "Twospoon.ai Frontend Assignment",
        "github_link": "https://github.com/SudeevDivakar/Twospoon.ai-Frontend-Assignment",
        "project_link": "https://sudeev-divakar-twospoonai-frontend.vercel.app/",
        "tech_used": ["React", "Tailwind CSS", "CSS"],
        "api_used": None,
        "description": "Frontend Web Development Assignment made using React and Tailwind CSS",
        "content":"""
            Frontend Web Development Assignment made using React and Tailwind CSS. Pinpoint recreation of a Figma Design provided by Twospoon.ai
        """
    },
    {
        "slug": "portfolio-website",
        "image": "portfolio.jpg",
        "project_image": None,
        "title": "Portfolio Website",
        "github_link": "https://github.com/SudeevDivakar/Portfolio-Website-Sudeev",
        "project_link": "https://sudeevdivakar-portfolio.vercel.app/",
        "tech_used": ["Django", "DTL", "HTML", "CSS"],
        "api_used": None,
        "description": "Portfolio website showcasing my projects, skill, achievements and knowledge",
        "content":"""
            Portfolio website showcasing my projects, skill, achievements and knowledge
        """
    },
]

"""End content for All Projects Page"""


"""Content for Index Page"""

resume_link = 'https://sudeevdivakar.github.io/SudeevDivakar_Resume.pdf'

top_three_projects = [ 
    {
        "slug": "spotify-playlist-generator",
        "image": "spotify.png",
        "project_image": ["spotify1.png", "spotify2.png", "spotify3.png", "spotify4.png"],
        "title": "Spotify Playlist Generator",
        "github_link": "https://github.com/SudeevDivakar/Spotify-Playlist-Generator",
        "project_link": None,
        "tech_used": ["ReactJS", "Tailwind CSS"],
        "api_used": ["Spotify API"],
        "description": "Spotify Playlist Generator made using React, Tailwind CSS and the Spotify API.",
        "content": """
            Spotify Playlist Generator made using React, Tailwind CSS and the Spotify API.

            Two Modes of Creating Playlists:
            -> Playlist Consisting of the Top Tracks of an Individual User's Top Artists.
            -> Playlist Consisting of the Top Tracks of Artists chosen by the user
        """
    },
    {
        "slug": "inventory-management-rabbitmq",
        "image": "invmanagement.png",
        "project_image": ["invmanagement1.jpeg", "invmanagement2.jpeg"],
        "title": "Microservice Inventory Management (RabbitMQ)",
        "github_link": "https://github.com/SudeevDivakar/Inventory_Management_Microservices-communication-using-RabbitMQ",
        "project_link": None,
        "tech_used": ["NodeJS", "RabbitMQ", "MongoDB", "Mongoose", "Express", "Docker"],
        "api_used": None,
        "description": "Backend Inventory Management System using Node JS. RabbitMQ used as a message broker and Docker used for containerization. MongoDB used as the database to store inventory data",
        "content":"""
            Backend Inventory Management System using Node JS. RabbitMQ used as a message broker and Docker used for containerization. MongoDB used as the database to store inventory data.

            The project is made up of a producer and four consumers. The producer sends messages to an exchange which then routes the messages in the appropriate queues. The queues connect to their respective consumers which all perform various database operations.

            -> Consumer_one : Performs a basic health check to see if the RabbitMQ server and it's components are running properly
            -> Consumer_two : Item Creation Microservice to create an item.
            -> Consumer_three : Stock Management Microservice to manage stock data in the MongoDB Database.
            -> Consumer_four : Order Processing Microservice to place/update orders and get order details. 
        """
    },
    {
        "slug": "turf-review",
        "image": "turfreview.jpeg",
        "project_image": ["turfreview1.png", "turfreview2.png"],
        "title": "Turf Review System",
        "github_link": "https://github.com/SudeevDivakar/Turf-Review-System",
        "project_link": "",
        "tech_used": ["NodeJS", "React", "MongoDB", "Mongoose", "Express", "Material UI", "JWT"],
        "api_used": ["Cloudinary", "OpenStreetMap"],
        "description": "A website to view and add football turfs, provide ratings, store user details, integrates map APIs and user authentication.",
        "content": """
            Turf Review System (AirBNB Clone) made using the MERN stack.

            Project Includes:
            -> Authentication using JWT.
            -> Features to Add Turfs, Delete Turfs, View Turfs, Login, Register and much more.
            -> Implements a cumulative rating system for turfs.
            -> Feature to leave comments/reviews on turfs.
            -> Stores Turf Images using the Cloudinary API.
            -> Visualize Turf Locations using the OpenStreetMap maps API. 
        """
    },
]

achievements = [
    {
        "image": "rv_football.jpg",
        "title": "Runners Up - Football",
        "description": "Secured Second Place in Football in JEET 2024 (RVU)"
    },
    {
        "image": "inter.jpg",
        "title": "Winners - Football",
        "description": "Secured First Place in Interdepartment Football 2024 (PESU)"
    },
]

"""End of content for index page"""


"""Content for the About Me Page"""

certifications = [
    {
        "certification": "The Web Developer Bootcamp 2024",
        "link": "https://www.udemy.com/certificate/UC-75f72636-151d-42c7-bc74-8e662b24211e/?utm_campaign=email&utm_medium=email&utm_source=sendgrid.com",
        "from": "Udemy",
        "date": "Jan 2024"
    },
    {
        "certification": "Python Django - The Practical Guide",
        "link": "https://www.udemy.com/certificate/UC-7c8cda12-71cc-4192-91ab-d52c95ff040b/",
        "from": "Udemy",
        "date": "Jul 2024"
    },
    {
        "certification": "50 Days of DSA Python Data Structures Algorithms LEETCODE",
        "link": "https://www.udemy.com/certificate/UC-f3798645-f677-4b33-bd7f-a11863c08bb3/?utm_campaign=email&utm_medium=email&utm_source=sendgrid.com",
        "from": "Udemy",
        "date": "Nov 2024"
    },
    {
        "certification": "Jira Work Management Fundamentals Badge",
        "link": "https://university.atlassian.com/student/award/fHUqC9HRyzwQ436EDKpUqQzK",
        "from": "Atlassian",
        "date": "Nov 2023"
    },
    {
        "certification": "The Git and Github Bootcamp",
        "link": "https://www.udemy.com/certificate/UC-60f9a0dc-49e8-4c55-9821-61a44828969f/?utm_medium=email&utm_campaign=email&utm_source=sendgrid.com",
        "from": "Udemy",
        "date": "Jul 2023"
    },
    {
        "certification": "AWS Skill Badges (AWS Educate)",
        "link": "https://www.credly.com/users/sudeev-divakar/badges",
        "from": "AWS Training and Certification",
        "date": "Jan 2024"
    }
]

domain_and_technologies = {
    "Languages": ["Javascript", "Python", "C", "Java" ],
    "Frontend Development": ["HTML", "CSS", "Tailwind CSS", "Bootstrap", "Chakra-UI", "Bulma", "Javascript", "React", "Material UI", "EJS", "DTL"],
    "Database/ORM/ODM": ["MongoDB", "MySQL", "SQLite", "Mongoose"],
    "Backend Development": ["NodeJS", "Express", "RabbitMQ", "Django", "Flask"],
    "Version Control": ["Git", "Github"],
    "DevOps": ["Docker", "Kubernetes"],
    "API and Testing": ["Postman", "Thunder Client"]
}

education = [
    {
        "institute" : "PES University",
        "year" : "2021 - 2025",
        "text" : "B.Tech-CSE",
        "link" : "https://pes.edu/"
    },  
    {
        "institute" : "Ekya Schools",
        "year" : "2019 - 2021",
        "text" : "11th & 12th Grade",
        "link" : "https://www.ekyaschools.com/itpl/"
    },
    {
        "institute" : "Ryan International School",
        "year" : "2009 - 2019",
        "text" : "1st-10th Grade",
        "link" : "https://www.ryangroup.org/ryaninternational/icse/bangalore/ryan-international-school-kundalahalli"
    },
]

work_experience = [
    {
        "company" : "Cuvasol Technologies Private Limited",
        "duration" : "June 2024 - August 2024 (2 months)",
        "position" : "Web Development Intern",
        "technologies" : ["HTML", "CSS", "PHP", "MySQL", "Postman"],
        "link": "https://www.cuvasol.com"
    },
    {
        "company" : "PES University",
        "duration" : "Sept 2024 - Dec 2024 (4 months)",
        "position" : "Teaching Assistant for Python",
        "technologies" : ["Python"],
        "link": "https://pes.edu/"
    }
]

"""End Content for the About Me Page"""

# Create your views here.
def index(request):
    return render(request, "portfolio/index.html", {
        "top_three_projects": top_three_projects,
        "achievements": achievements,
        "resume_link": resume_link
    })

def projects(request):
    return render(request, "portfolio/all-projects.html",{
        "all_projects": all_projects
    })

def single_project(request, slug):
    try:
        identified_project = next(project for project in all_projects if project['slug'] == slug)
        return render(request, "portfolio/single_project.html", {
            "project": identified_project
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

def about_me(request):
    return render(request, "portfolio/about-me.html", {
        "education": education,
        "work_experience": work_experience,
        "domain_and_technologies": domain_and_technologies,
        "certifications": certifications,
        "resume_link": resume_link
    })

def custom_404(request, exception):
    return render(request, "404.html", status=404)