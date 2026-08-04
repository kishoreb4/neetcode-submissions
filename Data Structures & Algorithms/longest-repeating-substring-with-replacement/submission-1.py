class Solution():
    def characterReplacement(self, s: str, k: int) -> int:
        # A window is valid if:
        # window_length - count_of_most_frequent_char <= k
        # Because: if the most frequent char appears max_count times, you need to replace all other chars — that's window_length - max_count replacements. If that's ≤ k, the window is valid.
        count = {}
        left = 0
        res = 0
        max_count = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
            # Update max frequency. Only need to check the newly added char — it's the only one that could have increased.
            while (i - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        return res