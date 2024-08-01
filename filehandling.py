file =  open('Text file.txt', mode='w')
file.write("created a text file .")
file.close()

print()

file =  open('Text file.txt', mode='w')
file.write("We have again excuted with same write mode. So it will overide the data.")
file.close()

print()