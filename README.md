# Announcement_Board

### Project Description:
Announcement Board website allows users to publish text announcements. It contains several features: A page where users can create, read and delete an announcement on the same page, a simple UI design with a headline, create, periods and announcements sections.

### How it works:
1. In the create announcement section, the user can write a text for the announcement that he/she would like to make and then press the **Create** button to create a new announcement.
2. The new announcement will appear on a card in the announcement section where the announcements are sorted by newest to oldest.
3. Every announcement card will have **Announcement Text**, **Delete Button** and **Announcement Date**.
4. If the user wants to view the announcements in a specific period of time, he/she can press:
   * **All**: Show all announcements.
   * **Today**: Show created announcements in the last 24 hours.
   * **Last 7 days**: Show created announcements in the last week.
   * **Last 30 days**: Show all announcements in the last month.  
6. If the user wants to delete an announcement, he/she can press the **Delete** button, a confirmation message will popup, press **ok** and the announcement will be deleted. 

### Run and installation:
* ***note: Before you start the installation process for the project, you need to have python already installed on your operating system.***
* Download and Extract the project **zip file** in your desired directory.
* Run **Command Prompet** and Navigate to the file's location: `cd <file_Path>`
* Install required libraries to run the project: `pip install -r requirements.txt`. 
* Start the local server to run the website: `py manage.py runserver`
* You will see that the local server had started, copy the **URL** and paste it into your browser.
* ***note: There are already built-in announcements to test the website***   

### Way to improve:
* Better Front-end Design.
* Add Edit functionality to modify an announcement.
* authentication/authorization for each user.
* Profile page for the user where he/she can find its own announcements with the ability to make changes on them or create new ones.
* The user could add different types of files to the announcement (image - videos..etc).
* Reply Functionality: The user can reply to an announcement.
