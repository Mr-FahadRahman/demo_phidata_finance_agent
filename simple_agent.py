from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile")
    model=Groq(id="deepseek-r1-distill-llama-70b")
)

agent.print_response("Write a short poem for the love of my life.")