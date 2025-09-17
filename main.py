
import os
import openai
from dotenv import load_dotenv

def loaddot():
	load_dotenv()
	return os.getenv("API_KEY")

def chat_with_gpt(prompt, model="gpt-4.1"):
	api_key = loaddot()
	if not api_key:
		raise ValueError("OPENAI_API_KEY not found in .env")
	openai.api_key = api_key
	response = openai.ChatCompletion.create(
		model=model,
		messages=[{"role": "user", "content": prompt}]
	)
	return response.choices[0].message["content"]

def main():
	while True:
		prompt = input("You: ")
		if prompt.lower() in ["exit", "quit", "q"]:
			print("Goodbye!")
			break
		try:
			reply = chat_with_gpt(prompt)
			print(f"GPT: {reply}")
		except Exception as e:
			print(f"Error: {e}")

if __name__ == "__main__":
	main()
