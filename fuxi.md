## A. As the new person, you’re told that you’ll be working in two-week sprints. What does this look like in practice? 

Working in two-week sprints is a basic practice in Scrum. During the sprint, the development team needs to complete a set of tasks, with each task usually being completed within a day. 

1. At the beginning of the sprint, the team focuses on the goals, starts tasks, performs development and testing, and then evaluates at the end of the sprint to check the completed work and the next steps.
2. Throughout the sprint, team members often have daily stand-up meetings and other forms of cooperation to maintain team communication and cooperation.

So, as a new person, I need to actively participate in the sprint, understand the tasks and team goals, and work with other team members to complete tasks.

## B. This application has a variety of different users. Which type of roles for user stories would you expect to see in the product backlog?

1. Users - Scan codes and see how to recycle, get points and use coupons.
2. Stores - Give coupons, get points from users, and watch how coupons are used.
3. Recycling places - Share recycling info, keep data new and updated.
4. App workers - Make, fix, and update the app.

## C.The application compiles to both iOS and Android versions. Explain which issues you will need to monitor in your programming.

1. Compatibility issues: Since iOS and Android have different parts and setups, we need to make sure the app works well on both systems and devices.
2. App performance issues: The app needs to run fast on phones and handle lots of data, so we must make sure it works well on different platforms.
3. Platform-specific issues: For example, iOS and Android may have different safety rules. We need to learn and follow the safety needs for each system.
4. User experience issues: On different platforms, the look and feel of the app might be different. We need to make sure the app has a good experience for users on all platforms.

## D.Explain the likely architecture of this application.

1. Client-side (Frontend) - Use React Native to make a mobile app that works on different devices, create the look of the app and talk to the server.
2. Server-side (Backend) - Handle user requests, like getting recycling info, managing points, and coupons. Can use different tools like Node.js, Python, Java, PHP, or Golang.
3. Database - Store data the app needs, such as recycling info, user data, points, and coupons. Might use relational databases (like MySQL) or non-relational databases (like MongoDB).
4. RESTful API - Give a standard way for the client and server to talk to each other, so they can share data in an expected way.
5. Barcode scanning library - Built into the app, helps read and understand scanned barcodes.
6. Authentication and authorization - Use technologies like OAuth, JWT to keep user data and privacy safe.
7. Docker - Use Docker containers to set up and run the app, making the app environment more consistent and controllable.
8. Kubernetes (k8s) - Use Kubernetes to manage containers, making the app more scalable and reliable.
9. Cloud services - Might use cloud services (like AWS, Google Cloud Platform, or Microsoft Azure)
