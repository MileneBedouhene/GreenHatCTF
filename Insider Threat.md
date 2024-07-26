## Challenge Description:

-   Name: Insider Threat
-   Points: 500
-   Description: "During your journey as SOC Analyst, you noticed Suspicious Traffic."

## Tools and Techniques:

-  to solve this challenge you must be very observant and be able to do python scripts.
-  CyberChef

## Solution:
1.  **Initial Approach**
   
    -  When I opened the web_log.txt file I tried to understand the default format of web logs
    -  then I looked for suspicious traffic that can be found in the web logs like : page acces methods, SQL injections, referers path ...

2.  **Detailed Solution**

    -  I made a python script to extract all suspicious traffic from the web_logs.txt file and put them in other files by category.
    -  I tried to analyze each file separately and see if there were any anomalies in the format of the web logs.
    -  I noticed an anomaly in the referer paths file especially when the referer path = "/comment.php" here was a part that was added even though it is not in the default format
      like this :

          "192.168.1.100 - - [10/Jul/2024:20:52:24 +0200] "GET /comment.php?f=21b475f4938f8e1b155e9 HTTP/1.1" "https://www.microclub.dz"......"

          "192.168.1.10 - - [10/Jul/2024:20:58:41 +0200] "GET /comment.php?l=3bb7a9dc0456002bc84911b117e617c8200909634fec5ccfdc" 200 50 HTTP/1.1" "https://www.microclub.dz"......"

          "192.168.1.10 - - [10/Jul/2024:21:03:06 +0200] "GET /comment.php?a=89504e470d0a1a0a0000000d494844520000008b0000028808" 200 50 HTTP/1.1" "https://www.microclub.dz"......"

          "192.168.1.10 - - [10/Jul/2024:21:12:14 +0200] "GET /comment.php?g=f883c5c1f1f517c1633cdf3b79cdaf82e5ed88f5377ec02063" 200 50 HTTP/1.1" "https://www.microclub.dz"......"

    -  So I made another python script to isolate the web log whose referer path = "/comment.php".
    -  I analyzed again the format of the web log in the new file and I noticed that there were only 2 ip addresses when the ip address = "192.168.1.10" the web log was correct
      but when the ip address ="192.168.1.100" there was the "server response code" and "bytes received" fields which were missing.
    - I made another python script to extract the web logs which only contain this ip-address = "192.168.1.10" and from that I also separated the weblogs according
      to "f", "l", "a", "g" , and I also output only the alphanumeric character which is written just after in separate files
    - I took each file and copied its contents into cyberchef using magic and I had at the output 4 images, each of them contained a part of the flag

## Flag:
"microCTF{w3B_L0g$_4n41yz3R}"
