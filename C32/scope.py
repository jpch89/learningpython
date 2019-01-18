def generate():
    class Spam:
        count = 1
        def method(self):
            print(count)
    return Spam()


generate().method()
