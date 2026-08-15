import argparse
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt

load_dotenv()  # pyright: ignore[reportUnusedCallResult]
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("environment variable not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="toy agent")
parser.add_argument("user_prompt", type=str, help="User prompt")  # pyright: ignore[reportUnusedCallResult]
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")  # pyright: ignore[reportUnusedCallResult]
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},  # pyright: ignore[reportAny]
]

for _ in range(20):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,  # pyright: ignore[reportArgumentType]
        temperature=0,
        tools=available_functions,  # pyright: ignore[reportArgumentType]
    )

    if response.usage is not None:
        if args.verbose:  # pyright: ignore[reportAny]
            print(f"User prompt: {args.user_prompt}")  # pyright: ignore[reportAny]
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("possible failed API request")
    message = response.choices[0].message
    messages.append(message)
    if message.tool_calls is not None:
        for tool_call in message.tool_calls:
            if tool_call.type == "function":
                result_message = call_function(tool_call)
                if not result_message["content"]:
                    raise Exception("tool content empty")
                if args.verbose:
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
    else:
        print(message.content)
        break
else:
    print("maximum attemps reached, sorry")
    sys.exit(1)
