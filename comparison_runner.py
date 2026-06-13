import time
import Levenshtein as lev_lib
from fuzzywuzzy import fuzz, process
from levenshtein_algo import levenshtein_distance
from doc_processor import get_text_from_docx, get_docx_files_from_directory

def benchmark(func, *args, iterations=100):
    start_time = time.time()
    for _ in range(iterations):
        func(*args)
    end_time = time.time()
    return (end_time - start_time) / iterations

def run_fuzzywuzzy_tasks():
    print("--- FuzzyWuzzy Tasks ---")
    
    r1 = fuzz.ratio('Привет мир', 'Привет мир')
    r2 = fuzz.ratio('Привет мир', 'Привт кир')
    print(f"fuzz.ratio identical: {r1}, similar: {r2}")

    p1 = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, Привет мир')
    print(f"fuzz.partial_ratio: {p1}")

    t1 = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
    t2 = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
    print(f"token_sort_ratio: {t1}, token_set_ratio: {t2}")

    cities = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар"]
    best_match = process.extractOne("Саратов", cities)
    print(f"Best match for 'Саратов': {best_match}")

def compare_methods(text1: str, text2: str):
    print(f"\n--- Comparing methods for strings of length {len(text1)} and {len(text2)} ---")
    
    start = time.time()
    dist_custom = levenshtein_distance(text1, text2)
    time_custom = time.time() - start
    
    start = time.time()
    dist_lib = lev_lib.distance(text1, text2)
    ratio_lib = lev_lib.ratio(text1, text2)
    time_lib = time.time() - start
    
    start = time.time()
    ratio_fuzzy = fuzz.ratio(text1, text2)
    time_fuzzy = time.time() - start
    
    print(f"{'Method':<25} | {'Distance/Ratio':<20} | {'Time (sec)':<15}")
    print("-" * 65)
    print(f"{'Custom Levenshtein':<25} | Dist: {dist_custom:<14} | {time_custom:.6f}")
    print(f"{'python-Levenshtein Lib':<25} | Dist: {dist_lib:<14} | Ratio: {ratio_lib:.2f} | {time_lib:.6f}")
    print(f"{'FuzzyWuzzy (fuzz.ratio)':<25} | Ratio: {ratio_fuzzy:<14} | {time_fuzzy:.6f}")

if __name__ == "__main__":
    run_fuzzywuzzy_tasks()
    
    s1 = "Привет мир, это тестовая строка для сравнения методов."
    s2 = "Привет мир, это тестовая строчка для сравнения метдов."
    compare_methods(s1, s2)