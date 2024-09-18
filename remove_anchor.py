to_test = [
    ["www.codewars.com#about", "www.codewars.com"],
    ["www.codewars.com?page=1", "www.codewars.com?page=1"]
]

def remove_anchor(input, expected):
    print(input, 'input')
    print(expected, 'expected')

for input, expected in to_test:
    remove_anchor(input, expected)
