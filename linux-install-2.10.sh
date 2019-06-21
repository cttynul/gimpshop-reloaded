#/bin/bash

if command -v gimp >/dev/null 2>&1; 
then
    echo GIMP found!

	if command -v git >/dev/null 2>&1; 
	then
    	echo Git found!
    	echo Installing GIMPshop Reloaded!
    	git clone git://github.com/cttynul/gimpshop-reloaded ~/.gimpshop-temp 
    	rm -f ~/.gimpshop-temp/gimprc
    	cp -r ~/.gimpshop-temp/. ~/.config/GIMP/2.10
    	echo Removing temp files
    	rm -r -f ~/.gimpshop-temp
    	echo Installation complete! You can now run GIMPshop Reloaded!
    	echo To display dark-theme Photoshop-like you have to choose "New CS6 Themes..." in
    	echo Edit  Preferences  Themes
    	echo 
    	echo Enjoy - cttynul/zegt

    else
    	echo Git is not installed
    	echo Install it using your package manager
    	echo "i.e. (buntu, debian-based) sudo apt-get install git"
    fi
else
    echo GIMP is not installed
    echo Install it using your package manager
    echo "i.e. (buntu, debian-based) sudo apt-get install gimp"
fi
