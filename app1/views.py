# assistant/views.py

from django.shortcuts import render
from django.http import JsonResponse
import random

# Optional: Uncomment if integrating Wikipedia
import wikipedia

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Doing well, how about you?", "I'm fine, and you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!","Bubbye"],
    "what is data analytics": [
        "Data analytics involves examining datasets to draw conclusions about the information they contain.",
        "It is the process of analyzing raw data to find trends and answer questions.",
        "Data analytics helps organizations make data-driven decisions."
    ],
    "tools used in data analytics": [
        "Some popular tools are Excel, SQL, Python, R, and Tableau.",
        "Data analysts often use tools like Power BI, SAS, and Google Analytics.",
        "Common tools include Jupyter Notebooks, Pandas, and Matplotlib for Python."
    ],
    "what is data science": [
        "Data science is a multidisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from data.",
        "It combines aspects of statistics, computer science, and domain expertise to analyze data.",
        "Data science involves data mining, machine learning, and big data analytics."
    ],
    "difference between data analytics and data science": [
        "Data analytics focuses on interpreting existing data, while data science involves creating algorithms and models to predict future outcomes.",
        "Data science is broader and includes data analytics as one of its components.",
        "Data analytics is more about processing and interpreting data, whereas data science involves building models and algorithms to understand complex data patterns."
    ],
    "skills needed for data analytics": [
        "Key skills include proficiency in Excel, SQL, and data visualization tools like Tableau.",
        "A good data analyst should know statistical analysis, data cleaning, and have strong critical thinking abilities.",
        "Experience with Python or R, and knowledge of databases, is also important."
    ],
    "skills needed for data science": [
        "A data scientist should be skilled in machine learning, programming (Python, R), and statistics.",
        "Strong mathematical skills, understanding of algorithms, and experience with big data tools like Hadoop or Spark are essential.",
        "Communication skills are also important to explain complex models to non-technical stakeholders."
    ],
    "what is machine learning": [
        "Machine learning is a branch of artificial intelligence that focuses on building systems that can learn from data.",
        "It involves training algorithms to recognize patterns and make predictions or decisions without being explicitly programmed for each task.",
        "Machine learning is a key component of data science and is used for tasks like classification, regression, and clustering."
    ],
    "examples of data science projects": [
        "Predicting customer churn using historical data and machine learning.",
        "Building a recommendation system for an e-commerce platform.",
        "Analyzing social media data to understand public sentiment about a product or brand."
    ],
    "who created you":[
        "I was created by, my master, Kesav Deepak Sridharan"
    ],
    "what is electrical energy consumption prediction": [
        "It refers to the process of forecasting future electricity usage based on historical consumption data, weather patterns, economic factors, and other relevant variables."
    ],
    
    "why is electrical energy consumption prediction important": [
        "Accurate prediction helps in energy management, reducing costs, optimizing power generation, and ensuring a balanced demand-supply ratio in the electrical grid.",
        "It also supports the integration of renewable energy sources."
    ],
    
    "what data is needed for electrical energy consumption prediction": [
        "Historical electricity consumption records.",
        "Weather data (temperature, humidity, etc.).",
        "Economic indicators.",
        "Holiday information.",
        "Time-related features (seasonality, day of the week).",
        "Other relevant variables."
    ],
    
    "what techniques are used for predicting electrical energy consumption": [
        "Machine learning models (example- linear regression, decision trees, support vector machines).",
        "Time series analysis (example- ARIMA, SARIMA).",
        "Deep learning models (example- LSTM, GRU)."
    ],
    
    "what are the challenges in predicting electrical energy consumption": [
        "Data quality and availability.",
        "Handling seasonality and sudden spikes in usage.",
        "Accounting for irregular events (e.g., holidays, power outages).",
        "Integrating renewable energy sources into the prediction models."
    ],
    "who are you":[
        "I am, Electro",
        "I am an chatbot used for this project"
    ],
    "what is your purpose":[
        "My purpose is to assist users with their queries related to electrical energy consumption prediction.",
        "I can provide information on the topic, including data requirements, techniques used, and challenges faced"
    ],
    "what is your limitation":[
        "My limitation is that I am a chatbot and do not have the ability to access external sources"
    ],
    "what is your goal":[
        "My goal is to assist users with their queries related to electrical energy consumption prediction"
    ],
    "what is your name":[
        "My name is Electro"
    ],
    "explain this dashboard":[
        "This dashboard is used to display the insights of the electrical energy consumption prediction model. It includes"

    ]
    
    
    

    
    
}

def home(request):
    return render(request, 'assistant/home.html')
def dash(request):
    return render(request,"assistant/dashboard.html")
def process_query(request):
    if request.method == 'POST':
        query = request.POST.get('query', '').lower()
        if not query:
            return JsonResponse({'response': "Please provide a valid query."})
        
        response = handle_query(query)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def handle_query(query):
    if 'wikipedia' in query:
        topic = query.replace("wikipedia", "").strip()
        if not topic:
            return "Please specify a topic to search on Wikipedia."
        try:
            summary = wikipedia.summary(topic, sentences=3)
            return f"According to Wikipedia: {summary}"
        except wikipedia.exceptions.DisambiguationError:
            return f"The topic '{topic}' is ambiguous. Please be more specific."
        except wikipedia.exceptions.PageError:
            return f"No Wikipedia page found for '{topic}'."
        except Exception as e:
            return "An error occurred while searching Wikipedia."

    elif 'the time' in query or 'what time' in query:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    elif 'good' in query :
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        if( now >="06:00:00"):
            return "Good Morning"
        elif(now >="12:00:00"):
            return "Good Afternoon"
        else:
            return "Good evening"
    else:
        # Handle predefined responses
        for key in responses:
            if key in query:
                return random.choice(responses[key])
        return "Sorry, I don't understand."
    
def homep(request):
    return render(request,"assistant/index.html")

import pickle
from django.shortcuts import render
import numpy as np
from math import sin, cos, pi

# Load the saved model
with open('final_gb_model (1).pkl', 'rb') as f:
    model = pickle.load(f)

# Define a view for handling predictions
def predict(request):
    if request.method == 'POST':
        # Get input data from the form (assuming it has three features for simplicity)
        
        input_data = [
            float(request.POST['feature1']),
            float(request.POST['feature2']),
            float(request.POST['feature3']),
            float(request.POST['feature4']),
            float(request.POST['feature5']),
            int(request.POST['feature6']),
            int(request.POST['feature7']),
            int(request.POST['feature8']),
            int(request.POST['feature9']),
            int(request.POST['feature10']),
        ]
        
        # Reshape the input and make predictions
        prediction = model.predict(np.array(input_data).reshape(1, -1))
        
        return render(request, 'assistant/result.html', {'prediction': prediction[0]})

    return render(request, 'assistant/predict.html')

