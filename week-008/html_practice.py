import webbrowser

var1 = open("file_hello_world.html", "w")

file_content = '''

<html>
<head></head>
<body>
<p> 
<h1>
Hello World!
</h1>
 </p>
<style>
img {
  width: 50%;
  height: auto;
}
</style>
<img src="https://img5.goodfon.com/original/2000x1400/9/4f/ozero-iaponiia-listia-osen-gora-fudzi.jpg" alt="Italian Trulli">
</body>
</html>

'''

var1.write(file_content)

var1.close()

webbrowser.open_new_tab("file_hello_world.html")