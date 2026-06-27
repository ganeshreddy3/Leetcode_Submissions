class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        for item in items:
            if ruleKey=="type":
                temp=0
            elif ruleKey=="color":
                temp=1
            else:
                temp=2
            if item[temp]==ruleValue:
                count+=1
        return count