import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Customer Support FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Customer Support FAQ Chatbot")
st.write("Welcome! Type your question below to receive immediate automated support.")

# FAQ data
faq_data = {
    "track package": "You can track your package using the tracking link sent to your registered email or phone number.",
    "return": "You can request a return within 7 days of delivery.",
    "refund": "Refunds are generally processed within 5–7 business days.",
    "cancel order": "You can cancel your order before it is shipped.",
    "payment": "We accept credit cards, debit cards, UPI and other supported payment methods.",
    "delivery": "Standard delivery usually takes 3–7 business days.",
    "contact": "You can contact customer support through email or phone during business hours."
}

# Function to generate chatbot response
def get_bot_response(user_query, faq_data):
    user_query = user_query.lower()

    for keyword, response in faq_data.items():
        if keyword in user_query:
            return response

    return (
        "Sorry, I couldn't understand your question. 🤔\n\n"
        "You can ask about:\n"
        "- 📦 Package tracking\n"
        "- 🔄 Returns\n"
        "- 💰 Refunds\n"
        "- ❌ Order cancellation\n"
        "- 💳 Payment\n"
        "- 🚚 Delivery\n"
        "- 📞 Customer support"
    )

# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get new user input
if user_query := st.chat_input(
    "Ask a question (e.g., How do I track my package?)"
):

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_query)

    st.session_state.messages.append({
        "role": "user",
        "content": user_query
    })

    # Generate bot response
    bot_reply = get_bot_response(user_query, faq_data)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()