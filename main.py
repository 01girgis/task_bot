# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from langchain.agents import create_csv_agent
from langchain.llms import  OpenAI
from dotenv import load_dotenv
import  os 

###load enviroment variables
load_dotenv()

def manin():
 #check the key 
 if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
 else:
        print("OPENAI_API_KEY is set")


###Gather Docs for langchain agent 
 docs = ["data/US_INDU_BALANCE_SHEET_STATEMENT.csv"]
###Set CSV Agent and Function Input Func.
 agent = create_csv_agent(OpenAI(temperature=0),docs,verbose = True)

 def answer_question(user_question: str) -> str: 
       agent.run(user_question)

# from langchain.text_splitter import RecursiveCharacterTextSplitter
# char_spliter  = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap = 0)
# chunk = char_spliter.create_documents(docs)
# ##print(len(chunk))

### data process loop
 while input != "quit()":
  user_input = input("Ask a question, Your AdvisorBot : ")
  response = answer_question(user_input)
  print(response)



if __name__ == "__main__" :
     manin()
