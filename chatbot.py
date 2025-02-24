import pandas as pd
import ollama
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load Titanic dataset
df = pd.read_csv("titanic.csv")

# Initialize Ollama LLM
llm = Ollama(model="llama2")

# Define prompt template
prompt = PromptTemplate(
    input_variables=["question", "data"],
    template="""
    You are an AI assistant with Titanic dataset knowledge.
    Answer the user's question using the dataset:
    {question}
    Data:
    {data}
    """
)

# Create chain
chain = LLMChain(llm=llm, prompt=prompt)

def ask_question(question):
    """Processes user question and returns AI response."""
    data_sample = df.head(10).to_string()  # Sending a small sample for context
    response = chain.run(question=question, data=data_sample)
    return response