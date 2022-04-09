#/bin/bash

if command -v gimp >/dev/null 2>&1; 
then
    echo GIMP found!

	if command -v git >/dev/null 2>&1; 
	then
    	echo Git found!
    	echo Installing GIMPshop Reloaded!
    	git clone https://github.com/cttynul/gimpshop-reloaded.git ~/.gimpshop-temp 
    	rm -f ~/.gimpshop-temp/gimprc
    	cp -r ~/.gimpshop-temp/. ~/.gimp-2.8
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
