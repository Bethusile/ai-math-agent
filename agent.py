import ollama
from tools import add, subtract, multiply, divide
import re

systemPrompt = """
You are an AI calculator assistant.
you must never perform arithmetic operations yourself.
you must always use available tools.

Available tools:
-add(a,b)
-subtract(a,b)
-multiply(a,b)
-divide(a,b)

Follow these steps upon user input
1. identify the operation
2. extract numbers from user input
3. use the correct tool
4. return result
"""

def extractNum(text):
    return list(map(float, re.findall(r'\d+',text)))

def chooseTool(userInput):

    numbers = extractNum(userInput)

    if len(numbers)<2:
        return "Please enter 2 numbers."
    
    a,b=numbers[0], numbers[1]

    if "add" in userInput or "sum" in userInput or "plus" in userInput or "take" in userInput or "buy" in userInput:
        return add(a,b)
    if "subtract" in userInput or "difference" in userInput or "minus" in userInput or "give" in userInput:
        return subtract(a,b)
    if "multiply" in userInput or "product" in userInput or "times" in userInput:
        return multiply(a,b)
    if "divide" in userInput or "over" in userInput or "split" in userInput:
        return divide(a,b)
    
    return "Error: operation not recognised."