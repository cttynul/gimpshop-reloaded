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
    	cp -r ~/.gimpshop-temp/. ~/.gimp-2.8
    	echo Removing temp files
    	rmdir --ignore-fail-on-non-empty ~/.gimpshop-temp
    	echo Installation complete! You can now run GIMPshop Reloaded!
    	echo To display dark-theme Photoshop-like you have to select "New CS6 Themes..." under
    	echo Edit  Preferences  Themes
    	echo 
    	echo Enjoy - cttynul/zegt

    else
    	echo Git is not installed
    	echo Install it using your package manager
    	echo $ sudo apt-get install git
    fi
else
    echo GIMP is not installed
    echo Install it using your package manager
    echo $ sudo apt-get install gimp
fi
