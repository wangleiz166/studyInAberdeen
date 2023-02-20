### Key Principles of OOP  //OOP关键原则:

    1.Encapsulation& Information Hiding //封装&信息隐藏
    
			It must be possible to define a unit that contains data and the subprograms that access (manipulate) it.
			//必须能够定义一个包含数据和访问（操作）数据的子程序的单元。
			Hiding implementation details of an  object from things that interact with it.
			//向与之交互的事物隐藏对象的实现细节。
			Separates external view (behaviour) from internal view (state).
			//将外部视图（行为）与内部视图（状态）分开。
	
    2.Abstraction //抽象
    
			An abstraction is a view or representation of an entity that includes only its most essential properties 
			//抽象是一个实体的观点或代表，只包括其最基本的属性 
	
    3.Inheritance //继承
    
			Subsumption provides the ability to create subclasses.
			//子类提供了创建子类的能力。   
			Subclasses share the structure and/or behaviour of the parent class.
			// 子类共享父类的结构和/或行为
			Inheritance from one class (single inheritance) ormore than one (multiple inheritance).
			//继承自一个类（单继承）或多个类（多继承）。
			
    4.Association, Composition & Aggregation  //关联、组成和聚集
    
			Association
			Simplest relationship.One class uses functionalities provided by another.
			// 最简单的关系。一个类使用另一个类提供的功能。
			Composition (part-of)
			Implies a relationship where the child class cannot exist without the parent.
			//意味着一种关系，即子类不能离开父类而存在。
			Aggregation (has-a)
			Implies a relationship where the child can exist independently of the parent
			//意味着一种关系，即子类可以独立于父类而存在
			
	5.Polymorphism //多态
	
			Method Overloading // 方法重载
			A class with two or more methods having the same name, but different lists of arguments and different behaviours.
			// 一个类有两个或多个名字相同的方法，但有不同的参数列表和不同的行为。
			Subtyping//子类型化
			Allows a method to be written to take an object of a certain class B, but also work correctly if passed an object that belongs             to a class S that is a subclass of B.
			// 允许编写一个方法来接收某个类B的对象，但如果传递一个属于B的子类S的对象，该方法也能正常工作。

	
### Method Overriding

Besides inheriting methods as is, a class can modify an inherited method 
//除了按原样继承方法外，一个类还可以修改继承的方法 
The new one overrides the inherited one – this is method overriding
//新的方法覆盖继承的方法--这就是方法覆盖

### Multiple Inheritance
Powerful mechanism to allow subclasses to inherit from multiple parents classes.
//强大的机制，允许子类从多个父类继承。

### Objects in Software 
Objects
    
    1.collection of data and associated behaviours //数据和相关行为的集合。
    
    2.reusable software components that model real-world items //可重复使用的软件组件，用于模拟真实世界的项目。
    
    3.Object-oriented programming ：Programming that models complex systems in terms of a collection of interacting objects 
	//面向对象的编程：用交互式对象的集合来模拟复杂系统的编程

### Elements of classical procedural (imperative) programming: //经典的程序性（命令式）编程的要素

    1.Data - which was completely passive //数据--这完全是被动的
    
    2.Procedures (functions) - which could manipulate the data //程序（函数）--可以对数据进行操作
    

### How do we differentiate between different types of objects：Class

    1.Used to describe objects //用于描述物体
    
    2.Like blueprints for creating an object //像创建一个物体的蓝图

### Object-Oriented Concepts/Terminology  // 面向对象的概念/术语 

    1.Fundamental building blocks are called	：classes 
	//基本的构建模块被称为：类 
    
    2.Class instances are called ：objects or instances
	//类的实例被称为：对象或实例
    
    3.Attributes of a class are called	：data members or properties 
	//一个类的属性被称为：数据成员或属性
    
    4.Attributes are used to represent	：state of an object & relationships to other objects
	//属性用于表示：对象的状态和与其他对象的关系
    
    5.Subprograms that define operationson objects are called 	：methods or member functions
	//定义对象操作的子程序被称为：方法或成员函数
    
    6.Calls to methods are called 	：messages 
	// 对方法的调用被称为：消息
	
	7.The attributes & operations provided byan object for others to interact with it is it : public interface
	//一个对象为其他人提供的与之互动的属性和操作就是它：公共接口。
	
	8.A class that inherits is a : derived class or a subclass 
	//一个继承的类是：派生类或子类 
	
	9.The class from which anotherclass inherits is a : base class or superclass 
	//另一个类所继承的类是：基类或超类 
	
	10.When a subclass provides its own versionof an inherited method, this is : method overriding
	//当一个子类为一个继承的方法提供自己的版本时，这就是：方法覆盖
	
	11.A class that declares methods but doesnot implement them is an : abstract class
	//一个声明了方法但没有实现这些方法的类是：抽象类。

### Why OOP?

    1.Reusability//可重用性
    The same code should be usable as a component of different systems in various applications.
    //同样的代码应该可以在不同的应用中作为不同系统的组成部分使用。
    
    2.Adaptability//适应性
    Software needs to be able to evolve over time in response to changing conditions in its environment.
    //软件需要能够随着时间的推移而发展，以应对其环境中不断变化的条件。
    
    3.Robustness//稳健性
    We want software to be capable of handling unexpected inputs that are not explicitly defined for its application.
    //我们希望软件能够处理没有为其应用明确定义的意外输入。
    
