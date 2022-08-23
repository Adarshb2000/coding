from typing import List


class Solution:
    def removeComments(self, source: List[str]):
        
        for i, x in enumerate(source):
            x = x.replace('/*', '\\', -1)
            x = x.replace('*/', '\\', -1)
            x = x.replace('//', '\"', -1)
            source[i] = x
        
        
        string = '\n'.join(source)
        answer = ''
        i = 0
        n = len(string)
        while i < n:
            if string[i] == '\"':
                while string[i] != '\n':
                    i += 1
                i += 1
                continue
            if string[i] == '\\':
                i += 1
                while string[i] != '\\':
                    i += 1
                i += 1
                continue
            
            answer += string[i]
            i += 1
        
        return [i for i in answer.split('\n') if i]
        
        
    
test = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print(Solution().removeComments(test))