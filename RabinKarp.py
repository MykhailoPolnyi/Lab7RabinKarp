def rabin_karp(search_text, pattern, mod=107, base=10):
    def hash_string(string_to_hash):
        h = 0
        for letter in string_to_hash:
            h = (h*base + ord(letter)) % mod
        return h

    def rehash(string_hash, removed_letter, new_letter):
        new_hash = string_hash - (first_char_coeff * ord(removed_letter)) % mod
        new_hash *= base
        new_hash += ord(new_letter)
        new_hash %= mod

        return new_hash

    def count_first_char_coeff():
        counted_coef = 1
        for _ in range(1, pattern_len):
            counted_coef *= base
            counted_coef %= mod
        return counted_coef

    pattern_len = len(pattern)
    if pattern_len == 0:
        return []

    search_results = []
    text_len = len(search_text)
    compare_point = 0
    last_char_pos_to_check = text_len - pattern_len

    pattern_hash = hash_string(pattern)
    search_hash = hash_string(search_text[compare_point:pattern_len])

    first_char_coeff = count_first_char_coeff()

    for compare_point in range(last_char_pos_to_check + 1):
        if search_hash == pattern_hash:
            match_found = True
            for i in range(pattern_len):
                if search_text[i + compare_point] != pattern[i]:
                    match_found = False
                    break
            if match_found:
                search_results.append(compare_point)
        if compare_point != last_char_pos_to_check:
            search_hash = rehash(search_hash, search_text[compare_point], search_text[compare_point+pattern_len])

    return search_results
