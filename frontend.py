import streamlit as st



def predict_news(sentence):
    import requests
    api_url = "http://9c16-35-225-18-94.ngrok-free.app/upload"

    data = {'sentence': sentence}
    print("api call")
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        result = response.json()  # Assuming the server responds with JSON data
        return result
    else:
        return f"Error: {response.status_code}"


st.title("App")

# Input Box
sentence = st.text_input("Enter a sentence:")


print("start")

# Submit Button
if st.button("Submit"):
    if sentence:
        result = predict_news(sentence)
        st.write(f"Sentiment: {result}")
    else:
        st.warning("Please enter a sentence.")
