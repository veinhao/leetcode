class Solution:
    def closestCost(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        """
        1. 遍历baseCosts值，并在内部嵌套遍历toppingCosts值的循环
        2. 个数：baseCosts = [1](只能取1) ，toppingCosts = [0, 1, 2]（可以取0，1，2）
        3. 1 * baseCosts[0] + [0, 0, 0] * toppingCosts
           1 * baseCosts[0] + [1, 0, 0] * toppingCosts
        """
        # 保存的差值
        subs = 999999999

        # 保存的最终结果
        f_res = -1
        for i in range(len(baseCosts)):
            for j in range(len(toppingCosts)):

                for k in range(3):
                    res = baseCosts[i] + toppingCosts[j] * k
                    # 如果找到更接近的值，保存到subs, 同时保存当前的较优 res
                    if abs(res - target) < subs:
                        subs = abs(res - target)
                        f_res = subs

        return f_res


def get_toppingCosts_array(toppingCosts: list[int]) -> list[int]:
    """
    对于 toppingCosts数组所有元素进行遍历相加并返回
    【3， 4】 * 【0， 0】 = 0
    【3， 4】 * 【1， 0】 = 3
    【3， 4】 * 【2， 0】 = 6

    【3， 4】 * 【0， 1】 = 4
    【3， 4】 * 【1， 1】 = 7
    【3， 4】 * 【2， 1】 = 10
    。。。
    【3， 4】 * 【2， 2】 = 14
    :param toppingCosts:
    :return: a list
    """
    restore = [[]]
    for i in range(len(toppingCosts)):
        for k in range(3):
            res = toppingCosts[i] * k
            if i != 0:
                res = res + restore[i-1][k]
            restore[i][k] = res 




if __name__ == '__main__':
    b = [1, 7]
    t = [3, 4]
    target = 10
    res1 = Solution()
    f = res1.closestCost(b, t, target)
    print(f)
