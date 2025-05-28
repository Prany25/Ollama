import ollama


response = ollama.list()

res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "why is the sky blue?"},
    ],
)

res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "why is the ocean so salty?",
        },
    ],
    stream=True,
)

res = ollama.generate(
    model="llama3.2",
    prompt="why is the sky blue?",
)

modelfile = """
FROM llama3.2
SYSTEM You are very smart assistant who knows everything about oceans. You are very succinct and informative.
PARAMETER temperature 0.1
"""
ollama.create(model="knowitall", modelfile=modelfile)

res = ollama.generate(model="knowitall", prompt="why is the ocean so salty?")
print(res["response"])

ollama.delete("knowitall")