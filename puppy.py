import state_asleep

class Puppy:
  def __init__(self):
    self._state = state_asleep.StateAsleep()
    self._feeds = 0
    self._plays = 0

  @property
  def feeds(self):
    return self._feeds

  @property
  def plays(self):
    return self._plays

  def change_state(self, new_state):
  #Changes the puppy's state to the new state
    self._state = new_state

  def throw_ball(self):
  #Calls the play method for the current state
    return self._state.play(self)

  def give_food(self):
  #Calls the feed method for the current state
    return self._state.feed(self)

  def inc_feeds(self):
  #Increments the number of times the puppy has been fed in a row
    self._feeds += 1

  def inc_plays(self):
  #Increments the number of times the puppy has been played with in a row
    self._plays += 1

  def reset(self):
  #Resets the number of times the puppy has been fed and played with in a row
    self._plays = 0
    self._feeds = 0