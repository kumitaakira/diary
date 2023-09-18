from django.contrib.auth import get_user_model
from django.test import TestCase,Client,RequestFactory

from snippets.models import Snippet
from snippets.views import top

UserModel=get_user_model()

class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user=UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.snippet=Snippet.objects.create(
            title="title",
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )
    def test_should_return_snippet_title(self):
        request=RequestFactory().get("/")
        request.user=self.user
        response=top(request)
        self.assertContains(response,self.snippet.title)

    def test_should_return_username(self):
    
        request=RequestFactory().get("/")
        request.user=self.user
        response=top(request)
        self.assertContains(response,self.user.username) # type: ignore


class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user=UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.snippet=Snippet.objects.create(
            title="title",
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )

    def test_should_use_expected_template(self):
        response=self.client.get("/snippets/%s/"%self.snippet.id) # type: ignore
        self.assertContains(response,self.snippet.title,status_code=200)


class CreateSnippetTest(TestCase):
    def setUp(self):
        self.user=UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
        )
        self.client.force_login(self.user)
    def test_render_creation_form(self):
        response=self.client.get("/snippets/new/")
        self.assertContains(response,"スニペットの登録",status_code=200)

    def test_create_snippet(self):
        data={'title':'タイトル','code':'コード','description':'解説'}
        self.client.post("/snippets/new/",data)
        snippet=Snippet.objects.get(title='タイトル')
        self.assertEqual('コード',snippet.code)
        self.assertEqual('解説',snippet.description)

    


        
