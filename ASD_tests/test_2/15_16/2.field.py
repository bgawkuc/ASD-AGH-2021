# struct field {
# int value;
# int long j;
# int short j;
# };
# Z każdego pola można skakać tylko o ilość pól zapisaną w long j lub short j. Napisać program
# który zwróci maksymalną wartość jaką możemy osiągnąć poprzez przejście z pola 0 do n-1.
# Można założyć że z każdego pola da się dojść do pola n-1.

class field:
    def __init__(self, value, short, long):
        self.value = value
        self.short = short
        self.long = long


def maxValue(A):
    n = len(A)
    dp = [0] * n
    dp[n - 1] = A[n - 1].value
    jump = ['long'] * n

    for i in range(n - 2, -1, -1):
        dp[i] = dp[i + A[i].short] + A[i].value

        if i + A[i].long < n:
            dp[i] = max(dp[i], dp[i + A[i].long] + A[i].value)

        if dp[i] == dp[i + A[i].short] + A[i].value:
            jump[i] = 'short'

    i = 0
    while i < n - 1:
        if jump[i] == 'short':
            i += A[i].short
        else:
            i += A[i].long

    return dp[0]


A0 = field(1, 1, 3)
A1 = field(3, 2, 3)
A2 = field(1, 1, 2)
A3 = field(1, 2, 3)
A4 = field(6, 1, 2)
A5 = field(1, 1, 2)
A6 = field(1, 1, 2)

A = [A0, A1, A2, A3, A4, A5, A6]
print(maxValue(A))
