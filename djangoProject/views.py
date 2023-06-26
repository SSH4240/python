import APIView as APIView


class test(APIView):
    def get(self, request):
        print('겟으로 호출')
        return render(request, "testPage/test.html")
    def post(self, request):
        print('포스트로 호출')
        return render(request, 'testPage/test.html')