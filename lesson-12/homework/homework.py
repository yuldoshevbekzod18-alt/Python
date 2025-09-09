
#Exercise 1: Threaded Prime Number Checker
#Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.
import threading
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes_in_range(start, end, result_list):
    for number in range(start, end + 1):
        if is_prime(number):
            result_list.append(number)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    result = []

    # Lock to protect shared resource (result list)
    lock = threading.Lock()

    # Function wrapper to safely append primes with lock
    def thread_task(s, e):
        local_primes = []
        check_primes_in_range(s, e, local_primes)
        with lock:
            result.extend(local_primes)

    total_numbers = end - start + 1
    chunk_size = total_numbers // num_threads

    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        # Make sure the last thread goes till the end
        chunk_end = start + (i + 1) * chunk_size - 1 if i != num_threads - 1 else end

        t = threading.Thread(target=thread_task, args=(chunk_start, chunk_end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    result.sort()
    return result

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4

    primes = threaded_prime_checker(start_range, end_range, num_threads)
    print(f"Primes between {start_range} and {end_range}:")
    print(primes)
#Exercise 2: Threaded File Processing
#Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads
import threading
from collections import Counter
from queue import Queue
import os

# Number of threads to use
NUM_THREADS = 4

def process_lines(lines, result_queue):
    """Function to count word occurrences in a list of lines."""
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result_queue.put(word_count)

def threaded_word_count(file_path, num_threads=NUM_THREADS):
    # Read the entire file into memory (can be optimized for very large files)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Divide the lines into chunks for each thread
    chunk_size = len(lines) // num_threads
    threads = []
    result_queue = Queue()

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        thread = threading.Thread(target=process_lines, args=(lines[start:end], result_queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Combine results from all threads
    final_word_count = Counter()
    while not result_queue.empty():
        final_word_count += result_queue.get()

    return final_word_count

# Example usage
if __name__ == "__main__":
    file_path = "large_text_file.txt"  # Replace with your file path

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
    else:
        result = threaded_word_count(file_path)
        for word, count in result.most_common(20):  # Display top 20 most common words
            print(f"{
