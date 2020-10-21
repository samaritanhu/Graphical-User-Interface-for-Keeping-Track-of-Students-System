# Graphical User Interface for Keeping Track of Students System

Course project for swe243p, Lab A Database program at University of California, Irvine. This system keeps track of students, courses, and their schedules. The program should create a database to keep track of all of this data. It provide a user interface: this interface can be a command-line interface or a graphical user interface. The interface should

- allow new students to enroll into the program,
- new courses to be introduced,
- students to enroll in courses,
- querying to see which students are in each course, 
- querying to see which courses each student is in,
- querying to see which courses and what times each course is for a given student on a given day of the week.

## Getting Started

Packages

```shell
Python3.5 or higher
mysql-connector-python-8.0.22
pandas
wxpython
```

To get the connectors, please reference this website:

```
https://dev.mysql.com/downloads/connector/python/
```

Here I recommend to download MySQL Workbench, and its installing process can refer to ***Murach's MySQL (2nd or 3rd edition)***

The possibilities are endless.

### Building the Application

Now that it's time to build your application by the simple command `load_db()`:

```python
def load_db():
    # choose your own database
    stu_db = DB('stu')
    # if your database doesn't exist, create them
    stu_db.select(TABLE_STU)
    stu_db.select(TABLE_COURSE)
    stu_db.select(STU_TABLE_COURSE)
    # logger can keep the process of your program
    logger.info("Tables are created;")
```

Yep. That's it. You should see the following output:

```
2020-10-20 21:10:52,401	Main function	INFO	Tables are created;
```

### Deploying

After loading your own database, it's time to deploy your Graphical User Interface. By running `demo()` you can deploy your application absolutely nowhere.

```python
from gui.DBFramework import demo
if __name__ == '__main__':
    load_db()
    demo()
```

It's that simple. And then you can try every button exists in the Graphical User Interface:

![demo_picture](D:\study\00.MSWE\swe243p\Module5\demo_picture.png)



## Contributing

Thanks for contributions by master students, teaching assistants, and professors at Information and Computer Science, University of California, Irvine.

 