def reverse_string(st):
    return ' '.join(reverse_word(word) for word in st.split())

def reverse_word(st):
    stack = []
    for el in st:
        if el.isalpha():
            stack.append(el)
    result = ''
    for el in st:
        if el.isalpha():
            result += stack.pop()
        else:
            result += el
    return result

instr = 'b3ghcd hg#tyj%h'

print(reverse_string(instr)) # prints 'd3chgb hj#ytg%h'
