#Checking palindrome if input is a number
class Solution:
    i = 0
    def isPalin(self,N):
        #code here
        
        #converting int to string
        n = str(N)
        
        #iterating i
        if(self.i <= (len(n) - self.i-1)):
            #comparing the start and end element
            if(n[self.i] == n[len(n) - self.i-1] ):
                self.i +=1
                return self.isPalin(n)
            else:
                return 0
        else:
            return 1