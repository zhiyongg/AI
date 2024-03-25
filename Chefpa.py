import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["hi "]
    },
    {
        "role": "model",
        "parts": ["Hello there! I am Chef Pa how can I assist you today?"]
    },
    {
        "role": "user",
        "parts": ["call me "]
    },
    {
        "role": "model",
        "parts": ["Hello, I am Chef Pa you can ask me anything about cooking."]
    },
    {
        "role": "user",
        "parts": ["Teach me cook lamb chop"]
    },

    {
        "role": "model",
        "parts": [
            "**Ingredients:**\n\n* 1 rack of lamb (about 8 chops)\n* 1 tablespoon olive oil\n* 1 teaspoon dried rosemary\n* 1 teaspoon dried thyme\n* 1/2 teaspoon salt\n* 1/4 teaspoon black pepper\n\n**Instructions:**\n\n1. Preheat oven to 400 degrees F (200 degrees C).\n2. In a small bowl, combine the olive oil, rosemary, thyme, salt, and pepper.\n3. Season the lamb chops generously with the herb mixture.\n4. Place the lamb chops on a baking sheet lined with parchment paper.\n5. Roast for 15-20 minutes, or until cooked to your desired doneness.\n6. Let the lamb chops rest for 5 minutes before serving.\n\n**Tips:**\n\n* For a more flavorful chop, marinate the lamb in the herb mixture for at least 30 minutes before roasting.\n* To check for doneness, insert a meat thermometer into the thickest part of the chop. The internal temperature should be 125 degrees F (52 degrees C) for rare, 135 degrees F (57 degrees C) for medium-rare, or 145 degrees F (63 degrees C) for medium.\n* Lamb chops can also be cooked on the grill. Preheat the grill to medium-high heat and cook the chops for 3-4 minutes per side, or until cooked to your desired doneness.\n* Serve the lamb chops with your favorite sides, such as mashed potatoes, roasted vegetables, or a green salad."]
    },
    {
        "role": "user",
        "parts": ["I don't have olive oil what can I use instead"]
    },
    {
        "role": "model",
        "parts": [
            "You can substitute any other type of cooking oil for olive oil in this recipe. Some good options include:\n\n* Avocado oil\n* Vegetable oil\n* Canola oil\n* Grapeseed oil\n* Sunflower oil\n\nYou can also use melted butter or ghee instead of oil.\n\nIf you are using a different type of oil, you may want to adjust the amount slightly. For example, if you are using avocado oil, which is a very flavorful oil, you may want to use a little less than you would olive oil.\n\nHere is the recipe with the substitution:\n\n**Ingredients:**\n\n* 1 rack of lamb (about 8 chops)\n* 1 tablespoon cooking oil (such as avocado oil, vegetable oil, canola oil, grapeseed oil, sunflower oil, melted butter, or ghee)\n* 1 teaspoon dried rosemary\n* 1 teaspoon dried thyme\n* 1/2 teaspoon salt\n* 1/4 teaspoon black pepper\n\n**Instructions:**\n\n1. Preheat oven to 400 degrees F (200 degrees C).\n2. In a small bowl, combine the cooking oil, rosemary, thyme, salt, and pepper.\n3. Season the lamb chops generously with the herb mixture.\n4. Place the lamb chops on a baking sheet lined with parchment paper.\n5. Roast for 15-20 minutes, or until cooked to your desired doneness.\n6. Let the lamb chops rest for 5 minutes before serving.\n\nEnjoy!"]
    }, {
        "role": "user",
        "parts": ["Who are you "]
    },
    {
        "role": "model",
        "parts": ["I am Chef Pa, a cooking chat bot, develop by someone mystery."]
    },
])


def send_message():
    user_message = st.session_state.user_message
    st.session_state.history.append(f"<div style='text-align: right;'><b>You 🧑</b></div>")
    st.session_state.history.append(
        f"<div class='user_message' style='text-align: right; color: white; '>{user_message}</div>")

    convo.send_message(user_message)

    # Bots response
    bot_response = convo.last.text
    st.session_state.history.append(f"<div><b>🤖 Chef Pa</b></div>")
    st.session_state.history.append(
        f"<div class= bot_message style='text-align: left;  color: black;'> {bot_response}</div>")

    # Clear the text input box
    st.session_state.user_message = ""


# Initialize conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Apply custom CSS styles
st.markdown(
    """
<style>
    
    .stTextInput > div > div > input {
        background-color: white;
        border-color: #515D59;
        border-radius: 5px;
        padding: 10px;
    }

    .user_message, .bot_message {
        max-width: fit-content;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        word-wrap: break-word;
    }

    .user_message {
        background-color: #DC8F7D;
        margin-right:20px;
        margin-left: auto;
    }

    .bot_message {
        background-color:#F1C6B3;
        margin-right:200px;
        margin-left: 20px;
      
    }
    
    .title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 50px; 
        background-color:#4F4A46;
   
    }
</style>


<div class="title-container" >
    <h1 style="color: white;">Welcome to Chef PA 👨‍🍳</h1>
</div>


    """,
    unsafe_allow_html=True
)

# Display conversation history
for chat in st.session_state.history:
    st.markdown(chat, unsafe_allow_html=True)  # Allow HTML rendering

# Create the form for user input  and button
with st.form("chat-form"):
    column = st.columns((6, 1))
    column[0].text_input("Chat",
                         value=st.session_state.get("user_message", ""),  # Set initial value
                         key="user_message",
                         label_visibility="collapsed")
    column[1].form_submit_button(
        "▶",
        type="primary",
        on_click=send_message  # Attach the event handler to the button
    )
