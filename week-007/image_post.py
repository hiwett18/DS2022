import webbrowser

var1 = open("file_hello_world.html", "w")

file_content = '''

<html>
<head></head>
<body>
<p> 

 </p>
<style>
img {
  width: 50%;
  height: auto;
}
</style>
<img src="/Users/hiwot-w/Desktop/Data_Science_Course/hiw-DS2022/DS2022-1/week-007/Screen Shot 2021-11-01 at 10.59.40 AM.png" alt="Italian Trulli">
</body>
</html>

'''

var1.write(file_content)

var1.close()

webbrowser.open_new_tab("file_hello_world.html")