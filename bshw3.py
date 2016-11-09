# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
print("i should start my homework")
print("start with homework 2 part C")
print("use the string matching from homework1")

f = open('hw3bshw3.html', 'r+')
f2 = open('hw3.html', "w")
for line in f:
	if line.find('student')!= -1:
		f2.write(line.replace('student', 'AMAZING student'))
	elif line.find('iframe') != -1:
		f2.write(line.replace('https://www.youtube.com/embed/mimp_3gquc4?feature=oembed', 'picofme.png'))
	elif line.find("/sites/default/themes/umsi/imgs/logo_footer.png") != -1:
		f2.write(line.replace("/sites/default/themes/umsi/imgs/logo_footer.png" , 'media/logo.png'))
	else:
		f2.write(line)

