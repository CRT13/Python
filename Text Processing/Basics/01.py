""" Python3: Rename bulk files with similar filenames """
import os
os.chdir(r'path/to/directory')
for f in os.listdir():
    f_name,f_ext = os.path.splitext(f)          # f_name = 'noname(N)',f_ext = '.gif'
    f_num = f_name.strip()[6:]			# f_num = '(N)'
    f_num = f_num.strip()[1:-1].zfill(2)	# f_num = 'N'
    new_name = 'tcs{}{}'.format(f_num,f_ext)    # new_name = 'tcsN.gif' 
    os.rename(f,new_name)

"""
Note:
  1. Useful when multiple downloads are made to get files of similar names.
     eg. noname.gif,noname(1).gif,noname(2).gif,...
      Above script renames 'noname(N).gif' to 'tcsN.gif', where N is 2-digit in precision.
  2. zfill(n) gives n-digit precision
     n=2 => 00,01,...,99
     n=3 => 000,001,...,999
     So, choose accordingly.
"""
