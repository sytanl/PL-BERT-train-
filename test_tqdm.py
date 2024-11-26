"""
Run `pip install tqdm` before running the script.

The function `foo` is going to be executed 100 times across
`MAX_WORKERS=5` processes. In a single pass, each process will
get an iterable of size `CHUNK_SIZE=5`. So 5 processes each consuming
5 elements of an iterable will require (100 / (5*5)) 4 passes to finish
consuming the entire iterable of 100 elements.

Tqdm progress bar will be updated after every `MAX_WORKERS*CHUNK_SIZE` iterations.
"""

# src.py


from __future__ import annotations

import multiprocessing as mp

from tqdm import tqdm
import time

import random
from dataclasses import dataclass

MAX_WORKERS = 5
CHUNK_SIZE = 5


@dataclass
class StartEnd:
    start: int
    end: int


def foo(start_end: StartEnd) -> int:
    time.sleep(0.2)
    return random.randint(start_end.start, start_end.end)


def main() -> None:
    inputs = [
        StartEnd(start, end)
        for start, end in zip(
            range(0, 100),
            range(100, 200),
        )
    ]

    with mp.Pool(processes=MAX_WORKERS) as pool:
        results = tqdm(
            pool.imap_unordered(foo, inputs, chunksize=CHUNK_SIZE),
            total=len(inputs),
        )  # 'total' is redundant here but can be useful
        # when the size of the iterable is unobvious

        for result in results:
            print(result)


if __name__ == "__main__":
    main()
