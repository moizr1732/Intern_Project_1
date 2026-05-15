import random

# Global variable to remember the last topic
last_topic = None

def analyze_input(user_input):
    """Analyze user input and return appropriate response"""
    global last_topic
    user_input = user_input.lower().strip()
    
    # Check for exit command
    if user_input in ["exit", "quit", "bye", "goodbye"]:
        return "exit"
    
    # Contextual responses - "tell me more" about previous topic
    if any(phrase in user_input for phrase in ["tell me more", "more about", "continue", "elaborate"]) and last_topic:
        return get_contextual_response(last_topic)
    
    # Topic tracking and responses
    if "python" in user_input:
        last_topic = "python"
        return "Python is great for data and AI! It's versatile and has amazing libraries."
    
    elif "javascript" in user_input or "js" in user_input:
        last_topic = "javascript"
        return "JavaScript powers the web! From frontend to backend with Node.js."
    
    elif "machine learning" in user_input or "ml" in user_input:
        last_topic = "machine learning"
        return "Machine learning is fascinating! It's about teaching computers to learn from data."
    
    elif "data science" in user_input:
        last_topic = "data science"
        return "Data science combines statistics, programming, and domain expertise to extract insights!"
    
    elif "web development" in user_input:
        last_topic = "web development"
        return "Web development involves creating websites and web applications. Frontend, backend, and databases!"
    
    # Data Analyst Mode - Structured insights
    elif "data analysis" in user_input or "data analyst" in user_input:
        last_topic = "data analysis"
        return """Data Analysis Steps:
1. Data Cleaning
2. Data Exploration  
3. Visualization
4. Insights"""
    
    elif "data" in user_input and "cleaning" in user_input:
        last_topic = "data cleaning"
        return """Data Cleaning Process:
• Handle missing values
• Remove duplicates
• Fix inconsistent formats
• Validate data quality"""
    
    elif "visualization" in user_input or "charts" in user_input:
        last_topic = "visualization"
        return """Data Visualization Types:
• Bar charts - Compare categories
• Line charts - Show trends
• Scatter plots - Relationships
• Histograms - Distribution"""
    
    # Greeting responses
    if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
        return random.choice([
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Greetings! How may I assist you?"
        ])
    
    # Thanks responses
    if any(word in user_input for word in ["thank", "thanks", "appreciate"]):
        return random.choice([
            "You're welcome!",
            "No problem!",
            "Happy to help!"
        ])
    
    # Help responses
    if any(word in user_input for word in ["help", "what can you do"]):
        return "As a data analyst, I can help with Python, JavaScript, machine learning, data science, data analysis, and visualization. Ask me about anything or say 'tell me more' for detailed insights!"
    
    # Default responses
    return random.choice([
        "I'm not sure I understand. Could you rephrase that?",
        "That's interesting. Tell me more.",
        "I'm processing what you said. Can you elaborate?"
    ])

def get_contextual_response(topic):
    """Provide contextual response based on the last topic"""
    responses = {
        "python": [
            "Python's syntax is clean and readable, making it perfect for beginners. Popular libraries include NumPy, Pandas, and TensorFlow!",
            "Did you know Python was created by Guido van Rossum in 1991? It's named after Monty Python!",
            "Python excels in AI/ML, web development (Django/Flask), data analysis, and automation. What aspect interests you most?"
        ],
        "javascript": [
            "JavaScript is event-driven and supports multiple paradigms. Modern frameworks like React and Vue make frontend development amazing!",
            "Node.js lets you run JavaScript on the server side. Full-stack JavaScript development is very popular!",
            "ES6+ features like arrow functions, destructuring, and async/await make modern JavaScript powerful and elegant."
        ],
        "machine learning": [
            "ML includes supervised learning, unsupervised learning, and reinforcement learning. Each has different use cases!",
            "Popular ML algorithms include linear regression, decision trees, neural networks, and support vector machines.",
            "Python libraries like scikit-learn, TensorFlow, and PyTorch make ML accessible to everyone!"
        ],
        "data science": [
            "Data science workflow: data collection → cleaning → exploration → modeling → visualization → communication.",
            "Key tools: Python (Pandas, NumPy), R, SQL, Tableau, and machine learning libraries.",
            "Data scientists need skills in statistics, programming, business acumen, and communication!"
        ],
        "web development": [
            "Frontend: HTML, CSS, JavaScript. Backend: Node.js, Python, Ruby, PHP. Databases: SQL and NoSQL options.",
            "Modern web dev uses frameworks like React, Angular, Vue for frontend and Express, Django, Flask for backend.",
            "Responsive design, performance optimization, and security are crucial aspects of web development!"
        ],
        "data analysis": [
            """Data Analysis Workflow:
1. Define Objectives
2. Collect Data
3. Clean & Preprocess
4. Exploratory Analysis
5. Statistical Testing
6. Visualize Results
7. Generate Insights""",
            """Key Data Analysis Tools:
• Python: Pandas, NumPy, Matplotlib
• R: ggplot2, dplyr
• SQL: Database queries
• Excel: Pivot tables, formulas""",
            """Data Quality Checks:
• Completeness: Missing values
• Accuracy: Correct values
• Consistency: Uniform format
• Timeliness: Current data"""
        ],
        "data cleaning": [
            """Missing Data Strategies:
• Delete rows with missing values
• Impute with mean/median/mode
• Forward/backward fill
• Predictive imputation""",
            """Outlier Detection:
• Statistical methods (Z-score, IQR)
• Visual inspection (box plots)
• Domain knowledge validation
• Automated detection algorithms""",
            """Data Validation Rules:
• Range checks (min/max values)
• Format validation (dates, emails)
• Uniqueness constraints
• Referential integrity"""
        ],
        "visualization": [
            """Choosing the Right Chart:
• Comparison: Bar, Column charts
• Trend: Line, Area charts
• Distribution: Histogram, Box plot
• Relationship: Scatter, Bubble charts""",
            """Visualization Best Practices:
• Clear titles and labels
• Appropriate color schemes
• Consistent scaling
• Remove chart junk""",
            """Advanced Visualizations:
• Heatmaps for correlations
• Treemaps for hierarchies
• Sankey for flows
• Geospatial maps"""
        ]
    }
    
    if topic in responses:
        return random.choice(responses[topic])
    else:
        return f"Here's more about {topic}: It's an interesting topic with many aspects to explore!"
