# IG_BOT
IG bot for uploading my concert and travel photos to different accounts.   

The script takes the date information, and if it is Monday, Wednesday, Friday or Saturday it changes the caption and hashtags that the photo will have. It access a txt file with 4 lines, each line has a number and the number it reads is the photo it will upload.    

Photos should be name like: 1.jpg, 2.jpg, 3.jpg and so on.   

The first line in the txt file is for Mondays, second for Wednesday, third for Fridays and fourth for Saturdays.   
On Fridays, it selects the number from the first or second line, base on if the number in line 4, is odd or even. And uploads the selected line.


#### White Frame
Inside the folder there is a script for adding white frames to the pictures, due to fact that **Capture One** doesn't have that feature. 

One script is for making an app with Automator in OSX and the other script is for running it and add white frames to a batch of files in a folder.   

Both scripts, have different border size if the picture is vertical or horizontal.

### TODO:

- [ ] Databases for pictures in drive   
- [ ] Updating database after picture is uploaded   
- [ ] user tags   


------------------------------------------------------------------------------------------------------------------------------------

# TW_BOT

Twitter bot for uploading some quotes or thoughts.   
No need for continuing since Twitter already schedule posts.
