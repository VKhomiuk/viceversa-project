from django.shortcuts import render

def home(reqest):
	return render(reqest, 'home.html')
def reverse(reqest):
	user_text = reqest.GET['usertext']
	reversed_text = user_text[::-1]
	counter = len(user_text.split())
	return render(reqest, 'reverse.html', {'usertext': user_text, 'reverstext': reversed_text, 'counter': counter})