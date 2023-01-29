def reverse_array(n):
    if type(n) == str:
        return n[::-1]
    if type(n) == int:
        reversed = int(str(n)[::-1])
        return reversed
    if type(n) == list:
        return n[::-1]

def dynamicArray(n,query):
    if type(query) == str:
        return "This is a str"
    arr = []
    lastAnswer = 0
    array_answers = []
    for num in range(0,n):
        arr.append([])

    for nodo in query:
        if nodo[0] == 1:
            index = ((nodo[1] ^ lastAnswer) % n)
            arr[index] = nodo[1]
        if nodo[0] == 2:
            index = ((nodo[1] ^ lastAnswer) % n)
            lastAnswer = arr[index][nodo[1] % len(arr[index])]
            array_answers.append(lastAnswer)
            print(lastAnswer)

print(3^6)