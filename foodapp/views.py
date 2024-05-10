from django.shortcuts import render

# Create your views here.
class FoodList(APIView):
    def get(self, request):
        food = Food.objects.all()
        query = self.request.GET.get('search')
