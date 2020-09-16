# bot_ig
IG bot for uploading my concert and travel photos to different accounts.   

The script takes the date information, and if it is Monday, Wednesday, Friday or Saturday it changes the caption and hashtags that the photo will have. It access a txt file with 4 lines, each line has a number and the number it reads is the photo it will upload.    
Photos should be name like: 1.jpg, 2.jpg, 3.jpg and so on.   
The first line in the txt file is for Mondays, second for Wednesday, third for Fridays and fourth for Saturdays.   
On Fridays, it selects a line(from 1-2) base on if the number is odd or even.

Inside the folder there is a script for adding white frames to the pictures, due to fact that capture one doesn't have that feature.   
One script is for making an app with Automator in OSX and the other script is for running it and add white frames to a batch of files in a folder.   
Both scripts, have different border size if the picture is vertical or horizontal.

## TODO:

- [ ] Databases for pictures in drive   
- [ ] Updating database after picture upload   
- [ ] user tags   


------------------------------------------------------------------------------------------------------------------------------------

# bot_tw

Twitter bot for uploading some quotes or thoughts.   
No need for continuing since Twitter already schedule posts.
