import puppy_state
import state_asleep
import state_play


class StateEat(puppy_state.PuppyState):
  def play(self, puppy):
  #Changes the puppy's state to playing and returns a string description.
    puppy.inc_plays()
    puppy.change_state(state_play.StatePlay())
    return "The puppy looks up from its food and chases the ball you threw."

  def feed(self, puppy):
  #Changes the puppy's state if fed enough times in a row and returns a string description.
    puppy.inc_feeds()
    if puppy.feeds < 3:
      return "The puppy continues to eat as you add another scoop of kibble to its bowl."
    else:
      # the puppy has eaten enough times in a row, change state to asleep
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return "The puppy ate so much it fell asleep!"

