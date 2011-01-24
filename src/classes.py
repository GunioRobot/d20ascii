import string
import yaml
import subprocess
import os

#classes=yaml.load(file('classes.yaml', 'r'))
#classes=yaml.load(os.popen('cat srd/base-classes/*.yaml', 'r'))
#(classfilesout,classfilesin)=subprocess.Popen3('cat srd/base-classes/*.yaml')

#print '\nread:'
proc = subprocess.Popen('cat src/*/base-classes/*.yaml',
                       shell=True,
                       stdout=subprocess.PIPE,
                       )
classfilesout = proc.communicate()[0]
#print '\tstdout:', repr(stdout_value)


classes=yaml.load(classfilesout)
# print yaml.dump(classes)

def saves(level, quality):
  if (quality == "Poor"):
    return int(level*1/3)
  if (quality == "Good"):
    return int(2+level/2)

def bab(level, quality):
  if (quality == "Poor"):
    return int(level*.5)
  if (quality == "Good"):
    return level
  if (quality == "Medium"):
    return int(level*.75)

def underline(symbol, text):
  print text
  line=""
  for i in text:
    line=line+symbol
  print line
  print

underline("=","Base Classes")

for i in classes:
#for i in classes["Base Classes"]:
#  for k in i:
#    print k
  underline("-",i["Name"])
  underline("~","The " + i["Name"] + " Base Class")
  if (i.has_key("Alignment")):
    print "*Alignment:* "+i["Alignment"]
    print  
  print "*Hit Die:* "+i["Hit Die"]
  print
  underline("^","Class Skills")
  print "*The "+i["Name"]+"'s class skills (and the key ability for each skill) are:* "
  skills = i["Class Skills"].keys()
  skills.sort()
  skillsout=""
#  print str.join(", ",skills)
  for j in skills:
#    print j
    if (i["Class Skills"][j]):
      if (j!="Knowledge"):
        skillsout=skillsout + j + " ("+i["Class Skills"][j]+"), "
      else:
        for k in i["Class Skills"]["Knowledge"]:
          skillsout=skillsout + "Knowledge (" + k + "): (Int), "
    else:
      skillsout=skillsout + j + ", "
  skillsout=skillsout.rstrip(", ")
  print skillsout
  print
  print "*Skill Points at 1st Level:* ("+str(i["Skill Points Per Level"])+" + Int Modifier) x 4."
  print
  print "*Skill Points at Each Additional Level:* "+str(i["Skill Points Per Level"])+" + Int Modifier."
  print
  print ".The " + i["Name"]
  if (i.has_key("Table Format")):
    print "[options=\"header\","+i["Table Format"]+"]"
  else:
    print "[options=\"header\"]"
  print "|====="

#  for k in range(1,21):
#    for j in i["Class Features"]:
#      if (i["Class Features"][j]["Level"]==k):
#        print k,j

# Determine Max Spell Level
  maxspelllevel=-1
  minspelllevel=10
  if (i.has_key('Spells Per Day')):
#    print "I",i
    for j in i["Spells Per Day"]:
#      print "J",j
      if (i["Spells Per Day"][j]):
        for k in i["Spells Per Day"][j]:
#          print "K",k
          if (k<minspelllevel):
            minspelllevel=k
          if (k>maxspelllevel):
            maxspelllevel=k
  print "| Level | Base Attack Bonus | Fort Save | Ref Save | Will Save | Special ",
  if (maxspelllevel>-1):
    for j in range(minspelllevel,maxspelllevel+1):
      print " | "+str(j),
  if (i.has_key('Flurry of Blows')):
    print " | ", "Flurry of Blows",
  if (i.has_key('Unarmed Damage')):
    print " | ", "Unarmed Damage",
  if (i.has_key('AC Bonus')):
    print " | ", "AC Bonus",
  if (i.has_key('Unarmored Speed Bonus')):
    print " | ", "Unarmored Speed Bonus",

  print
  
  for j in range(1,21):
    features=""
    for k in i["Class Features"]:
      if (i["Class Features"][k]["Level"]==j):
        if (i["Class Features"][k].has_key("Short")):
          features=features+i["Class Features"][k]["Short"]+", "

    print "| " + str(j) + " | +" + str(bab(j,i["Base Attack Bonus"])) + " | +" + str(saves(j,i["Saves"]["Fortitude"])) + " | +" + str(saves(j,i["Saves"]["Reflex"])) + " | +" + str(saves(j,i["Saves"]["Will"])) + " | " + features.rstrip(", "),
    if (i.has_key('Spells Per Day')):
      for k in range(minspelllevel,maxspelllevel+1):
        if (i["Spells Per Day"][j]):
          if (i["Spells Per Day"][j].has_key(k)):
            print " | ",
            print i["Spells Per Day"][j][k],
          else:
            print " | - ",
        else:
          print " | - ",
    if (i.has_key('Flurry of Blows')):
      print " | ", i["Flurry of Blows"][j],
    if (i.has_key('Unarmed Damage')):
      print " | ", i["Unarmed Damage"][j],
    if (i.has_key('AC Bonus')):
      print " | ", i["AC Bonus"][j],
    if (i.has_key('Unarmored Speed Bonus')):
      print " | ", i["Unarmored Speed Bonus"][j],
    print  
    
  print "|====="
  print  

  if (i.has_key('Spells Known')):
    print ".Spells Known"
    print '[options="header"]';
    print "|=====";
    print "| Level ",
    for k in range(minspelllevel,maxspelllevel+1):
      print "| ",k," ",
    print
    for j in range(1,21):
      print "| ",j,
      for k in range(minspelllevel,maxspelllevel+1):
        if (i["Spells Known"][j].has_key(k)):
          print "| ", i["Spells Known"][j][k]," ",
        else:
          print "| -  ",
    print
    print "|=====";

  underline("^","Class Features")
  for k in range(0,21):
    for j in i["Class Features"]:
      if (i["Class Features"][j]["Level"]==k):
        if (i["Class Features"][j].has_key("Description")):
          print "indexterm:["+j+"]"
          print "*" + j + ":* " + i["Class Features"][j]["Description"].replace("\n","\n\n")
          print
        #["Description"]
  print

  if (i.has_key("Ex")):
    underline("^","Ex-"+i["Name"]+"s")
    print i["Ex"]["Description"]
    print
  if (i.has_key("Animal Companion")):
    print i["Animal Companion"]
  if (i.has_key("Familiar")):
    print i["Familiar"]
  if (i.has_key("Variants")):
    for j in i["Variants"]:
      print i["Variants"][j]