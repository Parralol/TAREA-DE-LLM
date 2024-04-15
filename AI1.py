from langchain.chains import LLMChain
#from langchain.llms import OpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

import os

os.environ["OPENAI_API_KEY"] = "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"



template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What is at the core of Popper's theory of science?"

response = llm_chain.invoke(question)
print(response)