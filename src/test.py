import cocotb
from cocotb.triggers import ClockCycles


numbers = list(range(2**3))


def collatz(n):
    return n / 2 if n % 2 == 0 else 3 * n + 1


@cocotb.test()
async def test_collatz(dut):
    dut.n.value = 3
    await ClockCycles(dut.clk, 1)
    assert int(dut.out.value) == collatz(3)
