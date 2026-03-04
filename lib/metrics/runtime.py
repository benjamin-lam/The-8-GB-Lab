import time
import os
import psutil

def now_ms() -> float:
    return time.perf_counter() * 1000.0

def measure_ram_mb() -> float:
    # RAM of current process
    proc = psutil.Process(os.getpid())
    return proc.memory_info().rss / (1024 * 1024)
