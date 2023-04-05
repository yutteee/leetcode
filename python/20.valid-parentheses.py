#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # ([{先頭の括弧に注目する
        # 先頭の括弧をどんどん保存していく
        # 閉じ括弧が現れた場合、一番後ろの先頭括弧を参照する
        # okだったら保存してた場所から削除
        # ダメだったらfalseをリターン
        # ループが終わった際に保存が0ならok
        tmp = []
        for idx, ch in enumerate(s):
            if ch == '(' or ch == "{" or ch == "[":
                tmp.append(ch)

            if ch == ')':
                if (idx - 1) == -1:
                    return False
            
            if ch == ')':
                if tmp == []:
                    return False
                elif tmp[-1] == '(':
                    tmp.pop(-1)
                else:
                    return False
            if ch == ']':
                if tmp == []:
                    return False
                elif tmp[-1] == '[':
                    tmp.pop(-1)
                else:
                    return False
            if ch == '}':
                if tmp == []:
                    return False
                elif tmp[-1] == '{':
                    tmp.pop(-1)
                else:
                    return False
        
        if tmp == []:
            return True

# @lc code=end

