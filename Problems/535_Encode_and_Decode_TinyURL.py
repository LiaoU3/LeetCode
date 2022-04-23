import secrets

class Codec:
    
    def __init__(self):
        self.url_table = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        enc = secrets.token_hex(4)
        while enc in self.url_table:
            enc = secrets.token_hex(4)
        self.url_table[enc] = longUrl
        return "http://tinyurl.com/" + enc

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_table[shortUrl[19:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))