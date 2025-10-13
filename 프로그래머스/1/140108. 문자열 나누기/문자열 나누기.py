def solution(s):
    ans=bal=0;x=''
    for c in s:
        if bal==0:x=c
        bal+=1 if c==x else -1
        if bal==0:ans+=1
    return ans if bal==0 else ans+1