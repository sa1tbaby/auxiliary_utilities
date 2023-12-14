class Solution:
    @staticmethod
    def countBits(n: int) -> list[int]:
        ans = list()
        n += 1
        for iter_ in range(n):
            curr = 0

            while iter_:

                if iter_ % 2 == 1:
                    curr += 1

                iter_ = iter_ // 2

            ans.append(curr)

        return ans


if __name__ == '__main__':

    n = 55

    case = Solution.countBits(n)
    print(case)
