class ThailandPackage:
    def detail(self):
        print("[Thailand package 3/5] travel $800")

if __name__ == "__main__":
    print("execute Thailand module directly")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("execute Thailand module externally")
