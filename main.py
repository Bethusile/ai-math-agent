from agent import chooseTool, runLLM
import ollama

systemPrompt = "You are a helpful math agent that uses calculator tools and speaks like a clown"

while True:

    userInput = input("\nYou: ")

    if userInput.lower() in ["exit","quit", "q", "cancel"]:
        break
    if not userInput:
        break

    operation = runLLM(userInput)

    print("LLM decided: ", operation)
        
    result = chooseTool(userInput, operation)

    print("Bot:", result)