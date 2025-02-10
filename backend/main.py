from fastapi import FastAPI
import requests
from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Required for LangChain's agent
app = FastAPI()

# Function to fetch weather data
def get_weather(city: str):
    api_key = WEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "temperature": f"{data['main']['temp']}°C",
            "weather": data['weather'][0]['description'],
            "humidity": f"{data['main']['humidity']}%",
            "wind_speed": f"{data['wind']['speed']} m/s"
        }
    return {"error": "Unable to fetch weather data."}

# Define the LangChain Tool
weather_tool = Tool(
    name="Weather API",
    func=get_weather,
    description="Fetches real-time weather data for a given city."
)

# Initialize LangChain Agent
llm = OpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)
agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

@app.get("/weather/{city}")
def fetch_weather(city: str):
    """Uses LangChain agent to fetch weather data for a city"""
    response = agent.run(f"What is the weather like in {city}?")
    return {"city": city, "response": response}