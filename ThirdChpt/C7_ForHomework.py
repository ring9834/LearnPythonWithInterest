#使用python做作业

#让用户输入一个数学问题
problem = input("Please input one maths question or equation you want to solve，press 'q' button to exit：")

#继续输入，除非输入'q'而退出
while(problem != "q"):
    print("Question",problem,"'s result is'：",eval(problem))                   #显示提出的问题（公式），并显示答案
    problem = input("Please input one maths question or equation you want to solve，press 'q' button to exit：")   #提示用户继续输入问题或公式
