import openai
import pandas as pd
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI
import os
from dotenv import load_dotenv

load_dotenv() 

def main():
 # check the key 
 if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
 else:
        print("OPENAI_API_KEY is set")

# reading csv files
 data1 = pd.read_csv('data/US_INDU_CALCULATIONS.csv')
 data2 = pd.read_csv('data/US_INDU_INCOME_STATEMENT.csv')

#  merging the required files by outer order
 df = pd.merge(data1, data2,  
                   on=['name','fiscal_year'], 
                   how='outer')

# set dataframe for financial factuals
 df = df[['name','fiscal_year','netincome','totalrevenue','pricetoearnings','dividendyield','roe']]

# filter data  by 2022
 df_f = df[(df['fiscal_year'] == 2022)]
 #print(df_f.head(30)) #test

 
 
 def answer_question(user_question: str) -> str: 
  llm = OpenAI(api_token=openai.api_key)
  pandas_ai = PandasAI(llm)
  print(pandas_ai(df_f, prompt= user_question+" with  financial advise"))
  #(Test)print(pandas_ai(df_f, prompt='What is Total Revenue of Home Depot Inc 2022?'))
  #(Test)prompt = f" What is return on equity of walmart inc  2022? in {df_f} and financial calculation advise"
  #(Test)
#   prompt = f" {user_question} in {df_f} and financial calculation advise"
#   response = openai.Completion.create(
#      engine="text-davinci-003",
#      prompt=prompt,
#      temperature=0,
#      max_tokens=100
#     )
#   print(response.choices[0].text.strip())

# data process loop
 while True:
  user_input = input("Ask a question, Your AdvisorBot : ")
  #bot terminate method
  if user_input == "exit":
        break
  answer_question(user_input)


if __name__ == "__main__" :
     main()