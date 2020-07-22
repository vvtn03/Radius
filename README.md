# Parser.py and Output.json 

Parser.py is the Main Python file
So Basically We Require Name Address and Phone Number from The HTML File
So Using Beautiful Soup Library in Python The contents of The HTML has been Parsed

So Only Uselful Elements of HTML file(Considering Details of Name,Email and Phone Number) has been Taken into Consideration
So all the <td> </td> Elements are Taken into consideration as a LIST in python 

Once the List is Taken I have Found out The Email name and Phone number Indices On the List 
AS it was Only 1 Email 1 Name and 1 Phone Number i used it Directly
If we have Multiple Names and Email IDs we can Use REGEX in Python to perform That

After Taking that I have Stored it Back again onto a New Tuple after Extracting the Name,Email and Phone
Using import Json in Python I have Converted That Tuple into Json and i have Stored That Seperately in Output.json File

Few More Points: You need to install requests and beautiful soup using
pip install requests
pip install beautifulsoup4

and Requests Basically takes the external website like
r=requests.get("http://www.google.cpm") for an example
But Here I have Modified and Im accessing the Local File in python BeautifulSoup

HERE I HAVE ONLY GIVEN THE JSON FOR NAME,ADDRESS AND PHONE NUMBER AND ALSO SPECIFIC CASE,
Generic Case We can Use REGEX 

I have Attached Parser.py,Output.json Along with the Given HTML File

Thanks

