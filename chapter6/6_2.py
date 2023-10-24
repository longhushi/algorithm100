# 新郎和新娘
"""
有三对情侣结婚，假设三个新郎为A、B、C，三个新娘为X、Y、Z。有参加婚礼的人搞不清谁和谁结婚，
所以去询问了这六位新人中的三位，得到的回答为：新郎A说他要和新娘X结婚；新娘X说她的未婚夫是新郎C；而新郎C说他要和新娘Z结婚。
听到这样的回答后，提问者知道他们都是在开玩笑，说的都是假话，但他仍搞不清谁和谁结婚。现在请编程求出到底哪位新郎和哪位新娘结婚。
"""
# 因为都是假话，所以A不是和X结婚，X不是和C结婚，C不是和Z结婚

def solve():
    
    for a in ['X', 'Y', 'Z']:
        for b in ['X', 'Y', 'Z']:
            for c in ['X', 'Y', 'Z']:
                if a!='X' and c!='X' and c!='Z' and a!=b and a!=c and b!=c:
                    print("A和{}结婚".format(a))
                    print("B和{}结婚".format(b))
                    print("C和{}结婚".format(c))
        
if __name__ == '__main__':
    solve()