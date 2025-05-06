from flask import Flask, render_template, request
import os
from groq import Groq
import re

app = Flask(__name__, template_folder='templates')

# Set your Groq API key
os.environ['GROQ_API_KEY'] = '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'  # Replace this

client = Groq(api_key=os.environ['GROQ_API_KEY'])

prompt_template = (
    "Diet and Workout Recommendation System:\n"
    "Based on the following details, provide recommendations under the following labeled sections:\n\n"
    "1. Restaurants (6 names)\n"
    "2. Breakfast options (6 items)\n"
    "3. Dinner options (5 items)\n"
    "4. Workouts (6 exercises)\n\n"
    "User Details:\n"
    "- Age: {age}\n"
    "- Gender: {gender}\n"
    "- Weight: {weight} kg\n"
    "- Height: {height} cm\n"
    "- Diet Type: {veg_or_nonveg}\n"
    "- Disease: {disease}\n"
    "- Region: {region}\n"
    "- Allergies: {allergics}\n"
    "- Food Type: {foodtype}\n\n"
    "Respond in the format:\n"
    "Restaurants:\n1.\n2.\n...\n\n"
    "Breakfast:\n1.\n2.\n...\n\n"
    "Dinner:\n1.\n2.\n...\n\n"
    "Workouts:\n1.\n2.\n...\n"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    form = request.form

    prompt = prompt_template.format(
        age=form['age'],
        gender=form['gender'],
        weight=form['weight'],
        height=form['height'],
        veg_or_nonveg=form['veg_or_nonveg'],
        disease=form['disease'],
        region=form['region'],
        allergics=form['allergics'],
        foodtype=form['foodtype']
    )

    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1024
    )

    result = response.choices[0].message.content

    # Extract sections using regex
    restaurant_names = re.findall(r'Restaurants:\s*(.*?)\n\n', result, re.DOTALL)
    breakfast_names = re.findall(r'Breakfast:\s*(.*?)\n\n', result, re.DOTALL)
    dinner_names = re.findall(r'Dinner:\s*(.*?)\n\n', result, re.DOTALL)
    workout_names = re.findall(r'Workouts:\s*(.*?)$', result, re.DOTALL)

    def clean(text_block):
        return [x.strip('-• \n') for x in text_block[0].splitlines() if x.strip()] if text_block else []

    return render_template(
        'result.html',
        restaurant_names=clean(restaurant_names),
        breakfast_names=clean(breakfast_names),
        dinner_names=clean(dinner_names),
        workout_names=clean(workout_names)
    )

if __name__ == '__main__':
    app.run(debug=True)
