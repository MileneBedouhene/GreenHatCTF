## Challenge Description:

-   Name: Base64s
-   Points: 500
-   Description: "Where am i hidding hihihi ..."

## Tools and Techniques:
-  To solve this challenge you must be very observant and be able to do python scripts.

## Solution:
1.  **Initial Approach**
   
   -  After accessing the website link that was given to us I directly inspected it.
   -  I found in the element tab an html file whose title is "/" and the <head> tag contained comments which appeared to be base64.
  

2.  **Detailed Solution**

   -   Because the title was "/" which means root, I had the idea of ​​isolating comments in a file and adding them line by line to the path.
   -   I made a python script which takes each comment line and adds it to the access path, on each attempt it displays the HTTP status code
       but if the status code is equal to 200 it must display the content of the answer.
   -   You can find the python script and comments file in the base64s branch.
  
  ## Flag:
"microCTF{Base64s_brUt3_F0Rc3r_Bl439eL}"
