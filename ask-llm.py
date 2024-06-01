#!/usr/bin/env python3

import os
import json
import urllib.request
import time

LLM_API_BASE_URL = os.environ.get("LLM_API_BASE_URL", "https://api.groq.com/openai/v1")
LLM_API_KEY = os.environ.get("LLM_API_KEY") or os.environ.get("GROQ_API_KEY")
LLM_CHAT_MODEL = os.environ.get("LLM_CHAT_MODEL", "mixtral-8x7b-32768")

LLM_STREAMING = os.environ.get("LLM_STREAMING", "yes") != "no"

MAX_TOKENS = int(os.environ.get("LLM_MAX_TOKENS", 12000))
# SEED = int(os.environ.get("LLM_SEED")) # problème si j'active je connais pas la valeur pour retourner à void pour que ce soit de nouveau random
TEMPERATURE = float(os.environ.get("LLM_TEMPERATURE", 0))
SYSTEM_PROMPT = os.environ.get("LLM_SYSTEM_PROMPT")

LLM_DEBUG = os.environ.get("LLM_DEBUG")

def chat(messages):
    url = f"{LLM_API_BASE_URL}/chat/completions"
    auth_header = f"Bearer {LLM_API_KEY}" if LLM_API_KEY else None
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "python-requests/2.31.0",
    }
    if auth_header:
        headers["Authorization"] = auth_header
    body = {
        "messages": messages,
        "model": LLM_CHAT_MODEL,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
		"response_format": {
			"type": "text"
		},
	    "top_p": 0.1, # ne change rien, peut-être car mode json ?
		"frequency_penalty": 0, # ne change rien, peut-être car mode json ?
		"presence_penalty": 1, # ne change rien, peut-être car mode json ?
		#"seed": 123, # problème si j'active je connais pas la valeur pour retourner à void pour que ce soit de nouveau random
    }
    json_body = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(url, data=json_body, headers=headers, method="POST")
    response = urllib.request.urlopen(request)
    if response.status != 200:
        raise Exception(f"HTTP error: {response.status} {response.reason}")
    data = json.loads(response.read().decode("utf-8"))
    choices = data["choices"]
    first = choices[0]
    message = first["message"]
    content = message["content"]
    answer = content.strip()
    return answer

def main():
    # print(f"Using {LLM_CHAT_MODEL} LLM at {LLM_API_BASE_URL}.")
    # print("Don't abuse please.")
    # print()

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            question = input("")
        except EOFError:
            break

        messages.append({"role": "user", "content": question})
        start = time.time()
        answer = chat(messages)
        messages.append({"role": "assistant", "content": answer})
        print(answer)
        elapsed = time.time() - start
        if LLM_DEBUG:
            print(f"[{round(elapsed * 1000)} ms]")
        print()


if __name__ == "__main__":
    main()
