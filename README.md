![logo](https://raw.githubusercontent.com/cttynul/gimpshop-reloaded/gh-pages/img/logo.png) 

### Introduction 
GIMPshop was a modification of the free and open source graphics program GNU Image Manipulation Program (GIMP), with the intent to replicate the feel of Adobe Photoshop. 
Its primary purpose was to make users of Photoshop feel comfortable using GIMP (en.wikipedia.org)

GIMPshop Reloaded is an original GIMPshop remake, made by someone who had been using Photoshop for seven years! 
GIMPshop Reloaded has an interface similiar to Adobe's product, shortcuts, plugin and much more, everything you need to have a real Photoshop feel.

Soon I will release a portable version of GIMPShop preconfigured :).

![gimpshoprld](https://raw.githubusercontent.com/cttynul/gimpshop-reloaded/gh-pages/img/img-1.png)

### How to install
##### Linux
###### Auto Install
* Download and run bash script from [**here**](https://raw.githubusercontent.com/cttynul/gimpshop-reloaded/master/linux-install.sh) if you're using 2.8
* Download and run bash script from [**here**](https://raw.githubusercontent.com/cttynul/gimpshop-reloaded/master/linux-install-2.10.sh) if you're using 2.10

###### Manual Install

`
$ git clone https://github.com/cttynul/gimpshop-reloaded.git ~/.gimpshop-temp
`

`
$ rm ~/.gimpshop-temp/gimprc
`

Copy `~/.gimpshop-temp` content into `~/.gimp-2.8` if you're using 2.8

Copy `~/.gimpshop-temp` content into `~/.config/GIMP/2.10` if you're using 2.10

`
$ rmdir ~/.gimpshop-temp
`

##### Windows
1) Download using Download Zip

2) Copy all files (not gimp-splash.png) and paste it in

`
C:/Users/(Your User Windows Name)/.gimp-2.8
`

3) Copy and paste gimp-spalsh.png into

`
C:/Users/(Your User Windows Name)/.gimp-2.8/splashes
`

##### MacOS
[Follow this](https://github.com/cttynul/gimpshop-reloaded/issues/1#issuecomment-304475702) 

### Thanks to
- [**rex4539**](https://github.com/rex4539) for MacOS How-To.
- [**epierce**](http://epierce.freeshell.org/gimp/gimp_ps.php) for Photoshop shortcut.
- [**AbdullahRagb**](https://github.com/AbdullahRagb/) for GIMP Theme (gimp-dark-theme)
- [**Mehdi Abdollahi**](#) for GIMP Theme (NEW CS6 II theme for gimp).
- [**Riley Brandt**](http://www.rileybrandt.com/) for some interface fixes.
- [**slybug**](http://slybug.deviantart.com) for layer via copy/cut plugin.

### License
GIMPshop Reloaded is published under GNU General Public License v3.0.
