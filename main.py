import openai
import json

def gpt3(q_text):
    # This is where you open the file for your API key which created in '.json' format
    with open("OPENAI_KEY.json") as f:
        data = json.load(f)

    openai.api_key = data["API_KEY"]
    res = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=q_text,
        temperature=0.1,
        max_tokens=25,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return res.choices[0].text.split("\n")

answer=list()

while True:
    query = input("Ask Your Question: ")
    answer=gpt3(query)
    # this code below helps us to keep the each answer unique instead of being repeated words
    answer = list(dict.fromkeys(answer))
    for line in answer:
        if (("exit-status" not in line.lower()) and ("-status" not in line.lower())) and (line != "\n") and line.count("-") < 3:
            print(line)
    # exits the program(not case sensitive)
    if query.lower() == "exit":
        print("You have exited from program")
        break
