def rabin_karp_search(haystack, needle):
    if not haystack or not needle:
        return []

    result = []
    haystack_length = len(haystack)
    needle_length = len(needle)
    prime = 11

    def calculate_hash(substring):
        hash_value = 0
        for char in substring:
            hash_value = (hash_value * prime + ord(char)) % haystack_length
        return hash_value

    needle_hash = calculate_hash(needle)
    haystack_hash = calculate_hash(haystack[:needle_length])

    for i in range(haystack_length - needle_length + 1):
        if haystack_hash == needle_hash and haystack[i:i + needle_length] == needle:
            result.append(i)

        if i < haystack_length - needle_length:
            haystack_hash = (haystack_hash - ord(haystack[i]) * pow(prime, needle_length - 1, haystack_length)) % haystack_length
            haystack_hash = (haystack_hash * prime + ord(haystack[i + needle_length])) % haystack_length
            haystack_hash = (haystack_hash + haystack_length) % haystack_length

    return result

haystack = "My name is Andrii is"
needle = "is"
result_indices = rabin_karp_search(haystack, needle)
print(f"Індекси входжень '{needle}' в '{haystack}': {result_indices}")
