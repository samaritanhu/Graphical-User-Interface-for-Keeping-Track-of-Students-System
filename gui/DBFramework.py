import wx
from utils.db import DB
from resources.query import *
import random
from utils.df import named_tuple2df


def demo():
    stu_db = DB('stu')
    app = wx.App()
    frame = wx.Frame(None, title="Keeping Track of Students System", size=(1200, 800))

    panel = wx.Panel(frame)  # Create Panel

    def enroll_stu_program(event):
        student_name = tc_stu_na.GetValue()
        student_id = tc_stu_id.GetValue()
        if student_id == "":
            student_id = random.randint(1000000000, 2000000000-1)
        stu_db.execute(INSERT_STU % (str(student_name), int(student_id)))
        output.AppendText('Successfully Inserted student %s, generated student id %d!\n' % (student_name, student_id))

    def introduce_course(event):
        course_id = tc_cou_id.GetValue()
        course_name = tc_cou_na.GetValue()
        course_time = tc_cou_ti.GetValue()
        course_week = tc_cou_wd.GetValue()
        if not course_name or not course_time or not course_week:
            output.AppendText('Course Information is missing! Please fill in the blanks\n')
        else:
            if course_id == "":
                course_id = random.randint(0, 1000000000 - 1)
            stu_db.execute(INSERT_COURSE % (int(course_id), str(course_name),str(course_time)+':00', int(course_week)))
            output.AppendText('Successfully Inserted course %d, %s!\n' % (int(course_id), str(course_name)))

    def stu_choose_course(event):
        student_id = (tc_stu_na2.GetValue())
        course_id = (tc_cou_id2.GetValue())
        if not student_id and not course_id:
            output.AppendText('Course or Student Information is missing! Please fill in the blanks\n')
        else:
            stu_db.execute(INSERT_STU_COURSE % (int(student_id), int(course_id)))
            output.AppendText('Student %d successfully enrolled in course %d!\n' % (int(student_id), int(course_id)))

    def searching1(event):
        student_name = tc_stu_na3.GetValue()
        student_id = tc_stu_id3.GetValue()
        if not student_id and not course_id:
            output.AppendText('Student Information is missing! Please fill in the blanks\n')
        else:
            if student_id:
                res = stu_db.select(SEARCH_COURSE1 % (int(student_id)))
            elif student_name:
                res = stu_db.select(SEARCH_COURSE2 % (str(student_name)))
            output.AppendText('Student %s\'s course information\n' % (str(student_name), ))
            output.AppendText((named_tuple2df(res)))

    def searching2(event):
        course_name = tc_cou_na3.GetValue()
        course_id = tc_cou_id3.GetValue()
        if not course_name and not course_id:
            output.AppendText('Course Information is missing! Please fill in the blanks\n')
        else:
            if course_id:
                res = stu_db.select(SEARCH_STU1 % (int(course_id)))
            elif course_name:
                res = stu_db.select(SEARCH_STU2 % (str(course_name)))
            output.AppendText('Course %s\'s course information\n' % (str(course_name), ))
            output.AppendText((named_tuple2df(res)))

    def searching3(event):
        student_id = tc_stu_id4.GetValue()
        course_weekday = tc_course_we1.GetValue()
        if not student_id and not course_weekday:
            output.AppendText('Student or course Information is missing! Please fill in the blanks\n')
        else:
            res = stu_db.select(SEARCH_STU_COURSE % (int(student_id), int(course_weekday)))
            # output.AppendText('Course %s\'s course information\n' % (str(student_id), ))
            output.AppendText((named_tuple2df(res)))

    but1 = wx.Button(panel, label="Enroll")  # panel as parent
    but2 = wx.Button(panel, label="Introduce")
    but3 = wx.Button(panel, label="Enroll")
    but4 = wx.Button(panel, label="Search")
    but5 = wx.Button(panel, label="Search")
    but6 = wx.Button(panel, label="Search")

    box = wx.StaticBox(panel, label="Tips: Please fill in as many boxes as possible to get the best results! ")
    sbsizer = wx.StaticBoxSizer(box, wx.VERTICAL)

    # 声明尺寸器
    fgs = wx.FlexGridSizer(rows=7, cols=6, vgap=9, hgap=25)
    hbox = wx.BoxSizer(wx.HORIZONTAL)

    # 给尺寸器添加组件
    fuc_1 = wx.StaticText(panel, label="1. Enroll New Students: ", style=wx.ALIGN_RIGHT)
    stu_na = wx.StaticText(panel, label="Student Name", style=wx.ALIGN_RIGHT)
    stu_id = wx.StaticText(panel, label="Student ID (Optional)", style=wx.ALIGN_RIGHT)

    blk = wx.StaticText(panel, label="", style=wx.ALIGN_RIGHT)
    blk2 = wx.StaticText(panel, label="", style=wx.ALIGN_RIGHT)
    blk3 = wx.StaticText(panel, label="", style=wx.ALIGN_RIGHT)
    blk4 = wx.StaticText(panel, label="", style=wx.ALIGN_RIGHT)

    fuc_2 = wx.StaticText(panel, label="2. Introduce New Courses: ", style=wx.ALIGN_RIGHT)
    course_id = wx.StaticText(panel, label="Course ID (Optional)", style=wx.ALIGN_RIGHT)
    course_n = wx.StaticText(panel, label="Course Name", style=wx.ALIGN_RIGHT)
    course_time = wx.StaticText(panel, label="Course Time (HH:MM)", style=wx.ALIGN_RIGHT)
    course_weekday = wx.StaticText(panel, label="Course Weekday (1-7)", style=wx.ALIGN_RIGHT)

    fuc_3 = wx.StaticText(panel, label="3. Student enroll courses: ", style=wx.ALIGN_RIGHT)
    stu_na2 = wx.StaticText(panel, label="Student ID", style=wx.ALIGN_RIGHT)
    course_id2 = wx.StaticText(panel, label="Course ID", style=wx.ALIGN_RIGHT)

    fuc_4 = wx.StaticText(panel, label="4. See which courses each student is in: ", style=wx.ALIGN_RIGHT)
    stu_na3 = wx.StaticText(panel, label="Student Name", style=wx.ALIGN_RIGHT)
    stu_id3 = wx.StaticText(panel, label="Student ID", style=wx.ALIGN_RIGHT)

    fuc_5 = wx.StaticText(panel, label="5. See which students are in each course: ", style=wx.ALIGN_RIGHT)
    course_id3 = wx.StaticText(panel, label="Course ID", style=wx.ALIGN_RIGHT)
    course_na3 = wx.StaticText(panel, label="Course Name", style=wx.ALIGN_RIGHT)

    fuc_6 = wx.StaticText(panel, label="6. See which courses and what times each course: ", style=wx.ALIGN_RIGHT)
    stu_id4 = wx.StaticText(panel, label="Student ID", style=wx.ALIGN_RIGHT)
    course_we1 = wx.StaticText(panel, label="Weekday (1-7)", style=wx.ALIGN_RIGHT)

    output = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

    tc_stu_na = wx.TextCtrl(panel)
    tc_stu_id = wx.TextCtrl(panel)
    tc_cou_id = wx.TextCtrl(panel)
    tc_cou_na = wx.TextCtrl(panel)
    tc_cou_ti = wx.TextCtrl(panel)
    tc_cou_wd = wx.TextCtrl(panel)

    tc_stu_na2 = wx.TextCtrl(panel)
    tc_cou_id2 = wx.TextCtrl(panel)

    tc_stu_na3 = wx.TextCtrl(panel)
    tc_cou_id3 = wx.TextCtrl(panel)
    tc_stu_id3 = wx.TextCtrl(panel)
    tc_cou_na3 = wx.TextCtrl(panel)

    tc_stu_id4 = wx.TextCtrl(panel)
    tc_course_we1 = wx.TextCtrl(panel)

    fgs.AddMany(
        [(fuc_1, 0, wx.ALIGN_RIGHT),
         (stu_na, 0, wx.ALIGN_RIGHT), (tc_stu_na, 0, wx.SHAPED),
         (stu_id, 0, wx.ALIGN_RIGHT), (tc_stu_id, 0, wx.SHAPED),
         (but1, 0, wx.ALIGN_RIGHT),

         (fuc_2, 0, wx.ALIGN_RIGHT),
         (course_id, 0, wx.ALIGN_RIGHT), (tc_cou_id, 0, wx.SHAPED),
         (course_n, 0, wx.ALIGN_RIGHT), (tc_cou_na, 0, wx.SHAPED),
         (blk, 0, wx.EXPAND),

         (blk2, 0, wx.EXPAND),
         (course_time, 0, wx.ALIGN_RIGHT), (tc_cou_ti, 0, wx.SHAPED),
         (course_weekday, 0, wx.ALIGN_RIGHT), (tc_cou_wd, 0, wx.SHAPED),
         (but2, 0, wx.ALIGN_RIGHT),

         (fuc_3, 0, wx.ALIGN_RIGHT),
         (stu_na2, 0, wx.ALIGN_RIGHT), (tc_stu_na2, 0, wx.SHAPED),
         (course_id2, 0, wx.ALIGN_RIGHT), (tc_cou_id2, 0, wx.SHAPED),
         (but3, 0, wx.ALIGN_RIGHT),

         (fuc_4, 0, wx.ALIGN_RIGHT),
         (stu_na3, 0, wx.ALIGN_RIGHT), (tc_stu_na3, 0, wx.SHAPED),
         (stu_id3, 0, wx.ALIGN_RIGHT), (tc_stu_id3, 0, wx.SHAPED),
         (but4, 0, wx.ALIGN_RIGHT),

         (fuc_5, 0, wx.ALIGN_RIGHT),
         (course_na3, 0, wx.ALIGN_RIGHT), (tc_cou_na3, 0, wx.SHAPED),
         (course_id3, 0, wx.ALIGN_RIGHT), (tc_cou_id3, 0, wx.SHAPED),
         (but5, 0, wx.ALIGN_RIGHT),

         (fuc_6, 0, wx.ALIGN_RIGHT),
         (stu_id4, 0, wx.ALIGN_RIGHT), (tc_stu_id4, 0, wx.SHAPED),
         (course_we1, 0, wx.ALIGN_RIGHT), (tc_course_we1, 0, wx.SHAPED),
         (but6, 0, wx.ALIGN_RIGHT),
        ])

    # 设置索引列1，3为自动增长列
    fgs.AddGrowableCol(1, 1)
    fgs.AddGrowableCol(3, 1)
    fgs.AddGrowableCol(5, 1)

    but1.Bind(wx.EVT_BUTTON, enroll_stu_program)
    but2.Bind(wx.EVT_BUTTON, introduce_course)
    but3.Bind(wx.EVT_BUTTON, stu_choose_course)
    but4.Bind(wx.EVT_BUTTON, searching1)
    but5.Bind(wx.EVT_BUTTON, searching2)
    but6.Bind(wx.EVT_BUTTON, searching3)

    sbsizer.Add(fgs, 1, wx.EXPAND)
    sbsizer.Add(output, 1, wx.EXPAND)
    hbox.Add(sbsizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
    panel.SetSizer(hbox)

    frame.Show()  # 因为文本组件和按钮组件都是以窗框组件为父组件，所以只需要调用frame
    app.MainLoop()


if __name__ == '__main__':
    demo()