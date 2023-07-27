import shutil
import os
from PIL import Image        #you have to intall pillow module to run the programme
c_username=os.getlogin()

if os.path.isfile('C:/Users/'+c_username+'/AppData/Local/wlp/wlu.txt')==True:
        os.chdir('C:/Users/'+c_username+'/AppData/Local/wlp')
        file=open('wlu.txt','r')
        lastf=(file.read())
        lasttime=float(lastf)
        file.close()
else:
        lasttime=float(0)
        os.makedirs('C:/Users/'+c_username+'/AppData/Local/wlp')
        
Assets='C:/Users/'+c_username+'/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
saveto='C:/Users/'+c_username+'/Pictures/G_Wallpapers'
if os.path.isdir(saveto)==False:
    os.mkdir('C:/Users/'+c_username+'/Pictures/G_Wallpapers')
os.chdir(Assets)
folderlist=os.listdir()
os.chdir(saveto)
j=0
newtime=lasttime

for i in folderlist :
    oldln=Assets+'/'+i
    img=Image.open(oldln)
    filectime=os.path.getctime(oldln)
    if img.width==1920 and img.height==1080 and (filectime>lasttime) and os.path.isfile('wallpaper'+str(j)+str(filectime)+'.jpg')==False:
        shutil.copy2(oldln,saveto)
        os.rename(saveto+'/'+i,'wallpaper'+str(j)+str(filectime)+'.jpg')
        j=j+1
        if filectime>newtime:
            newtime=filectime
print("You have already downloded the latest wallpapers") if j==0 else print("Successfully downloaded ",j," wallpapers")
os.chdir('C:/Users/'+c_username+'/AppData/Local/wlp')
savefile=open('wlu.txt','w+')
savefile.write(str(newtime)) 
