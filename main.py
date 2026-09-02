from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")
# Create the OpenAI chat model through LangChain
model = ChatOpenAI(model="gpt-4o-mini")

chain = prompt | model | StrOutputParser()

# This run is automatically recorded in LangSmith.
response = chain.invoke({"topic": "Tell me a fun fact about Tamil Nadu."})
print(response)