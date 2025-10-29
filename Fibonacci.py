cache = [None]*(6)

def fibonacci(n): 
    print(f"call fibonacci({n})")
    if n <= 1:
        print(f"return fibonacci({n})")
        return n
    
    # Check if the value exists
    if cache[n] is None:
        # Save the result in cache
        cache[n] = fibonacci(n-2) + fibonacci(n-1)
        print(f"cache fibonacci({n})")
    print(f"return fibonacci({n})")
    return cache[n]

print(f"fibonacci(5) = {fibonacci(5)}")
