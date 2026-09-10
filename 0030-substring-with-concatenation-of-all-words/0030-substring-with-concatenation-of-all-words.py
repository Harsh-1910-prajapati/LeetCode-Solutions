class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        from collections import Counter

        target = Counter(words)
        result = []

        for start in range(word_len):
            left = start
            right = start
            count = 0
            current = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in target:
                    current[word] += 1
                    count += 1

                    while current[word] > target[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)

                else:
                    current.clear()
                    count = 0
                    left = right

        return result