from rx import Observable, Observer

def news_events(observer):
  observer.on_next("Concurrency with Python Published!")
  observer.on_next("Book reaches top of the charts")
  observer.on_next("Author Retires Early")
  observer.on_completed()

class Subscriber(Observer):

  def __init__(self, ident):
    self.id = ident

  def on_next(self, value):
    print("Subscriber: {} Received: {}".format(self.id, value))

  def on_completed(self):
    print("Subscriber: {} Received All Important News".format(self.id))

  def on_error(self, error):
    print("Error Occurred: {}".format(error))

source = Observable.create(news_events)
source.subscribe(Subscriber("Grant"))
source.subscribe(Subscriber("Callum"))
source.subscribe(Subscriber("Sophie"))