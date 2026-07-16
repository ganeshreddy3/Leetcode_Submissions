class Solution:
    def reverseWords(self, s: str) -> str:
        vowel=set('aeiou')
        arr=s.split()
        res=[]
        appear=0
        for i in arr[0]:
            if i in vowel:
                appear+=1
        res.append(arr[0])
        for word in arr[1:]:
            count=0
            for i in word:
                if i in vowel:
                    count+=1
            if count==appear:
                res.append(word[::-1])
            else:
                res.append(word)
        ans=""
        n=len(res)
        for i in range(n):
            ans+=res[i]
            if i!=n-1:
                ans+=" "
        return ans