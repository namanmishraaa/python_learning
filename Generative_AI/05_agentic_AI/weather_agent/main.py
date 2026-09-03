from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI()

def get_weather(city:str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"Weather in {city} is {response.text}"

    return "Something went wrong {response.status_code}"

def agent_call(message:str):
    response = client.responses.create(
        model = 'gpt-4o-mini',
        input = message
    )
    return response


def main(): 

    message = input("> ")
    llm_response = agent_call(message=message)
    print(f'🤖 {llm_response.output_text}')


if __name__ == "__main__":
    main()




"""
Here is the sample response of response =
Response(
    id='resp_05bc8d794bff49eb006a99a4e46fbc87d2bb21c7e0ace2f9ae',
 created_at=1788454116.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='gpt-4o-mini-2024-07-18', object='response', output=[ResponseOutputMessage(id='msg_05bc8d794bff49eb006a99a4e5cecc87d2aaf6e3935be8a8fa', content=[ResponseOutputText(annotations=[], text="I'm here and ready to help! How about you?", type='output_text', logprobs=[])], role='assistant', status='completed', type='message', phase=None)], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[], top_p=1.0, background=False, completed_at=1788454117.0, conversation=None, max_output_tokens=None, max_tool_calls=None, moderation=None, previous_response_id=None, prompt=None, prompt_cache_key=None, prompt_cache_options=None, prompt_cache_retention='in_memory', reasoning=Reasoning(context=None, effort=None, generate_summary=None, mode=None, summary=None), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=13, input_tokens_details=InputTokensDetails(cache_write_tokens=0, cached_tokens=0), output_tokens=12, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=25, compute_units=None), user=None, billing={'payer': 'developer'}, frequency_penalty=0.0, presence_penalty=0.0, store=True, tool_usage={'image_gen': {'input_tokens': 0, 'input_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'output_tokens': 0, 'output_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'total_tokens': 0}, 'web_search': {'num_requests': 0}})

"""