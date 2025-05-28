import ollama


response = ollama.list()

res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "what is your name?"},
    ],
)

res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "what is a flower?",
        },
    ],
    stream=True,
)

res = ollama.generate(
    model="llama3.2",
    prompt="what is your name?",
)

modelfile = """
FROM llama3.2
SYSTEM You are very smart assistant who knows everything about oceans. You are very succinct and informative.
PARAMETER temperature 0.1
"""
ollama.create(model="knowitall", modelfile=modelfile)

res = ollama.generate(model="knowitall", prompt="whst is a flower?")
print(res["response"])

ollama.delete("knowitall")