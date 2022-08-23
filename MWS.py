class Solution:
    def something(self, s: str, t: str):
        from collections import deque
        t_elements = {}
        for c in t:
            t_elements[c] = t_elements.get(c, 0) - 1

        
        start = 0
        m = s.__len__()

        while start < m and s[start] not in t_elements:
            start += 1
        
        if start == m and s[start - 1] not in t:
            return ''
        
        i = start
        t_copy = t_elements.copy()
        extras = t_elements.copy()
        queue = deque()

        while len(t_copy) and i < m:
            if s[i] in t_copy:
                t_copy[s[i]] += 1
                if not t_copy[s[i]]:
                    del t_copy[s[i]]
            
            if s[i] in extras:
                queue.append(i)
                extras[s[i]] += 1
            
            i += 1
        
        if i == m and len(t_copy):
            return ""
        else:
            curr_index = [start, i]
            curr_length = i - start
        
        max_length = curr_length
        max_index = curr_index.copy()

        while i < m and len(queue):
            curr_char = s[queue.popleft()]
            if extras[curr_char] >= abs(t_elements[curr_char]):
                extras[curr_char] -= 1
                
            else:
                while i < m and s[i] != curr_char:
                    if s[i] in t_elements:
                        queue.append(i)
                        extras[s[i]] += 1
                    
                    i += 1
                if i < m:
                    queue.append(i)
                    extras[s[i]] += 1
                    i += 1
            
            if len(queue):    
                curr_index = [queue[0], i]
                curr_length = curr_index[1] - curr_index[0]

                if max_length > curr_length:
                    max_length = curr_length
                    max_index = curr_index.copy()
        
        return s[max_index[0] : max_index[1]]

print(Solution().something(s = "bba", t = "ab"))    
            
            
