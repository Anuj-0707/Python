def check_for_line(word):
    data = True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            else:
                print("-1")
            line_no+=1
word=input("Enter a word to found : ")
check_for_line(word)