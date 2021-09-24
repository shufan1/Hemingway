
with open("HemingwayBook/WinnerTakeNothingBook.txt","r") as f:
    contents = f .read()
    
stories = contents.split('\n\n\n\n') # split file by chapter


outputfile = open("input.txt", "w")

chunck_texts = []
for story in stories:
    print("here")
    lines = story.split("\n")
    j = 0
    for line in lines:
        if (len(line)>50):
            break
        j += 1
    for k in range(j, len(lines), 6):
            text = " ".join(lines[k:k+6])
            text += "\n"
            outputfile.writelines(text)


    