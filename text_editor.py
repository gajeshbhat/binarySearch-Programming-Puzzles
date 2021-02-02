class Solution:
    def solve(self, s):
        editor_stk = list()
        for i in range(len(s)):
            current_char = s[i]
            if current_char == '-':
                # Look at the previous charcter
                if i > 0 and s[i-1] == '<':
                    # Pop two times : Check len the second time as we might pop the very first character
                    editor_stk.pop()
                    if len(editor_stk) > 0:
                        editor_stk.pop()
                else:
                    editor_stk.append(current_char)
            else:
                editor_stk.append(current_char)
        rev_str = str()
        for char in editor_stk:
            rev_str = rev_str + char
        return rev_str