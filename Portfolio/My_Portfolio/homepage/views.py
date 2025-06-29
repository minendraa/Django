from django.shortcuts import render


# Example static data in your views.py or directly in the template context

projects = [
    {
        "title": "Predictive Data Modeling with Python",
        "description": "A project that uses machine learning algorithms to predict house prices based on historical data in Streamlit.",
        "image": "/static/images/house_price.png",  
        "technologies": ["Python", "Scikit-learn", "Pandas", "NumPy","Streamlit"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day4/streamlit_house_prediction.py",
        # "live_url": "https://student.github.io/house-price-prediction"
    },
    {
        "title": "Image Prediction Cat and Dog Classifier",
        "description": "A project that determines whether the given photo is dog or cat.",
        "image": "/static/images/dogcat.png",  
        "technologies": ["Kaggle", "CNN", 'TensorFlow',"Keras"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/image_predict/cat_vs_dog_classification.ipynb",
        # "live_url": "https://student.github.io/genai-text-generator"
    },
    {
        "title": "Django project on Library Management System",
        "description": "A Django-based Library Management System that allows users to manage books, update book details, register and log in as members, and keep track of book availability and transactions.",
        "image": "/static/images/library.jpg",  
        "technologies": ["Python", "Django", "HTML", "CSS"],
        "github_url": "https://github.com/minendraa/Django/tree/main/library_management",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {
        "title": "Streamlit project on Salary Prediction System",
        "description": "A streamlit project that allows predicts an employee's salary based on their age, gender, education level, and years of experience using a pre-trained machine learning model.",
        "image": "/static/images/salary.png",  
        "technologies": ["Python", "Streamlit", "Joblib", "Numpy"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day4/streamlit_for_salary_prediction.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {
        "title": "Amazon Review Star Rating Predictor using Tkinter and Machine Learning",
        "description": "A tkinter based project that allows using Tkinter that loads a trained sentiment rating model and vectorizer to predict Amazon-style review ratings (out of 5 stars) based on user-entered review text.",
        "image": "/static/images/musicreview2.png",  
        "technologies": ["Tkinter", "Scikit-learn", "Joblib", "MLPClassifier",'Vectorization','EventHandling','InputValidation'],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day7/mlpclassifier/tkinter_for_mlp.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {
        "title": "Streamlit project on Employee Attrition Prediction System",
        "description": "This Streamlit app predicts employee attrition based on various input features using a pre-trained machine learning model, with data preprocessing, model inference, and result visualization.",
        "image": "/static/images/attrition.png",  
        "technologies": ["Pandas", "Streamlit", "Joblib", "Scikit-learn",'Machine Learning'],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day5/streamlit_for_employee_attrition.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {
        "title": "Tkinter project on Email Spam Detection",
        "description": "This code creates a simple email spam detection application with a graphical user interface (GUI) using Tkinter, where users can input email content, and the model predicts whether the message is spam or not.",
        "image": "/static/images/spam.png",  
        "technologies": ["Pandas",'Tkinter', "CountVectorizer", "Joblib", "Scikit-learn",'Machine Learning'],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day6/email_detection_gui.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {
        "title": "Streamlit-Based Sentiment Analysis App for Musical Instrument Reviews",
        "description": "This Python script uses Streamlit to build an interactive web application that loads a pre-trained multilayer perceptron (MLP) sentiment analysis model and a CountVectorizer, allowing users to input or select musical instrument reviews and receive sentiment predictions (Positive, Negative, or Neutral) along with visual feedback using emojis.",
        "image": "/static/images/musicreview.png",  
        "technologies": ["Streamlit", "Pandas", "Joblib", "CountVectorizer", "MLPClassifier", "Scikit-learn", "Machine Learning", "Text Vectorization", "Model Inference", "User Interface", "Conditional Logic", "Python Functions"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day7/featureengineeringimplemented/Streamlit_implemented_for_sentiment_analysis.py",
        # "live_url": "https://student.github.io/prompt-engineering-chatbot"
    },
    {
        "title": "Insurance Charges Predictor Using Linear Regression and Streamlit",
        "description": "This Streamlit app trains a Linear Regression model on a preprocessed insurance dataset to predict medical charges based on user input (age, BMI, smoker status, region, and number of children) and displays both the predicted charges and model performance metrics.",
        "image": "/static/images/insurance.png",  
        "technologies": ["Streamlit", "Pandas", "NumPy", "ModelTraining", "TrainTestSplit", "MeanAbsoluteError", "MeanSquaredError", "R2Score", "LabelEncoding"],
        "github_url": "https://github.com/minendraa/Machine-Learning-/blob/main/day2/insurance_gui.py",
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
