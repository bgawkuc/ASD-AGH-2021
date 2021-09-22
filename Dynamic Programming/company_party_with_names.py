# impreza firmowa z wypisywaniem imion


class Employee:
    def __init__(self, f, n):
        self.emp = []  # podwladni
        self.f = f  # fun
        self.n = n  # name
        self.best_party = None  # value of best party with employee
        self.without_emp = None  # best party without employee
        self.go = False  # going tu party


def best_party_without_employee(e):  # najlepsza impreza bez szefa
    if e.without_emp is not None: #gdy jest juz to policzone
        return e.without_emp

    e.without_emp = 0

    for o in e.emp:
        e.without_emp += best_party(o)

    return e.without_emp


def best_party(e): #najlepsza impreza z szefem
    if e.best_party is not None: #gdy jest to policzone dla odpowiedniego wiezrchołka
        return e.best_party

    go = e.f  # suma gdy szef idzie

    for u in e.emp:  # dodaje do niej wszystkie sumy podszefow jego podszefow
        go += best_party_without_employee(u)

    not_go = best_party_without_employee(e)  # suma gdy szef nie idzie

    if go > not_go:  # gdy szef idzie
        e.go = True

        for x in e.emp:  # to jego podszefi nie idą
            x.go = False

    else:  # gdy szef nie idzie
        e.go = False

    e.f = max(go, not_go)
    return e.f


def result(root):
    partiers = []

    def func(curr):

        if curr.go:
            partiers.append(curr.n)

        for e in curr.emp:
            func(e)

    func(root)

    return partiers


b = Employee(1, "A")
b.emp = [Employee(15, "B"), Employee(3, "C")]
b.emp[0].emp = [Employee(5, "D"), Employee(3, "E")]
b.emp[1].emp = [Employee(8, "F")]

print(best_party(b))
print(result(b))

