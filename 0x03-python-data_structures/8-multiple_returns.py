#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])

if __name__ == "__main__":
    # Example usage
    text = "Hello, World!"
    result = multiple_returns(text)
    print(result)
