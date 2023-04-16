from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import RegionModel, B, S, R1, R2, R3, R4, R5, R6, SchoolName, BaBies
import csv

class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/login.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/register.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ForgotPasswordView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ChartsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/charts.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class TablesView(APIView):
    def get(self, request, *args, **kwargs):
        results = BaBies.objects.all()
        return render(request, "theme/tables.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class TablesView1(APIView):
    def get(self, request, *args, **kwargs):
        results = RegionModel.objects.all()
        return render(request, "theme/tables1.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})    
    
class TablesView2(APIView):
    def get(self, request, *args, **kwargs):
        results = S.objects.all()
        return render(request, "theme/tables2.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView3(APIView):
    def get(self, request, *args, **kwargs):
        results = R1.objects.all()
        return render(request, "theme/tables3.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView4(APIView):
    def get(self, request, *args, **kwargs):
        results = R2.objects.all()
        return render(request, "theme/tables4.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView5(APIView):
    def get(self, request, *args, **kwargs):
        results = R3.objects.all()
        return render(request, "theme/tables5.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView6(APIView):
    def get(self, request, *args, **kwargs):
        results = R4.objects.all()
        return render(request, "theme/tables6.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView7(APIView):
    def get(self, request, *args, **kwargs):
        results = R5.objects.all()
        return render(request, "theme/tables7.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView8(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/tables8.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ButtonsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/buttons.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class CardsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/cards.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class PageNotFoundView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/404.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BlankView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/blank.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ColorsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-color.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BordersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-border.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class AnimationsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-animation.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class OthersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-other.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})



class DashboardView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "users/dashboard.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class Map_View(APIView):
    def get(self, request, *args, **kwargs):
        # with open('C:/Users/kdh15/sbadmin/xy.csv', 'r', encoding='utf-8') as f:
        #     reader = csv.reader(f)
        #     data = []
        #     for row in reader:
        #         data.append({'longitude': row[1], 'latitude': row[0]})
        # df = open('C:\Users\kdh15\sbadmin\location.csv', 'r',encoding = 'utf-8')
        # rdr = csv.reader(df)
        # for line in rdr:
            
        results = SchoolName.objects.all()
        return render(request, "theme/map.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})