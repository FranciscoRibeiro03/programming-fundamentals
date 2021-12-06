def p(x):
    return x**2 + 2*x + 3

def main():
    p0 = p(0)
    p1 = p(1)
    p2 = p(2)
    pp1 = p(p1)
    print(f"""
p(0): {p0}
p(1): {p1}
p(2): {p2}
p(p(1)): {pp1} 
""")

main()