functions = {}
def funcdict(label):
    def wrap(f):
        # could use __name__ here
        functions[label] = f
        return f
    return wrap
