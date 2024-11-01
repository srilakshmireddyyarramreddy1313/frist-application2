from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.
def display(request):

   ss = '''
          <center>
            <h2>  
               hello user,welcome to django Frist-project
               Frist-App
            </h2>
            <hr/>
          </center>
        ''';
     return HttpResponse(ss);   
        