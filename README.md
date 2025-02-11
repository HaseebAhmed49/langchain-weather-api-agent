# AI-Powered Weather Aggregator

## 📌 Project Overview
The **AI-Powered Weather Aggregator** that combines the capabilities of FastAPI, LangChain, and Streamlit to provide real-time weather information using an AI agent. The application fetches weather data from the OpenWeatherMap API and uses LangChain for intelligent querying. The backend is built with FastAPI, and the frontend is built using Streamlit.

---
## Project Structure

```sh
langchain-weather-api-agent/
│── backend/  
│   ├── main.py       # FastAPI backend with LangChain  
│   ├── .env          # API keys 
│── frontend/  
│   ├── app.py        # Streamlit frontend 
│── requirements.txt  # Dependencies  
│── README.md         # Project documentation
```

---
## Technologies Used
* **FastAPI** for backend API
* **Streamlit** for frontend UI
* **LangChain** for AI-based responses
* **OpenAI** for using with LangChain

---
## 📌 Prerequisites
Ensure you have the following installed on your system:
- **Python 3.13+**
- **pip** (Python package manager)

---
## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/haseebahmed49/langchain-weather-api-agent.git
cd langchain-weather-api-agent
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the backend directory and add your OpenAI/OpenWeatherMap API key:
```sh
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
echo "WEATHER_API_KEY=your_weather_api_key_here" > .env
```

---
## 🖥 Backend (FastAPI)

### 📌 Start the FastAPI Server
Run the backend using:
```sh
uvicorn backend.main:app --reload
```
The API will be available at `http://127.0.0.1`.
## Backend (FastAPI) - main.py

### Functionality:
- Uses FastAPI to create an API that fetches weather data from OpenWeatherMap.
- Calls OpenAI's model via LangChain for summary of the weather.
- Handles weather datails filtering by location.

### API Endpoints:
#### 1. Fetch News Articles
**Get/weather** - Fetches weather details based on the location provided.

---
## 🎨 Frontend (Streamlit)

### 📌 Run the Streamlit App
```sh
streamlit run app.py
```

### Functionality:
- Accepts user input for location.
- Calls the FastAPI backend to fetch weather details for the location.
- Displays a summary of weather.

### Key Features:
- Interactive UI with Streamlit.
- Real-time weather fetching based on user input.
- Error handling for API failures.

---
## Application View


## 📜 License
This project is licensed under the MIT License.

---
## Contact
For any queries or issues, feel free to reach out:
* Email: haseebahmed02@gmail.com
* GitHub: https://github.com/HaseebAhmed49

💡 **Happy Coding!** 🚀

