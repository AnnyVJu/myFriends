import json
from django.http import HttpResponse
from django.views import View


class JsonView(View):
    def json_to_response(self, data):
        return HttpResponse(content=json.dumps(data), content_type='application/json')

    def json_error(self, message='Unknown error', error_code="unknown"):
        data = {
            'result': 'error',
            'message': message,
            'code': error_code
        }
        return HttpResponse(content=json.dumps(data), content_type='application/json')

    def json_success(self, data):
        data = {
            'result': 'success',
            'data': data
        }
        return HttpResponse(content=json.dumps(data), content_type="application/json")

    def handle(self, request, *args, **kwargs):
        return self.json_to_response({'result': 'nothing'})


class AuthView(JsonView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return self.handle(request, *args, **kwargs)
        else:
            return self.json_error('User is not authenticated')
