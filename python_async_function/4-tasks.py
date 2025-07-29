import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_n(n: int, max_delay: int) -> float:
    return asyncio.run(wait_n(n, max_delay))
