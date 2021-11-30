def rabin_karp(search_text, pattern, mod=17, base=10):
    def hash_string(string_to_hash):
        h = 0
        for j in range(pattern_len):
            h = (h*base + ord(string_to_hash[j])) % mod
        return h

    def rehash(string_hash, removed_letter, new_letter):
        first_char_coeff = 1
        for k in range(1, pattern_len):
            first_char_coeff *= base
            first_char_coeff %= mod

        new_hash = string_hash - (first_char_coeff * ord(removed_letter)) % mod
        new_hash *= base
        new_hash += ord(new_letter)
        new_hash %= mod

        return new_hash

    search_results = []
    pattern_len = len(pattern)
    text_len = len(search_text)
    compare_point = 0

    pattern_hash = hash_string(pattern)
    search_hash = hash_string(search_text[compare_point:pattern_len])

    last_char_pos_to_check = text_len - pattern_len

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
