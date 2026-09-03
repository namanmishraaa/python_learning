from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
from agent_output import myOutputFormat

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries suing chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enought PLAN had been done, finally you can give an OUTPUT.
    You can also call the tools if required from the list of available tools.
    For every tool call wait for the tool_result step which is the output from the called tool.

    Rules:
    - Stictly follwo the give JSON output format.
    - Only run one step at a time.
    - The swqucen of steps in START (Where user give an input), PLAN (That can be multiple times) 
    and finally OUTPUT (Which is going to the diplayed to the user).

    OUTPUT JSON Format:
    {
     "step": "START" | "PLAN" | "TOOL_CALL" | "TOOL_CALL" | "TOOL_RESULT",
     "content":"string"
    }

    Available Tools:
    - get_weather(city:str) : Take city name as an input string and returns the weather info about the city.

    Example_1:

        START: Hey, can you solve 2+3*5/10
        PLAN: {"step": "PLAN", "content" : "User is interested in math problem"}
        PLAN: {"step": "PLAN", "content" : "Looking at the problem, we should sovle this using BODMAS method"}  
        PLAN: {"step": "PLAN", "content" : "Yes, BODMAS is the correct thing to be done here."}
        PLAN: {"step": "PLAN", "content" : "First we multiply 3 * 5 which is 15"}
        PLAN: {"step": "PLAN", "content" : "Now the new equation is 2+ 15 / 10"}
        PLAN: {"step": "PLAN", "content" : "We must perform division of 15 / 10 which is 1.5"}
        PLAN: {"step": "PLAN", "content" : "Now the new equation is 2 + 1.5"}
        PLAN: {"step": "PLAN", "content" : Now we must add 2 + 1.5 which is 3.5"}
        OUTPUT: Here is the output of 2+3*5/10=3.5

    Example_2 :
    
        START: Hey, what is the weather of delhi?
        PLAN: {"step": "PLAN", "content" : "Seems like user is interested in getting the weather of Delhi, India"}
        PLAN: {"step": "PLAN", "content" : "Let's see if there is any available tools"}  
        PLAN: {"step": "PLAN", "content" : "Great we have get_weather tool avaialbe for this query"}
        PLAN: {"step": "PLAN", "content" : "I need to call get_weather tool as Delhi as input for city"}
        TOOL_CALL: {"step": "TOOL_CALL", "tool": "get_weather', "input" : "delhi"}
        TOOL_RESULT: {"step": "TOOL_RESULT", "tool": "get_weather', "content" : "Partly Cloudy  +27°C"}
        PLAN: {"step": "PLAN", "content" : "We got the result from tool_call for delhi now let me struture it."}
        OUTPUT: Weather in Delhi, India is pleasent with cloud and temp is +27°C


"""


def get_weather(city:str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"Weather in {city} is {response.text}"

    return f"Something went wrong {response.status_code}"

def llm_call(message):

    response = client.responses.parse(
        model = 'gpt-4o-mini',
        input = message,
        text_format = myOutputFormat
    )
    return response


AVAILABLE_TOOLS = {
    "get_weather" : get_weather
}

def agent_invoke(message:str):

    messages = [
            {"role" : "system", "content" : SYSTEM_PROMPT},
            {"role" : "user", "content" : message}
    ]
    while True:
        try:
                # Call the model with the FULL history (messages)
                response = llm_call(messages)
                
                # Parse the JSON response
                response_text = response.output_text.strip()
                data = json.loads(response_text)

                if data.get("content"):
                    if data.get("step") == 'START' : print("🔥", end = ' ')
                    if data.get("step") == 'PLAN' : print("🧠", end = ' ')
                    if data.get("step") == 'TOOL_CALL' : 
                        print("⚒️", end = ' ')
                        # tool_to_call = data.get("tool")
                        # tool_input = data.get("input")
                        # tool_result = AVAILABLE_TOOLS[tool_to_call](tool_input)
                        # messages.append({
                        #     "role" : "developer",
                        #     "content" : json.dumps(
                        #         {
                        #             "step" : "TOOL_RESULT",
                        #             "tool" : tool_to_call,
                        #             "input" : tool_input,
                        #             "output" : tool_result
                        #         }
                        #     )
                        # })
                        # continue
                    if data.get("step") == 'OUTPUT' : print("🤖", end = ' ')
                    print(data.get("content"))


                if data.get("step") == 'TOOL_CALL':
                    tool_to_call = data.get("tool")
                    tool_input = data.get("input")
                    tool_result = AVAILABLE_TOOLS[tool_to_call](tool_input)
                    messages.append({
                        "role" : "developer",
                        "content" : json.dumps(
                            {
                                "step" : "TOOL_RESULT",
                                "tool" : tool_to_call,
                                "input" : tool_input,
                                "output" : tool_result
                            }
                        )
                    })
                    continue


                # Add the AI's response to the history so it remembers what it planned
                messages.append({
                    "role": "assistant",
                    "content": json.dumps(data)
                })

                # Check if we should stop
                if data['step'] == "OUTPUT":
                    print("\nFinal Result Received!")
                    break
        
                # # Wait to avoid 429 Rate Limit errors
                # print("...waiting 10 seconds for next step...")
                # time.sleep(30)
        

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    print(messages)





def main(): 

    message = input("> ")
    agent_invoke(message=message)
    # print(f'🤖 {llm_response.output_text}')


if __name__ == "__main__":
    main()