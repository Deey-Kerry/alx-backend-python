#!/usr/bin/env python3
"""a measure_time function with integers n and max_delay"""
import asyncio
from time import perf_counter
imported_func = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """
    start_time = perf_counter()
    asyncio.run(imported_func(n, max_delay))
    end_time = perf_counter()
    return (end_time - start_time)
