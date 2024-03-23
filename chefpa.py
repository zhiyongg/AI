import streamlit as st



def send_message():
    user_message = st.session_state.user_message
    st.session_state.history.append(f"<div style='text-align: right;'><b>You 🧑</b></div>")
    st.session_state.history.append(
        f"<div class='user_message' style='text-align: right; color: white; '>{user_message}</div>")

    

    # Bot's response
    bot_response = "hello"
    st.session_state.history.append(f"<div><b>🤖 Chef Pa</b></div>")
    st.session_state.history.append(f"<div class= bot_message style='text-align: left;  color: black;'> {bot_response}</div>")

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
        margin-bottom: 50px; /* Add some space below the title */
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

# Create the form for user input
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

