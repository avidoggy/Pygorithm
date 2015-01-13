import re

def poly_add(p1, p2):
    result = p1.copy()
    for i in p2:
        if result.has_key(i):
            result[i] += p2[i]
        else:
            result[i] = p2[i]

    return result

def poly_sub(p1, p2):
    result = p1.copy()
    for i in p2:
        if result.has_key(i):
            result[i] -= p2[i]
        else:
            result[i] = -p2[i]

    return result

def poly_product(p1, p2):
    result = dict()
    for i in p1:
        for j in p2:
            power = i + j
            value = p1[i] * p2[j]
            if result.has_key(power):
                result[power] += value
            else:
                result[power] = value

    return result

def simplify(expr):
    stack = []
    postfix = []
    priority = {'(': 0, '+': 1, '-': 1, '*': 2}
    i = 0
    while i < len(expr):
        if expr[i] == '(':
            stack.append(expr[i])
            i += 1
        elif expr[i] == ')':
            oper = stack.pop()
            while oper != '(':
                postfix.append(oper)
                oper = stack.pop()
            i += 1
        elif expr[i] == '+' or expr[i] == '-' or expr[i] == '*':
            while len(stack) > 0 and priority[stack[-1]] >= priority[expr[i]]:
                postfix.append(stack.pop())
            stack.append(expr[i])
            i += 1
        else :
            match = re.match(r'\d+', expr[i : ])
            if match :
                postfix.append({0 : int(match.group())})
                i += len(match.group())
            match = re.match(r'x(\*\*(?P<pow>\d+))?', expr[i : ])
            if match:
                if match.group('pow'):
                    #print match.group('pow')
                    postfix.append({int(match.group('pow')) : 1})
                else:
                    postfix.append({1 : 1})
                i += len(match.group())

    while len(stack) != 0:
        postfix.append(stack.pop())

    #print postfix
    for i in postfix:
        if i == '+':
            p2 = stack.pop()
            p1 = stack.pop()
            stack.append(poly_add(p1, p2))
        elif i == '-':
            p2 = stack.pop()
            p1 = stack.pop()
            stack.append(poly_sub(p1, p2))
        elif i == '*':
            p2 = stack.pop()
            p1 = stack.pop()
            stack.append(poly_product(p1, p2))
        else:
            stack.append(i)

    result = stack.pop()
    #print result
    l = []

    for k in sorted(result.iterkeys(), reverse = True):
        if result[k] == 0:
            continue

        if k == 0:
            term = str(abs(result[k]))
        else :
            if k == 1:
                term = 'x'
            else:
                term = 'x**' + str(k)

            if abs(result[k]) != 1:
                #term += str(abs(result[k])) + '*' + term
                term = str(abs(result[k])) + '*' + term

        if result[k] > 0:
            term = '+' + term
        else:
            term = '-' + term
        l.append(term)

    if len(l) == 0:
        return '0'

    expr_str = "".join(l)
    #print expr_str

    return expr_str[1 : ] if expr_str[0] == '+' else expr_str

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert simplify(u"(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify(u"(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify(u"(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify(u"x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify(u"(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify(u"x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify(u"5-5-x") == "-x", "Negative C1"
    assert simplify(u"x*x*x-x*x*x-1") == "-1", "Negative C0"

