class DecayingLearningRate:
  """
  This class implements a decaying learning rate schedule.
  """

  def __init__(self, initial_lr, decay_rate, min_lr=0.001):
    """
    Initializes the learning rate schedule.

    Args:
        initial_lr: The initial learning rate.
        decay_rate: The rate at which the learning rate decays (between 0 and 1).
        min_lr: The minimum allowed learning rate (optional, defaults to 0.001).
    """
    self.initial_lr = initial_lr
    self.decay_rate = decay_rate
    self.min_lr = min_lr
    self.current_lr = initial_lr  # Track current learning rate

  def getLearningRate(self, epoch):
    """
    Calculates the learning rate for a given epoch.

    Args:
        epoch: The current training epoch.

    Returns:
        The learning rate for the current epoch.
    """
    self.current_lr = max(self.initial_lr * (1 - self.decay_rate) ** epoch, self.min_lr)
    return self.current_lr

