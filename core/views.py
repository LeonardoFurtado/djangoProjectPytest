from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.auth import get_auth_context


class ProfileView(APIView):
    def post(self, request):
        auth_context = get_auth_context(1) # expected: 2 but i will mock it as 3
        if auth_context == 2:
            return Response(
                {
                    "success": False,
                    "error": "The get_auth_context is returning the number 2 instead of the mocked value 3.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        elif auth_context == 3:
            return Response(
                {
                    "success": True,
                    "error": "Ok. The get_auth_context is returning the mocked value",
                },
                status=status.HTTP_200_OK,
            )


