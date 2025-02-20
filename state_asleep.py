import puppy_state
import state_eat


class StateAsleep(puppy_state.PuppyState):

  def feed(self, puppy):
  #Changes the puppy's state to eat when it wakes up from being asleep. 
  #Returns a string describing the puppy's reaction.
    puppy.inc_feeds()
    puppy.change_state(state_eat.StateEat())
    return "The puppy wakes up and comes running to eat."

  def play(self, puppy):
  #Returns a string describing the puppy's reaction to playing when it is asleep.
    return "The puppy is asleep. It doesn't want to play right now."
