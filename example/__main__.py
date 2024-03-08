import time
from .xeryon import Stage, Units, Xeryon

controller = Xeryon("/dev/tty.usbmodem1101")
axisX = controller.addAxis(Stage.XLS_312, "X")
axisY = controller.addAxis(Stage.XLS_312, "Y")

controller.start()

# For some reason we need to wait 1 second after starting the controller to
# avoid "Index is not found, but stopped searching for index" errors.
time.sleep(1)

for axis in controller.getAllAxis():
    axis.findIndex()
