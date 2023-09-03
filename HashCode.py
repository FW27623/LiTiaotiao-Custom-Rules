import sys

class JavaHashStr(str):
    def __hash__(self):
        hashCode = 0
        for char in self:
            hashCode = (hashCode * 31 + ord(char)) & (2**32 - 1) # unsigned
            if hashCode & 2**31:
                hashCode -= 2**32 # make it signed
        return hashCode

def main():
    input_str = sys.argv[1]
    java_hash_str = JavaHashStr(input_str)
    print(f"包名'{input_str}'的hashCode是：{hash(java_hash_str)}")

if __name__ == "__main__":
    main()
