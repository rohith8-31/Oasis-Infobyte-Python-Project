# Oasis-Infobyte-Python-Project

# Oasis Infobyte Python Project

Hey there! Welcome to my repository! I put this together to showcase three Python projects I built during my Oasis Infobyte internship. They’re all command-line tools—nothing fancy, just good, solid stuff that works. I’ve organized everything neatly, and below you’ll find all the details about what I made.

---

## BMI Calculator
- **What It Does**: This one’s a simple tool to figure out your Body Mass Index (BMI). You enter your weight in kilograms and height in meters, and it calculates your BMI, then tells you if you’re Underweight, Normal, Overweight, or Obese.
- **How It Works**:
  - Prompts you for your weight and height.
  - Uses the formula: BMI = weight divided by height squared.
  - Checks your BMI against these ranges:
    - Underweight: below 18.5
    - Normal: 18.5 to 24.9
    - Overweight: 25 to 29.9
    - Obese: 30 or above
  - I added some checks so it won’t freak out if you type something odd, like a negative number.
- **How to Run It**: Just run the script with Python and follow the on-screen instructions!
---

## Random Password Generator
- **What It Does**: This tool whips up a random password for you. You decide how long it should be and whether you want letters, numbers, or symbols in it, and it’ll create something unique every time.
- **How It Works**:
  - Asks you how many characters you want and what to include (letters? numbers? symbols?).
  - Mixes it all up randomly and hands you a password.
  - I made sure it only accepts sensible inputs, like a positive length.
- **How to Run It**: Run the script with Python and answer the questions it asks—easy as that!
---

## Basic Weather App
- **What It Does**: This is my take on a weather checker. You type in a city name, and it pulls up the current weather—like the temperature, humidity, and what’s happening outside (sunny, cloudy, etc.)—using an API.
- **How It Works**:
  - You give it a city name (like “London” or “Mumbai”).
  - It connects to OpenWeatherMap and shows you the basics: temperature in Celsius, humidity, and a quick weather description.
  - If something goes wrong—like a typo in the city name—it’ll let you know instead of crashing.
- **How to Run It**:
  1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)—they’ll give you one after you register.
  2. Open the script in a text editor, find where it says `YOUR_API_KEY`, and replace it with your key.
  3. Run it with Python and type in a city when it asks.
- **Extras**: You’ll need the `requests` library (install it with `pip install requests`) and an internet connection.

---

## What You’ll Need
- Python 3 (any recent version should be fine).
- For the weather app, grab the `requests` library with `pip install requests`.

## Getting Started
Want to give them a spin? Here’s how:
1. Download or clone this repo to your computer.
2. Pick a project, open its folder, and run the script with Python.
3. Follow the instructions each one gives you.

I really enjoyed working on these during my internship and am excited to share them with you!
