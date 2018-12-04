from django.test import TestCase
from .models import *

def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

def creategame(self, name="testgame", startdate=timezone.now(), enddate=timezone.now(), difficulty="easy", category="test"):
        return game(name=name, startdate=timezone.now(), difficulty=timezone.now())

#Test creation of class
def test_whatever_creation(self):
        game = self.create_whatever()
        self.assertTrue(isinstance(game, game.name="testgame"))
        self.assertEqual(game.__unicode__(), game.title)

#test view
def test_whatever_list_view(self):
        game = self.creategame()
        url = reverse("")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)

#Checks to see if the form is working
def testvalidform(self):
    g = Game.objects.create(title='Foo', body='Bar')
    data = {'title': g.name, 'body': g.name,}
    form = Form(data=data)
    self.assertTrue(form.is_valid())

#Checks to see if the JSON API is working
def testapi(self):
        resp = self.api_client.get('https://opentdb.com/api.php?amount=10&category=9&type=multiple', format='json')
        self.assertValidJSONResponse(resp)
