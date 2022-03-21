from B import solution

def get_testcase(file):
    with open(file) as f:
        cases = f.read().split('-'*15)
        for case in cases:
            inp, out = case.split('OUTPUT:')
            inp = inp.strip().strip('INPUT:').strip()
            out = out[1:-2]
            yield inp, out

case = 1
for inp, out in get_testcase('TestCasesB.txt'):
    attempt = solution(int(inp))
    assert attempt == out, f"Case {case} failed!\nInput:\n{inp}\nExpected:\n{out}\nGot:\n{attempt}"
    print(f'Case {case}: OK')
    case += 1
print('All tests passed!')
