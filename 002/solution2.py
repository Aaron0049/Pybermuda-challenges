from time import perf_counter


def fibonacci(n) -> int:
    flist = [0, 1]
    for i in range(2, n):
        flist.append(flist[i-1] + flist[i-2])
    return flist[n-1]
    

def check_fibonacci() -> None:
    n = 40
    max_time = 1

    start = perf_counter()
    answer = fibonacci(n)

    assert (
        answer is not None
    ), "Yeah you're going to actually have to write something in the fibonacci function"

    assert (
        answer == 63245986
    ), f"Unfortunately {answer} is not the {n}th fibonacci number"

    print(f"The {n}th fibonacci number is {answer}")
    stop = perf_counter()

    elapsed = stop - start

    assert (
        elapsed < max_time
    ), f"The {n}th fibonacci number took more than {max_time}s: it took {elapsed:.2f}s"

    print(f"Done in {elapsed:.6f}s")


if __name__ == "__main__":
    check_fibonacci()