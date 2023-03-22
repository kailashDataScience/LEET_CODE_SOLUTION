class Solution:
    def romanToInt(self, s: str) -> int:
         roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
         result = 0
         prev_value = 0
    
         for i in range(len(s) - 1, -1, -1):
             current_value = roman_map[s[i]]
             print(current_value)
             if current_value < prev_value:
                 result -= current_value
             else:
                 result += current_value
            
             prev_value = current_value
        
         return result
        