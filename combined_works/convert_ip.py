import json

def convert_to_json(code):
    # This is a simplified example; real parsing would be more complex
    functions = []

    # Example function extraction (in a real scenario, use a parser)
    functions.append({
        "name": "example_function",
        "instrs": [
            {"dest": "a", "op": "add", "args": ["b", "c"]},
            {"dest": "d", "op": "mul", "args": ["a", "e"]},
            {"dest": "f", "op": "call", "args": ["g", "h"]},
            {"dest": "d", "op": "print", "args": ["d"]}
        ]
    })

    return json.dumps({"functions": functions}, indent=2)

# Example usage
code = '''
def example_function():
    a = b + c
    d = a * e
    f = g(h)
    print(d)
'''
json_output = convert_to_json(code)
print(json_output)
