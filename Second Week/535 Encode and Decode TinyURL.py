import random

class Codec:
    def __init__(self):
        self.urlHashMap = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        randomCode = self.createRandomCode()
        domain = "http://tinyurl.com/"
        shortUrl = domain + randomCode
        self.urlHashMap[shortUrl] = longUrl
        return shortUrl
    
    def createRandomCode(self):
        while(True):
            randomCode = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(6)])
            if randomCode not in self.urlHashMap.keys():
                return randomCode

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urlHashMap[shortUrl]



# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.decode(codec.encode(url)))
