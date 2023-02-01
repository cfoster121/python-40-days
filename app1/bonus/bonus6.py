contents = ["Peter Piper picked",
            "How much wood would a woodchuck",
            "Sally sells seashells"]

filenames = ['p.txt', 'w.txt', 's.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)