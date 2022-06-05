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
***Note: Before you start the installation process of the project, you need to have python>=3.7 already installed on your operating system.***
1. Download and extract the project **zip file** in your desired directory.
2. From your terminal, navigate to the file's location: `cd <file_Path>`
3. Install required libraries to run the project: `pip install -r requirements.txt`. 
4. Start the local server to run the website: `py manage.py runserver`
5. After the server starts, copy the **URL** and paste it into your browser.
***Note: For testing, there are already built-in announcements.***   

### Improvment points:
* Better Front-end design.
* Add "edit" feature to modify an announcement.
* Authentication/Authorization.
* Profile page for users where they can find their own announcements with the ability to modify them or create new ones.
* Users could add different types of files to the announcement (image - videos..etc).
* Reply feature: The user can reply to an announcement.
