import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Nutrition Adviser AI",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.main{
    padding-top:1rem;
}
.stButton>button{
    width:100%;
    background:#2E8B57;
    color:white;
    border-radius:10px;
    height:3em;
    font-size:18px;
}
.stButton>button:hover{
    background:#256f46;
}

.question-box{
    background:#f5f7fa;
    padding:15px;
    border-radius:12px;
    border-left:5px solid #2E8B57;
    color:black;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

.feature{
    background:#f8f9fc;
    padding:15px;
    border-radius:10px;
    box-shadow:0px 2px 5px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1046/1046857.png",
        width=120
    )

    st.title("🥗 Nutrition Adviser")

    st.markdown("---")

    st.subheader("Example Questions")

    st.info("""
• Fiber rich foods

• Weight loss diet

• Foods for diabetes

• Heart healthy meals

• Protein rich vegetarian foods

• Vitamin D deficiency

• Sports nutrition

• Mediterranean diet
""")

    st.markdown("---")

    st.success("Powered by Llama 3.1 + Groq")

# ------------------ HEADER ------------------

st.title("🍲 Nutrition Adviser AI Chatbot")

st.write(
    """
Welcome! 👋

Ask me anything related to:

✅ Healthy Eating

✅ Weight Management

✅ Vitamins & Minerals

✅ Diabetes Nutrition

✅ Heart Health

✅ Sports Nutrition

✅ Specialized Diets

✅ Meal Planning
"""
)

# ------------------ FEATURE CARDS ------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="feature">
<h4>🥦 Nutrition Guidance</h4>
Personalized nutrition explanations.
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="feature">
<h4>❤️ Healthy Lifestyle</h4>
Heart, diabetes and immunity tips.
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="feature">
<h4>🏃 Fitness Nutrition</h4>
Protein, muscle gain and sports nutrition.
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------ USER INPUT ------------------

question = st.text_area(
    "💬 Enter your nutrition question",
    placeholder="Example: Suggest a high-protein vegetarian diet..."
)

# ------------------ PROMPT ------------------

prompt = ChatPromptTemplate.from_template("""
You are an expert Nutrition and Diet Advisor.

Your task is to answer ONLY nutrition-related questions.

Allowed topics:
- Macronutrients
- Micronutrients
- Fiber
- Cardiovascular Health
- Metabolic Disorders
- Inflammation and Immunity
- Specialized Diets
- Sports Nutrition
- Life-Span Nutrition
- Sustainable Nutrition
- Food Labels
- Global Malnutrition
- Healthy Eating
- Weight Management
- Meal Planning

If the question is NOT related to nutrition, reply:

"Sorry, I can only answer nutrition related questions."

Question:
{question}

Provide your answer in the following format:

🥗 Explanation

📌 Step-by-Step Guidance

✅ Best Practices

⚠ Precautions (if necessary)

🍽 Sample Food Suggestions (if applicable)

Keep the answer simple and beginner friendly.
""")

# ------------------ BUTTON ------------------

if st.button("🚀 Ask Nutrition AI"):

    if question.strip() == "":
        st.warning("Please enter a nutrition question.")

    else:

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.3
        )

        chain = prompt | llm

        with st.spinner("🥗 Thinking..."):

            response = chain.invoke({"question": question})

        st.success("Answer Generated Successfully!")

        st.markdown("## 🤖 AI Response")

        st.markdown(
            f"""
<div class="question-box">

{response.content.replace(chr(10), "<br>")}

</div>
""",
            unsafe_allow_html=True,
        )

# ------------------ DISCLAIMER ------------------

st.divider()

st.info(
    """
**Disclaimer**

This chatbot provides general nutrition information and should not replace
professional medical advice. Consult a registered dietitian or healthcare
provider for personalized recommendations.
"""
)

# ------------------ FOOTER ------------------

st.markdown(
"""
<div class="footer">

Made with ❤️ using Streamlit • LangChain • Groq • Llama 3.1

</div>
""",
unsafe_allow_html=True
)