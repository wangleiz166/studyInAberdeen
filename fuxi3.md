# A. Explain the role of coupling and cohesion between components. 
### 先解释高内聚/内聚， 会使项目代码怎么样，根据场景举个例子，最后总结说应该使用高内聚
1.Cohesion: High cohesion means in component ，one component does one job.  This makes our project code easier to read, fix, and reuse. For example：XXXXX.,so wo should try to use  High cohesion in project.

### 先解释耦合，会使项目代码怎么样，根据场景举个例子，最后总结说应该使用低耦合
2.Coupling: Coupling is about how much components depend on each other. Low coupling means each components doesn't depend on the others too much. This makes our project code easier to fix and grow. For example, if we get information through an interface, it doesn't matter if we change the database (like from MySQL to MongoDB), as long as the interface data stays the same.,so wo should try to use  low Coupling in project.


# B. What might you do to enable a continuous integration and continuous delivery pipeline for the application?


1.Use a version control system like Git to manage code.

2.Set up an auto build system, such as npm, Jenkins.

3.Write auto test cases, including unit tests, integration tests, and end-to-end tests, to ensure the application work well.

4.Configure automatic deployment tools, like Dockers, Kubernetes, to auto deploy the built application to the environment.

5. monitor and watch alarm, timely feedback problems in the application, such as ELK (Elasticsearch, Logstash, Kibana).

# C. What role would testing play in the application?

1.Verify the functions if right.

2.Discover and fix .

3.Improve software quality.

4.Improve user experience.

5.Reduce fix costs.

# D. Explain how you use retrospectives at the end of a sprint.

1.Think about what happened in the last Sprint.
2.Think about why problems happened.
3.Make a plan to do better.
4.Set goals and make a plan to reach them.
5.Keep track of how we're doing.
6.Be open and honest with each other.

By talking about how we did at the end of each Sprint, we can keep learning and getting better, which helps us work more efficiently and make better software.
