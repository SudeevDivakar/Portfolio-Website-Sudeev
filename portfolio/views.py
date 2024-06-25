from datetime import date

from django.shortcuts import render

all_projects = [
    {
        "slug": "turf-review",
        "image": "turfreview.jpeg",
        "title": "Turf Review System",
        "github-link": "https://github.com/SudeevDivakar/Turf-Review-System",
        "project-link": "https://turfreview.vercel.app/",
        "tech-used": ["NodeJS", "React", "MongoDB", "Mongoose", "Express", "Material UI", "JWT"],
        "api-used": ["Cloudinary", "Leaflet"],
        "description": "TurfReview is a comprehensive system for reviewing and exploring turf locations. Whether you're a sports enthusiast, event planner, or someone looking for the perfect turf for your activities, TurfReview has you covered",
        "content": """
          
        """
    },
    {
        "slug": "parking-manager",
        "image": "parkingmanager.jpg",
        "title": "Parking Lot Manager",
        "github-link": "https://github.com/SudeevDivakar/Parking_Management_System",
        "project-link": None,
        "tech-used": ["NodeJS", "EJS", "MySQL", "Express", "Bulma"],
        "api-used": None,
        "description": "The Parking Management System is a comprehensive solution designed to efficiently manage and streamline parking operations in various settings, such as commercial complexes, residential areas, and public spaces",
        "content": """
          
        """
    },
    {
        "slug": "arm-assembler",
        "image": "arm.png",
        "title": "Arm Assembler",
        "github-link": "https://github.com/SudeevDivakar/ARM-Assembler",
        "project-link": None,
        "tech-used": ["Python"],
        "api-used": None,
        "description": "Assembler using python lex and yacc for subset of instructions of ARM v6",
        "content": """
          
        """
    },
    {
        "slug": "chat-application",
        "image": "chatapp.jpg",
        "title": "Chat Application",
        "github-link": "https://github.com/SudeevDivakar/Chit-Chat-MERN-Stack-",
        "project-link": None,
        "tech-used": ["NodeJS", "React", "MongoDB", "Mongoose", "Express", "Chakra UI", "JWT"],
        "api-used": None,
        "description": "Chit Chat is a versatile and user-friendly real-time messaging application designed to facilitate seamless communication between individuals and groups",
        "content":"""

        """
    },
    {
        "slug": "inventory-management-rabbitmq",
        "image": "invmanagement.png",
        "title": "Microservice Inventory Management (RabbitMQ)",
        "github-link": "https://github.com/SudeevDivakar/Inventory_Management_Microservices-communication-using-RabbitMQ",
        "project-link": None,
        "tech-used": ["NodeJS", "RabbitMQ", "MongoDB", "Mongoose", "Express", "Docker"],
        "api-used": None,
        "description": "Backend Inventory Management System using Node JS. RabbitMQ used as a message broker and Docker used for containerization. MongoDB used as the database to store inventory data",
        "content":"""

        """
    },
    {
        "slug": "user-teams-manager",
        "image": "heliverse.jpeg",
        "title": "User & Teams Manager",
        "github-link": "https://github.com/SudeevDivakar/User-Teams-Manager-Heliverse",
        "project-link": None,
        "tech-used": ["NodeJS", "React", "MongoDB", "Mongoose", "Express", "Material UI"],
        "api-used": None,
        "description": "Full Stack Web Development Assessment for the Heliverse Internship Round :D",
        "content":"""

        """
    }
]


"""Content for the About Me Page"""

certifications = [
    {
        "certification": "The Web Developer Bootcamp 2024",
        "link": "https://www.udemy.com/certificate/UC-75f72636-151d-42c7-bc74-8e662b24211e/?utm_campaign=email&utm_medium=email&utm_source=sendgrid.com",
        "from": "Udemy",
        "date": "Jan 2024"
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
    "Frontend Development": ["HTML", "CSS", "Bootstrap", "Chakra-UI", "Bulma", "Javascript", "React", "Material UI", "EJS", "DTL"],
    "Database/ORM/ODM": ["MongoDB", "MySQL", "Mongoose"],
    "Backend Development": ["NodeJS", "Express", "Django", "Flask"],
    "Version Control": ["Git", "Github"],
    "DevOps": ["Docker", "Kubernetes"],
    "API and Testing": ["Postman", "Thunder Client"]
}

education = [
    {
        "institute" : "Ryan International School",
        "year" : "2009 - 2019",
        "text" : "1st-10th Grade",
        "link" : "https://www.ryangroup.org/ryaninternational/icse/bangalore/ryan-international-school-kundalahalli"
    },
    {
        "institute" : "Ekya Schools",
        "year" : "2019 - 2021",
        "text" : "11th & 12th Grade",
        "link" : "https://www.ekyaschools.com/itpl/"
    },
    {
        "institute" : "PES University",
        "year" : "2021 - 2025",
        "text" : "B.Tech-CSE",
        "link" : "https://pes.edu/"
    }
]

work_experience = [
    {
        "company" : "Cuvasol Technologies Private Limited",
        "duration" : "June 2024 - August 2024 (2 months)",
        "position" : "Backend Web Development Intern",
        "technologies" : ["HTML", "CSS", "PHP", "MySQL", "Postman"],
        "link": "https://www.cuvasol.com"
    }
]

"""End Content for the About Me Page"""

# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")

def projects(request):
    return render(request, "portfolio/all-projects.html",{
        "all_projects": all_projects
    })

def specific_project(request, slug):
    identified_project = next(project for project in all_projects if project['slug'] == slug)
    return render(request, "portfolio/single-project.html", {
        "project": identified_project
    })

def about_me(request):
    return render(request, "portfolio/about-me.html", {
        "education": education,
        "work_experience": work_experience,
        "domain_and_technologies": domain_and_technologies,
        "certifications": certifications
    })