import sys
import math
import time



class ProgressBar(object):
    """A progress bar used in command line.
        Args:
            epochs (int): the epochs of the job configured by user
            steps (int, optional): the number of steps which progress bar composite of them
        Sampler:
            all = 5000
            progress = ProgressBar(5000)
            for i in range(all+1):
                time.sleep(0.0005)
                progress.step(i)
    """
    def __init__(self, epochs, steps=100):
        self.epochs = epochs
        self.steps = steps
        self.current_step = 0
        self.undo_step = 0


    def step(self, current_epoch):
        percent = self._count_percent(current_epoch)
        state = 'Running' if self.undo_step > 0 else 'Done'

        sys.stdout.write('\r')
        sys.stdout.write(percent + '% |' + '#' * self.current_step + '-' * self.undo_step + '|' + state)
        sys.stdout.flush()

        if self.epochs == current_epoch:
            print('\n')


    def _count_percent(self, current_epoch):
        self.current_step = math.ceil(current_epoch / self.epochs * self.steps)
        self.undo_step = self.steps - self.current_step
        percent = self.current_step / self.steps * 100 if self.undo_step > 0 else 100
        return '%3.0f' % percent