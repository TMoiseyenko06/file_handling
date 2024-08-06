import os 

def list_directory_contents(path):
    for path, subdirs, files in os.walk(path):
        for name in files:
            print(os.path.join(path, name))

def main():
    path = input("What directory would you like to list?")
    list_directory_contents(path)

if __name__ == "__main__":
    main()