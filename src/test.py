import cocotb


BIT_LENGTH = 4
numbers = list(range(2**BIT_LENGTH))


def collatz(n):
    return n / 2 if n % 2 == 0 else 3 * n + 1


@cocotb.test()
async def test_collatz(dut):
    for n in numbers:
        dut.n.value = n
        c = collatz(n)
        if c < 2**BIT_LENGTH:
            assert int(dut.out.value) == c
