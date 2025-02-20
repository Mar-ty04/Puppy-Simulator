import abc


class PuppyState(abc.ABC):
  @abc.abstractmethod
  def feed(self, puppy):
  #Abstract method for feeding the puppy.
    raise NotImplementedError()
    
  @abc.abstractmethod
  def play(self, puppy):
  #Abstract method for playing with the puppy.
    raise NotImplementedError()
        
