# TeachAdminBalancer User's Manual

This user manual is intended to familiarise users with the backend operations, and does not contain technical documentation or flowcharts.
For more technical information, please see the panel report and readme.md.

Render:  https://teachadminbalancer-aberdeen.onrender.com

UserName: **admin**  
PassWord: **123**

# Catalogue Introduction

 1. **StaffvModules**
"StaffvModules" is a module for managing basic information about courses, programmes, administrative roles and school roles. The module provides a list of staff associated with each piece of information, as well as all the "HS" shared statistics associated with the staff member. In addition, "StaffvModules" provides a full-screen mode, which can be accessed with a double-click to easily modify basic information.
 
 3. **Staff**
 "Staff" is a module used to maintain basic information about faculty and staff. It not only provides a comprehensive overview of staff information, but also allows users to associate and bind specific staff members to courses, programmes, administrative roles and school roles.
 
 4. **TotalWork**
  The TotalWork module provides a comprehensive display of staff workload distribution and availability. All information displayed is based on real-time data from the system database.
  
 5. **Course Infomation**
 Visit the Course Information page to view a table containing details of various courses. The table displays the course categories and their corresponding parameter matches such as alpha, beta, and other relevant details.
 
 6. **User Management**
 The user management module enables comprehensive management of users. It allows users to perform search queries and can view a user's recent activity history. In addition, the module provides functions such as adding new users, viewing the activity history of a specific user, editing user information, deleting users, and modifying user access rights, which ensures precise control of user information and user rights and meets diversified management needs.
 
 8. **Setting**
User settings module, you can set the default permissions for the back-office administrator roles of Manager, Employee and IT Administrator.

# Quick Guide

## 1.New staff
Click on "add" in the upper right corner.
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230724033943.png?raw=true)

## 2.Edit and delete staff
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/3.png?raw=true)

## 3.New Basic information on courses, programmes, administrative roles, school roles, etc.
Click on "add" in the upper right corner.
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/20230724034529.png?raw=true)

## 4.Editing and deleting basic information such as courses, programmes, administrative roles and school roles
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/4.png?raw=true)

## 5.View basic information about courses, programmes, administrative roles and school roles Corresponding staff-list
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/5.png?raw=true)

## 6.View and edit basic information such as courses, programmes, administrative roles and school roles Corresponding large screen version

6.1 View the corresponding large screen version
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/6.png?raw=true)
6.2 Double-click on the grid to edit it and save it
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/7.png?raw=true)
6.3 Save Success Tip
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/8.png?raw=true)

## 7.Bind staff to courses, projects, admin roles and school roles
7.1 In the staff module, click on the person's name
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/9.png?raw=true)

7.2 Click "add new one" to add a new row of data, please fill in the code correctly.
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/10.png?raw=true)

7.3 Total hours is automatically generated according to the formula 
`Total_hours = credits * (alpha * delta + beta * numStudents) * share + coordinator`
”remove“ will remove a line
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/11.png?raw=true)

7.4 Click "save" to save the binding information successfully
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/12.png?raw=true)

7.5 Total summary information

       1.Total hours permitted = staff Details of "Adjusted Max"
        
       2.Total hours allocated = course total hours + project total hours + admin role total hours + school total hours + uni total hours
        
       3.Total left = Total hours permitted - Total hours allocated**
        
       4.Total_hours = credits * (alpha * delta + beta * numStudents) * share + coordinator

![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/13.png?raw=true)

## 8.Download totalwork information
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/14.png?raw=true)

![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/20.png?raw=true)

## 9.Managing user information
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/15.png?raw=true)

## 10.Viewing user logs
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/16.png?raw=true)

The log contains information such as staff_id, operation log, etc.
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/17.png?raw=true)

## 11.Permission Related
Default permissions for each role can be edited in the setting module
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/18.png?raw=true)

Take the test account as an example, if you don't have permission, you will get the following page
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/19.png?raw=true)
