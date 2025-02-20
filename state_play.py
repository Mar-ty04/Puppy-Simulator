import puppy_state
import state_asleep

class StatePlay(puppy_state.PuppyState):
#Changes the state to the puppy playing.Returns a string of a puppy playing
  
  def play(self, puppy):
  #Returns a string describing the puppy playing."""
    puppy.inc_plays()
    if puppy.plays == 3:
    #if puppy has played 3 times, change state to asleep
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return "You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!"

    else:
      return "You throw the ball again and the puppy excitedly chases it."

  def feed(self, puppy):
  #Returns a string describing the puppy not being fed.
    return "The puppy is too busy playing with the ball to eat right now."