def check_for_word(word):
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")
word=input("Enter a word to find : ")
check_for_word(word)