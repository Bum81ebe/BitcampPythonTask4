# converting symbols to EMOJI

def func():
    text = input("Tell me something: ")
    text = convert(text)
    print(text)


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


func()