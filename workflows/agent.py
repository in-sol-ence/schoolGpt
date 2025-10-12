import langgraph
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langgraph.chains.router import ConditionalRouter, Route

load_dotenv()

llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL"), temperature=os.getenv("OPENAI_TEMPERATURE"), api_key=os.getenv("OPENAI_KEY"))

def main(state):
    