import streamlit as st
import joblib
import base64

# Load vectorizer and model
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('lr_model.jb')

# Function to load and encode the image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your image file
image_file = "images/photo.jpg"  
base64_image = get_base64_image(image_file)

# Add background image using custom CSS
st.markdown(
    f"""
    <style>
    body {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover; /* Ensures the image fits the screen */
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
    }}
    .stApp {{
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white for readability */
        border-radius: 10px;
        padding: 15px;  /* Reduced padding for a smaller box */
        width: 30%; /* Smaller box width */
        margin-left: 50px; /* Move box to the left */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        color: black; /* Changes the text color to black */
        font-family: Arial, sans-serif; /* Optional: Sets a clean font */
    }}
    .stButton, .stTextArea {{
        width: 100%; /* Makes button and text area fit inside the smaller box */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title and Description
st.markdown(
    """
    <div style="background-color:#1f77b4;padding:10px;border-radius:10px;text-align:center;">
        <h1 style="color:white;">📰 Fake News Detector 🕵️‍♂️</h1>
    </div>
    """, 
    unsafe_allow_html=True
)
st.write(
    """
    Welcome to the **Fake News Detector App**!  
    Enter a news article below, and our AI will determine if it’s **Fake** or **Real**.  
    """
)

# News Input
st.markdown("### 📝 Enter the News Article:")
news_input = st.text_area('Type or paste the article here...', "")

# Analyze Button
if st.button('🔍 Check News'):
    if news_input.strip():
        try:
            # Transform input and predict
            transform_input = vectorizer.transform([news_input])
            prediction = model.predict(transform_input)

            # Display results
            if prediction[0] == 1:
                st.success("🟢 **The News is Real!**")
                st.balloons()
            else:
                st.error("🔴 **The News is Fake!**")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please enter some text to analyze.")

# Footer
st.markdown(
    """
    <hr>
    <div style="text-align:center;">
        Made with ❤️ by J Priyanka
    </div>
    """, 
    unsafe_allow_html=True
)
