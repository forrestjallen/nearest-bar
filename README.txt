 _______  _______  _______  ______   _______  _______ 
(  ____ )(  ____ \(  ___  )(  __  \ (       )(  ____ \
| (    )|| (    \/| (   ) || (  \  )| () () || (    \/
| (____)|| (__    | (___) || |   ) || || || || (__    
|     __)|  __)   |  ___  || |   | || |(_)| ||  __)   
| (\ (   | (      | (   ) || |   ) || |   | || (      
| ) \ \__| (____/\| )   ( || (__/  )| )   ( || (____/\
|/   \__/(_______/|/     \|(______/ |/     \|(_______/

######################################################

DOCUMENTATION FOR: nearest_bar.py

Dependencies:
To use the nearest_bar.py script first:
	(1) ensure that you are running python3 
	(2) ensure pip3 is installed on your system. Instructions to install pip3 if it is not already installed
	on the system:
		https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3
		 
	(3) install the needed imports by running  "pip3 install xlrd", "pip3 install googlemaps", and "pip3 install xlwt" in your terminal

	(4) IMPORTANT: Get a distance matrix API key from your google maps platform on google cloud. See URL for directions on getting the needed key:
		https://developers.google.com/maps/documentation/distance-matrix/get-api-key

	(5) on line 19 in the script replace 'My API KEY' with the key received key from google.
		e.g. api_key='My API KEY' should now be api_key='<some api key>'

Running the script:
	(1) to run the script enter the following in your terminal: python3 nearest_bar.py
	(2) you will be prompted to enter an xlsx file name, enter the xlsx file name and be sure that it is in the same directory as the script
	(3) IMPORTANT: script will not run correctly if input file does not have columns labeled in the following order:
	    	Number, Street, City, Zip Code, Miles To Nearest Bar
	(4) the script will create an output file prefixed with OUTPUT_ in the same directory as the script!

Thats it!!! feel free to reach out via upwork if you have any questions.

__________         ___________                                   __       _____  .__  .__                 
\______   \___.__. \_   _____/_________________   ____   _______/  |_    /  _  \ |  | |  |   ____   ____  
 |    |  _<   |  |  |    __)/  _ \_  __ \_  __ \_/ __ \ /  ___/\   __\  /  /_\  \|  | |  | _/ __ \ /    \ 
 |    |   \\___  |  |     \(  <_> )  | \/|  | \/\  ___/ \___ \  |  |   /    |    \  |_|  |_\  ___/|   |  \
 |______  // ____|  \___  / \____/|__|   |__|    \___  >____  > |__|   \____|__  /____/____/\___  >___|  /
        \/ \/           \/                           \/     \/                 \/               \/     \/ 
