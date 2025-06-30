from django.shortcuts import render


# Example static data in your views.py or directly in the template context

projects = [
    {   #1
        "title": "Predictive Data Modeling with Python",
        "description": "A project that uses machine learning algorithms to predict house prices based on historical data in Streamlit.",
        "image": "/static/images/house_price.png",  
        "technologies": ["Python", "Scikit-learn", "Pandas", "NumPy","Streamlit"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day4/streamlit_house_prediction.py",
        # "live_url": "https://student.github.io/house-price-prediction"
    },
    {   #2
        "title": "Image Prediction Cat and Dog Classifier",
        "description": "A project that determines whether the given photo is dog or cat.",
        "image": "/static/images/dogcat.png",  
        "technologies": ["Kaggle", "CNN", 'TensorFlow',"Keras"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/image_predict/cat_vs_dog_classification.ipynb",
        # "live_url": "https://student.github.io/genai-text-generator"
    },
    {   #3
        "title": "Django project on Library Management System",
        "description": "A Django-based Library Management System that allows users to manage books, update book details, register and log in as members, and keep track of book availability and transactions.",
        "image": "/static/images/library.jpg",  
        "technologies": ["Python", "Django", "HTML", "CSS"],
        "github_url": "https://github.com/minendraa/Django/tree/main/library_management",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #4
        "title": "Streamlit project on Salary Prediction System",
        "description": "A streamlit project that allows predicts an employee's salary based on their age, gender, education level, and years of experience using a pre-trained machine learning model.",
        "image": "/static/images/salary.png",  
        "technologies": ["Python", "Streamlit", "Joblib", "Numpy"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day4/streamlit_for_salary_prediction.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #5
        "title": "Email Sending API using FastAPI and Gmail SMTP",
        "description": "A RESTful API built with FastAPI that enables sending emails through Gmail's SMTP server using structured request data validated by Pydantic.",
        "image": "/static/images/emailfastapi.png",  
        "technologies": ["Python", "FastAPI", "SMTP", "Gmail SMTP Server",'smtplib','HTTPException','EmailMessage'],
        "github_url": "https://github.com/minendraa/emailsender/blob/main/spammain.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #6
        "title": "Amazon Review Star Rating Predictor using Tkinter and Machine Learning",
        "description": "A tkinter based project that allows using Tkinter that loads a trained sentiment rating model and vectorizer to predict Amazon-style review ratings (out of 5 stars) based on user-entered review text.",
        "image": "/static/images/musicreview2.png",  
        "technologies": ["Tkinter", "Scikit-learn", "Joblib", "MLPClassifier",'Vectorization','EventHandling','InputValidation'],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day7/mlpclassifier/tkinter_for_mlp.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #7
        "title": "Streamlit project on Employee Attrition Prediction System",
        "description": "This Streamlit app predicts employee attrition based on various input features using a pre-trained machine learning model, with data preprocessing, model inference, and result visualization.",
        "image": "/static/images/attrition.png",  
        "technologies": ["Pandas", "Streamlit", "Joblib", "Scikit-learn",'Machine Learning'],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day5/streamlit_for_employee_attrition.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #8
        "title": "Tkinter project on Email Spam Detection",
        "description": "This code creates a simple email spam detection application with a graphical user interface (GUI) using Tkinter, where users can input email content, and the model predicts whether the message is spam or not.",
        "image": "/static/images/spam.png",  
        "technologies": ["Pandas",'Tkinter', "CountVectorizer", "Joblib", "Scikit-learn",'Machine Learning'],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day6/email_detection_gui.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #9
        "title": "Django project on Student Management System",
        "description": "A Django-based Student Management System that allows users to add, view, and delete student records, including details like name, date of birth, average marks, and email address.",
        "image": "/static/images/djangostudent.png",  
        "technologies": ["Python",'Django', "SQLite Database", "Templates", "CRUD Operations"],
        "github_url": "https://github.com/minendraa/Django/tree/main/Student_record/Student_record",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #10
        "title": "Streamlit-Based Sentiment Analysis App for Musical Instrument Reviews",
        "description": "This Python script uses Streamlit to build an interactive web application that loads a pre-trained multilayer perceptron (MLP) sentiment analysis model and a CountVectorizer, allowing users to input or select musical instrument reviews and receive sentiment predictions (Positive, Negative, or Neutral) along with visual feedback using emojis.",
        "image": "/static/images/musicreview.png",  
        "technologies": ["Streamlit", "Pandas", "Joblib", "CountVectorizer", "MLPClassifier", "Scikit-learn", "Machine Learning", "Text Vectorization", "Model Inference", "User Interface", "Conditional Logic", "Python Functions"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day7/featureengineeringimplemented/Streamlit_implemented_for_sentiment_analysis.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   
        #11
        "title": "Django project on Teacher Management System",
        "description": "A Django-based Teacher Management System that allows users to add, view, and delete teacher records, including details like name, date of join, Salary, email address.",
        "image": "/static/images/djangoteacher.png",  
        "technologies": ["Python",'Django', "SQLite Database", "Templates", "CRUD Operations"],
        "github_url": "https://github.com/minendraa/Django/tree/main/Student_record/Teacher_record",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #12
        "title": "Insurance Charges Predictor Using Linear Regression and Streamlit",
        "description": "This Streamlit app trains a Linear Regression model on a preprocessed insurance dataset to predict medical charges based on user input (age, BMI, smoker status, region, and number of children) and displays both the predicted charges and model performance metrics.",
        "image": "/static/images/insurance.png",  
        "technologies": ["Streamlit", "Pandas", "NumPy", "ModelTraining", "TrainTestSplit", "MeanAbsoluteError", "MeanSquaredError", "R2Score", "LabelEncoding"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day2/insurance_gui.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #13
        "title": "Formula 1 Reaction Time Simulator using Python",
        "description": "A reflex-testing desktop game that simulates F1 race start lights and measures a user's reaction time to the green light using Python's Tkinter GUI.",
        "image": "/static/images/f1.png",  
        "technologies": ["Python", "Tkinter", "Time Module", "Multithreading", "Random Delays",'Real-time Feedback'],
        "github_url": "https://github.com/minendraa/Data-Visualization-Analysis/blob/main/day1/parking_gui.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #14
        "title": "Smart Parking Management System using Python GUI",
        "description": "A desktop-based application to manage vehicle parking with real-time logging, parking capacity tracking, and log filtering using a graphical user interface built with Tkinter.",
        "image": "/static/images/parking.png",  
        "technologies": ["Python", "Tkinter", "Datetime Module", "User Input Validation", "OOP"],
        "github_url": "https://github.com/minendraa/Data-Visualization-Analysis/blob/main/day2/f1.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #15
        "title": "Rock, Paper, Scissors Game with Streamlit",
        "description": "A simple web-based Rock, Paper, Scissors game built with Streamlit where users play against the computer and instantly see the result of each round.",
        "image": "/static/images/rps.png",  
        "technologies": ["Python", "Streamlit", "Random Module", "User Input"],
        "github_url": "https://github.com/minendraa/My-Python/blob/main/week12/day2/rps_gui.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #16
        "title": "Number Guessing Game with Streamlit",
        "description": "A fun web-based number guessing game built using Streamlit, where users try to guess a randomly chosen number between 1 and 20 with feedback and attempt tracking.",
        "image": "/static/images/guess.png",  
        "technologies": ["Python", "Streamlit", "Random Module", "Interactive UI"],
        "github_url": "https://github.com/minendraa/My-Python/blob/main/week12/day2/guessnumbergame.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #17
        "title": "Password Validator & Strength Checker using Streamlit",
        "description": "A secure web app built with Streamlit that validates a password against best practices (length, character types) and provides a strength assessment along with confirmation matching.",
        "image": "/static/images/password.png",  
        "technologies": ["Python", "Streamlit", "Password Validation Logic", "User Feedback"],
        "github_url": "https://github.com/minendraa/My-Python/blob/main/week12/day6/guipassword.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #18
        "title": "Bank Account Management App with OOP & Streamlit",
        "description": "A simple interactive banking application built using Streamlit and Python's object-oriented principles, allowing users to create an account, deposit, withdraw, and explore encapsulation.",
        "image": "/static/images/app.png",  
        "technologies": ["Python", "Streamlit", "OOP", "Encapsulation",'Interactive Widgets'],
        "github_url": "https://github.com/minendraa/My-Python/blob/main/week12/day7/app.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #19
        "title": "Library Management System with Streamlit",
        "description": "An interactive Streamlit app to manage a library’s collection that supports adding, borrowing, returning, deleting, and viewing books with real-time updates.",
        "image": "/static/images/library2.png",  
        "technologies": ["Python", "Streamlit", "OOP", "Looping",'CRUD'],
        "github_url": "https://github.com/minendraa/My-Python/blob/main/week12/day8/gui_library.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {   #20
        "title": "Even/Odd Number Counter using Tkinter",
        "description": "A simple GUI application built with Tkinter that accepts 10 user-entered numbers and displays the count of even and odd numbers upon completion.",
        "image": "/static/images/evenoddcounter.png",  
        "technologies": ["Python", "Tkinter", "List Data", "Input Validation"],
        "github_url": "https://github.com/minendraa/My-Python/blob/main/week12/day3/gui_evenodd.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
]

def viewmore(request):
    return render(request,'homepage/viewmore.html',{'projects': projects})


# Create your views here.
def index(request):
    return render(request,'homepage/index.html', {'projects': projects[:3]})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail  # Optional for sending email

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Do something with the data: save to DB, send email, etc.
        print(f"Message from {name} ({email}): {message}")
        
        return HttpResponse("Thank you for contacting me!")
    
    return redirect('home')  # redirect if someone opens the form directly
