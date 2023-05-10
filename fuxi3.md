# A. Explain the role of coupling and cohesion between components. 

1.Cohesion: High cohesion means each part of our system does one job really well. This makes our system easier to read, fix, and reuse. For example, in Django, each APP does one thing.

2.Coupling: Coupling is about how much parts of our system depend on each other. Low coupling means each part doesn't rely on the others too much. This makes our system easier to fix and grow. For example, if we get information through an interface, it doesn't matter if we change the database (like from MySQL to MongoDB), as long as the interface data stays the same.


# B. What might you do to enable a continuous integration and continuous delivery pipeline for the application?


1.Use a version control system like Git to manage code.
2.Set up an automatic build system, such as npm, Jenkins.
3.Write automated test cases, including unit tests, integration tests, and end-to-end tests, to ensure the correct functionality of the application.
4.Configure automatic deployment tools, like Dockers, Kubernetes, to automatically deploy the built application to the production environment.
5.Implement monitoring and alert mechanisms, so as to detect and solve problems in the application in time, such as ELK (Elasticsearch, Logstash, Kibana).

# C. What role would testing play in the application?

1.Verify the correctness of functions.
2.Discover and fix defects.
3.Improve software quality.
4.Enhance user experience.
5.Reduce maintenance costs.

# D. Explain how you use retrospectives at the end of a sprint.

1.Think about what happened in the last Sprint.
2.Figure out why problems happened.
3.Make a plan to do better.
4.Set goals and make a plan to reach them.
5.Keep track of how we're doing.
6.Be open and honest with each other.

By talking about how we did at the end of each Sprint, we can keep learning and getting better, which helps us work more efficiently and make better software.
