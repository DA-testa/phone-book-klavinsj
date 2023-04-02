# python3
class HashMap:
    _multiplier = 123
    _prime = 100000000005
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]
        
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count
        
    def add(self, number, name):
        hashed = self._hash_func(number)
        bucket = self.buckets[hashed]
        for i, (num, _) in enumerate(bucket):
            if num == number:
                bucket[i] = (number, name)
                return
        bucket.append((number, name))
        
    def delete(self, number):
        hashed = self._hash_func(number)
        bucket = self.buckets[hashed]
        for i, (num, _) in enumerate(bucket):
            if num == number:
                bucket.pop(i)
                return
        
    def find(self, number):
        hashed = self._hash_func(number)
        bucket = self.buckets[hashed]
        for num, name in bucket:
            if num == number:
                return name
        return "not found"

def main():
    n = int(input())
    phone_book = HashMap()
    result = []
    for i in range(n):
        ievade = input().split()
        if ievade[0] == "add":
            phone_book.add(ievade[1], ievade[2])
        elif ievade[0] == "del":
            phone_book.delete(ievade[1])
        elif ievade[0] == "find":
            print(phone_book.find(ievade[1]))

if __name__ == "__main__":
    main()