def rabin_karp(search_text, pattern, mod=12, base=10):
    def hash_string(string_to_hash):
        h = 0
        for j in range(pattern_len):
            h += ord(string_to_hash[j])*(base**(pattern_len - j - 1))
        return h

    def rehash(string_hash, removed_letter, new_letter):
        new_hash = string_hash - ord(removed_letter)*(base**(pattern_len-1)) + ord(new_letter)
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


if __name__ == '__main__':
    print(rabin_karp("Like the Naive Algorithm, Rabin-Karp algorithm also slides the pattern one by one. "
                     "But unlike the Naive algorithm, Rabin Karp algorithm matches the hash value of the"
                     " pattern with the hash value of current substring of text, and if the hash values "
                     "match then only it starts matching individual characters. So Rabin Karp algorithm "
                     "needs to calculate hash values for following strings.",
                     "m"))
