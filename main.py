from agent import chooseTool
import ollama

systemPrompt = "You are a helpful math agent that uses calculator tools"

while True:

    userInput = input("\nUser: ")

    if userInput.lower() in ["exit","quit", "q", "cancel"]:
        break
    
    result = chooseTool(userInput)

    print("Agent:", result)