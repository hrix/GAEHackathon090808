import os
import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.api import mail

class ConfirmInfo(webapp.RequestHandler):
  def get(self):

    template_values = {}

    path = os.path.join(os.path.dirname(__file__), 'view/index.html')
    self.response.out.write(template.render(path, template_values))

class SendMessage(webapp.RequestHandler):
  def post(self):
    user_address = self.request.get("email_address")
    template_values = {
      'user_address': user_address
    }
    if not mail.is_email_valid(user_address):
      path = os.path.join(os.path.dirname(__file__), 'view/error.html')
      self.response.out.write(template.render(path, template_values))
    else:
      #confirmation_url = createNewUserConfirmation(self.request)
      confirmation_url = 'just a test'
      sender_address = "hirai.sumito@gmail.com"
      subject = "Test For Gaepmail"
      body = self.request.get("content")
      mail.send_mail(sender_address, user_address, subject, body)

    path = os.path.join(os.path.dirname(__file__), 'view/sent.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
    [
     ('/', ConfirmInfo),
     ('/sent', SendMessage)
     ],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
