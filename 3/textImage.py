#Chalenge is Bitmap Message, by Al Sweigart al@inventwithpython.com, Display a text message according to the provided bitmap image
#open file for image, get contents and close file
fi = open('3/pictureText.txt')
image = fi.read()
fi.close()

#get text to use for displaying over message
txt = input('Enter text to display in image\n')
#if no message entered then just exit
if txt == '':
    exit()
cur = 0
for line in image.splitlines():
    for pixel in line:
        #if space is blank, leave it blank
        if pixel == ' ':
            print(' ' ,end='')
        else:
            #if space is not plank print next character in text chosen by user
            try:
                print(txt[cur],end ='')
                cur += 1
            except:
                print(txt[0], end = '')
                cur=1
    #print newline at end of each line of characters
    print('\n', end='')