#!/bin/python3

import math
import os
import random
import re
import sys
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    from datetime import datetime as dt


    fmt = '%a %d %b %Y %H:%M:%S %z'
    for i in range(int(input())):
        print(int(abs((dt.strptime(input(), fmt) - 
                    dt.strptime(input(), fmt)).total_seconds())))

# After lot's of trying i finally saw the soultion 
# Learnings : we can use modules also in hackerank 
