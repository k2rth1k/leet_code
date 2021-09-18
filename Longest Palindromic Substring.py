"""
    ref : https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        palindrome_matrix = [[0] * length for i in range(length)]
        j = 0
        palindrome_matrix[0] = [1] * length
        max_palindrome_length = 1
        max_length_palindrome = s[0]
        for i in range(length):
            j = i
            palindrome_length = i + 1
            while j < length and i > 0:
                if s[j] == s[j-palindrome_length+1]:
                    if palindrome_length - 2 == 0:
                        palindrome_matrix[i][j] = 2
                    else:
                        if palindrome_matrix[i - 2][j - 1] != 0:
                            palindrome_matrix[i][j] = palindrome_matrix[i - 2][j - 1] + 2

                if palindrome_matrix[i][j] > max_palindrome_length:
                    max_palindrome_length = palindrome_matrix[i][j]
                    max_length_palindrome = s[j-palindrome_length+1:j + 1]
                j = j + 1
        return max_length_palindrome


def main():
    sol = Solution()
    print(sol.longestPalindrome("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"))


if __name__ == "__main__":
    main()
