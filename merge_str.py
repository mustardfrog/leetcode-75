import unittest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        i = 0
        j = 0

        while (i < len(word1) and j < len(word2)):
            answer.append(word1[i])
            answer.append(word2[j])
            i += 1
            j += 1

        while (i < len(word1)):
            answer.append(word1[i])
            i += 1
        while (j < len(word2)):
            answer.append(word2[j])
            j += 1

        return "".join(answer)


if __name__ == "__main__":
    unittest.main()


class TestMergeStr(unittest.TestCase):
    def test_mergeAlter(self):
        s = Solution()
        self.assertEqual(s.mergeAlternately("abc", "pqr"), "apbqcr")
        self.assertEqual(s.mergeAlternately("ab", "pqrs"), "apbqrs")
        self.assertEqual(s.mergeAlternately("abcd", "pq"), "apbqcd")
