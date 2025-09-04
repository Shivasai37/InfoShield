import streamlit as st
import openai

# Set up page
st.set_page_config(page_title="InfoShield - Fake News Detector", layout="wide")
st.title("🛡️ InfoShield - AI Powered Misinformation Detector")
st.markdown("Check if news or claims are trustworthy using AI ⚡")

# 🔑 Enter API Key (you can also set it as an environment variable)
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# User input
user_input = st.text_area("Paste a news article, claim, or statement:", height=200)

if st.button("🔍 Check Credibility"):
    if api_key.strip() == "":
        st.error("⚠️ Please enter your OpenAI API key.")
    elif user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        try:
            openai.api_key = api_key

            # Prompt for GPT
            prompt = f"""
            Analyze the following text for misinformation:
            - Provide a credibility score (0–100%)
            - Explain why it is credible or suspicious
            - Suggest 2–3 reference sources (if available)

            Text:
            {user_input}
            """

            response = openai.ChatCompletion.create(
                model="gpt-4.1",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )

            ai_output = response["choices"][0]["message"]["content"]

            st.subheader("📊 AI Analysis")
            st.write(ai_output)

        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown("---")
st.caption("⚡ Prototype powered by OpenAI GPT-4.1")
